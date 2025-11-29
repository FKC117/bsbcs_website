from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed minimal SiteSettings and NavigationLink entries for development.'

    def handle(self, *args, **options):
        from website.models import SiteSettings, NavigationLink

        # Create SiteSettings if missing
        settings = SiteSettings.objects.first()
        if not settings:
            settings = SiteSettings.objects.create(
                site_name='BSBCS',
                abbreviation='Breast Cancer Studies',
                footer_content='Advancing breast cancer care through collaborative excellence, research, and education.',
                footer_copyright='© 2025 Bangladesh Society of Breast Cancer Studies. All Rights Reserved.',
            )
            self.stdout.write(self.style.SUCCESS('Created default SiteSettings'))
        else:
            self.stdout.write('SiteSettings already exists')

        # Seed NavigationLink entries if none exist
        if not NavigationLink.objects.exists():
            navs = [
                ('Home', 'homepage', 0),
                ('About', 'about', 1),
                ('Members', 'member_directory', 2),
                ('Research', 'research_and_publications', 3),
                ('Resources', 'knowledge_center', 4),
                ('News', 'news_and_updates', 5),
            ]
            for label, url_name, order in navs:
                NavigationLink.objects.create(label=label, url_name=url_name, order=order, is_active=True)
            self.stdout.write(self.style.SUCCESS('Seeded NavigationLink entries'))
        else:
            self.stdout.write('NavigationLink entries already present')