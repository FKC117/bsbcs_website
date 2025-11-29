from django import template
from django.urls import reverse, NoReverseMatch
from django.core.cache import cache

from website.models import SiteSettings, NavigationLink

register = template.Library()

# Cache timeout (in seconds): 1 hour
CACHE_TIMEOUT = 3600


@register.simple_tag
def get_site_settings():
    """Return the first SiteSettings instance or None.
    
    Results are cached for 1 hour to reduce database queries.
    """
    cached = cache.get('site_settings')
    if cached is not None:
        return cached
    
    settings = SiteSettings.objects.first()
    cache.set('site_settings', settings, CACHE_TIMEOUT)
    return settings


@register.simple_tag
def get_navigation_links():
    """Return a list of navigation link dicts: {'label':..., 'url':...}.

    This resolves URL names when possible and falls back to the stored value.
    Results are cached for 1 hour to reduce database queries.
    """
    cached = cache.get('navigation_links')
    if cached is not None:
        return cached
    
    navs = []
    for nav in NavigationLink.objects.filter(is_active=True).order_by('order'):
        url = nav.url_name or ''
        try:
            url = reverse(nav.url_name) if nav.url_name else ''
        except (NoReverseMatch, TypeError):
            url = nav.url_name
        navs.append({'label': nav.label, 'url': url})
    
    cache.set('navigation_links', navs, CACHE_TIMEOUT)
    return navs
