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
    Webinar, Member, NavigationLink, FooterColumn, FooterLink
)


def homepage(request):
    hero = HeroSection.objects.filter(page='homepage').first()
    carousel_items = CarouselItem.objects.filter(hero_section=hero) if hero else []
    news_tickers = NewsTickerItem.objects.filter(is_active=True).order_by('order')
    quick_access_cards = QuickAccessCard.objects.filter(page='homepage').order_by('order')
    stats_counters = StatisticCounter.objects.filter(page='homepage').order_by('order')
    member_spotlights = MemberSpotlight.objects.filter(is_featured=True).order_by('order')
    research_highlights = ResearchHighlight.objects.all().order_by('order')
    events = Event.objects.all().order_by('order', 'date')
    # Use the latest CallToAction entry for homepage (most recent).
    # We keep the model's order field available but prefer the latest DB entry
    # so content managers can update the hero CTA by creating a new entry.
    call_to_action = CallToAction.objects.filter(page='homepage').order_by('-id').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

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
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/homepage.html', context)


def about(request):
    hero = HeroSection.objects.filter(page='about').first()
    board_members = BoardMember.objects.all().order_by('order')
    committees = Committee.objects.all().order_by('order')
    partnerships = Partnership.objects.all().order_by('order')
    awards = Award.objects.all().order_by('order', '-year')
    call_to_action = CallToAction.objects.filter(page='about').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

    context = {
        'hero': hero,
        'board_members': board_members,
        'committees': committees,
        'partnerships': partnerships,
        'awards': awards,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/about.html', context)


def knowledge_center(request):
    hero = HeroSection.objects.filter(page='knowledge_center').first()
    resource_categories = ResourceCategory.objects.all().order_by('order')
    resources = ResourceItem.objects.all().order_by('order')
    webinars = Webinar.objects.all().order_by('order')
    call_to_action = CallToAction.objects.filter(page='knowledge_center').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

    context = {
        'hero': hero,
        'resource_categories': resource_categories,
        'resources': resources,
        'webinars': webinars,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/knowledge_center.html', context)


def member_directory(request):
    hero = HeroSection.objects.filter(page='member_directory').first()
    members = Member.objects.all().order_by('order')
    call_to_action = CallToAction.objects.filter(page='member_directory').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

    context = {
        'hero': hero,
        'members': members,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/member_directory.html', context)


def news_and_updates(request):
    hero = HeroSection.objects.filter(page='news_and_updates').first()
    news_tickers = NewsTickerItem.objects.filter(is_active=True).order_by('order')
    events = Event.objects.all().order_by('order', 'date')
    call_to_action = CallToAction.objects.filter(page='news_and_updates').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

    context = {
        'hero': hero,
        'news_tickers': news_tickers,
        'events': events,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/news_and_updates.html', context)


def research_and_publications(request):
    hero = HeroSection.objects.filter(page='research_and_publications').first()
    research_highlights = ResearchHighlight.objects.all().order_by('order')
    annual_reports = AnnualReport.objects.all().order_by('-year')
    call_to_action = CallToAction.objects.filter(page='research_and_publications').first()
    navigation_links = NavigationLink.objects.filter(is_active=True).order_by('order')
    footer_columns = FooterColumn.objects.all().order_by('order').prefetch_related('links')

    context = {
        'hero': hero,
        'research_highlights': research_highlights,
        'annual_reports': annual_reports,
        'call_to_action': call_to_action,
        'navigation_links': navigation_links,
        'footer_columns': footer_columns,
    }
    return render(request, 'pages/research_and_publications.html', context)