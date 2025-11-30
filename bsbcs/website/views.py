from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from pathlib import Path
import os
from django.http import FileResponse
from django.conf import settings

def favicon(request):
    favicon_path = os.path.join(settings.BASE_DIR, 'website', 'static', 'img', 'favicon.ico')
    return FileResponse(open(favicon_path, 'rb'))
from django.shortcuts import render
from .models import (
    HeroSection, CarouselItem, NewsTickerItem, QuickAccessCard, StatisticCounter,
    MemberSpotlight, ResearchHighlight, Event, CallToAction, BoardMember,
    Committee, Partnership, Award, AnnualReport, ResourceCategory, ResourceItem,
    Webinar, Member, NavigationLink, OrganizationalValue
)


def homepage(request):
    hero = HeroSection.objects.filter(page='homepage').first()
    carousel_items = CarouselItem.objects.filter(hero_section=hero) if hero else []
    news_tickers = NewsTickerItem.objects.filter(is_active=True).order_by('order')
    quick_access_cards = QuickAccessCard.objects.filter(page='homepage').order_by('order')
    stats_counters = StatisticCounter.objects.filter(page='homepage').order_by('order')
    member_spotlights = MemberSpotlight.objects.filter(is_featured=True).order_by('order')
    # Only show highlights flagged for homepage (highlight=True)
    research_highlights = ResearchHighlight.objects.filter(highlight=True).order_by('order')
    events = Event.objects.all().order_by('order', 'date')
    # Use the latest CallToAction entry for homepage (most recent).
    # We keep the model's order field available but prefer the latest DB entry
    # so content managers can update the hero CTA by creating a new entry.
    call_to_action = CallToAction.objects.filter(page='homepage').order_by('-id').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')

    context = {
        'hero': hero,
        'carousel_items': carousel_items,
        'news_tickers': news_tickers,
        'quick_access_cards': quick_access_cards,
        'stats_counters': stats_counters,
        'member_spotlights': member_spotlights,
        'research_highlights': research_highlights,
        'events': events,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
    }
    return render(request, 'pages/homepage.html', context)


def about(request):
    hero = HeroSection.objects.filter(page='about').first()
    stats_counters = StatisticCounter.objects.filter(page='about').order_by('order')
    board_members = BoardMember.objects.all().order_by('order')
    committees = Committee.objects.all().order_by('order')
    partnerships = Partnership.objects.all().order_by('order')
    awards = Award.objects.all().order_by('order', '-year')
    call_to_action = CallToAction.objects.filter(page='about').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    
    # Fetch organizational values grouped by type
    mission = OrganizationalValue.objects.filter(value_type='mission').first()
    vision = OrganizationalValue.objects.filter(value_type='vision').first()
    values = OrganizationalValue.objects.filter(value_type='value').order_by('order')

    # Prepare values_items for the template. If there are multiple `value` rows,
    # use each row's title as an item. If there is a single `value` row which
    # contains a multi-line description (e.g. authors pasted a list into the
    # description field), split it into list items for rendering.
    import re
    values_items = []
    if values.count() > 1:
        for v in values:
            # prefer the title for short list items, fallback to description
            text = v.title or (v.description or '').strip()
            if text:
                values_items.append(text)
    elif values.count() == 1:
        single = values.first()
        desc = (single.description or '').strip()
        if desc:
            # split on newlines first
            parts = [p.strip() for p in re.split(r'[\r\n]+', desc) if p.strip()]
            if len(parts) == 1:
                # if still single, try splitting on common separators
                parts = [p.strip() for p in re.split(r'[;\u2022,]+', desc) if p.strip()]
            values_items = parts
        else:
            # no description, use the title as a single item
            if single.title:
                values_items = [single.title]
    
    # Determine a header title and icon for the Values card.
    # Prefer an explicit "Values" meta row when present (title like 'Values' or 'Our Values').
    values_header_title = 'Values'
    values_header_icon_url = None
    if values.exists():
        # try to find a meta/header row
        header = values.filter(title__iregex=r'^(values|our values?)$').first()
        if header:
            values_header_title = header.title
            if header.icon_svg:
                values_header_icon_url = header.icon_svg.url
        else:
            # no explicit header row: if there's a single row, use its title/icon as header
            if values.count() == 1:
                single = values.first()
                values_header_title = single.title or values_header_title
                if single.icon_svg:
                    values_header_icon_url = single.icon_svg.url
            else:
                # multiple rows and no header candidate: leave generic title and no icon
                values_header_title = 'Values'

    context = {
        'hero': hero,
        'stats_counters': stats_counters,
        'board_members': board_members,
        'committees': committees,
        'partnerships': partnerships,
        'awards': awards,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'mission': mission,
        'vision': vision,
        'values': values,
        'values_items': values_items,
        'values_header_title': values_header_title,
        'values_header_icon_url': values_header_icon_url,
    }
    return render(request, 'pages/about.html', context)


def knowledge_center(request):
    hero = HeroSection.objects.filter(page='knowledge_center').first()
    resource_categories = ResourceCategory.objects.all().order_by('order')
    resources = ResourceItem.objects.all().order_by('order')
    webinars = Webinar.objects.all().order_by('order')
    call_to_action = CallToAction.objects.filter(page='knowledge_center').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')

    context = {
        'hero': hero,
        'resource_categories': resource_categories,
        'resources': resources,
        'webinars': webinars,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
    }
    return render(request, 'pages/knowledge_center.html', context)


def member_directory(request):
    hero = HeroSection.objects.filter(page='member_directory').first()
    members = Member.objects.all().order_by('order')
    call_to_action = CallToAction.objects.filter(page='member_directory').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')

    context = {
        'hero': hero,
        'members': members,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
    }
    return render(request, 'pages/member_directory.html', context)


def news_and_updates(request):
    hero = HeroSection.objects.filter(page='news_and_updates').first()
    news_tickers = NewsTickerItem.objects.filter(is_active=True).order_by('order')
    events = Event.objects.all().order_by('order', 'date')
    call_to_action = CallToAction.objects.filter(page='news_and_updates').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')

    context = {
        'hero': hero,
        'news_tickers': news_tickers,
        'events': events,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
    }
    return render(request, 'pages/news_and_updates.html', context)


def research_and_publications(request):
    hero = HeroSection.objects.filter(page='research_and_publications').first()
    stats_counters = StatisticCounter.objects.filter(page='research_and_publications').order_by('order')
    research_highlights = ResearchHighlight.objects.all().order_by('order')
    annual_reports = AnnualReport.objects.all().order_by('-year')
    call_to_action = CallToAction.objects.filter(page='research_and_publications').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')

    context = {
        'hero': hero,
        'stats_counters': stats_counters,
        'research_highlights': research_highlights,
        'annual_reports': annual_reports,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
    }
    return render(request, 'pages/research_and_publications.html', context)