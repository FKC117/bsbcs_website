from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default='BSBCS')
    abbreviation = models.CharField(max_length=50, blank=True, null=True)
    tag_line = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='site_settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site_settings/', blank=True, null=True)
    footer_content = models.TextField(blank=True, null=True)
    contact_mail = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    footer_copyright = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Settings"


class NavigationLink(models.Model):
    label = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)  # Django URL name or external URL
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['order']


class HeroSection(models.Model):
    PAGE_CHOICES = [
        ('homepage', 'Homepage'),
        ('about', 'About'),
        ('knowledge_center', 'Knowledge Center'),
        ('member_directory', 'Member Directory'),
        ('news_and_updates', 'News and Updates'),
        ('research_and_publications', 'Research and Publications'),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='images/hero/', blank=True, null=True)  # SVG content or path reference

    def __str__(self):
        return f"{self.page} Hero - {self.title}"


class CarouselItem(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='carousel_items')
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='images/carousel/', blank=True, null=True)
    badge_text = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class NewsTickerItem(models.Model):
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']


class QuickAccessCard(models.Model):
    PAGE_CHOICES = HeroSection.PAGE_CHOICES

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page} QuickAccess - {self.title}"

    class Meta:
        ordering = ['order']


class StatisticCounter(models.Model):
    PAGE_CHOICES = HeroSection.PAGE_CHOICES

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    title = models.CharField(max_length=255)
    count_text = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page} StatisticCounter - {self.title}"

    class Meta:
        ordering = ['order']


class MemberSpotlight(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='images/members/', blank=True, null=True)
    profile_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ResearchHighlight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    lead_researcher_name = models.CharField(max_length=255, blank=True, null=True)
    lead_researcher_image_url = models.ImageField(upload_to='images/researchers/', blank=True, null=True)
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    journal_link = models.URLField(blank=True, null=True)    
    highlight = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('webinar', 'Webinar'),
        ('meeting', 'Meeting'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    registration_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.date})"

    class Meta:
        ordering = ['order', 'date']


class CallToAction(models.Model):
    PAGE_CHOICES = HeroSection.PAGE_CHOICES

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    primary_button_text = models.CharField(max_length=100, blank=True, null=True)
    secondary_button_text = models.CharField(max_length=100, blank=True, null=True)
    primary_button_url = models.URLField(blank=True, null=True)
    secondary_button_url = models.URLField(blank=True, null=True)
    background_svg = models.ImageField(upload_to='images/backgrounds/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page} CTA - {self.title}"

    class Meta:
        ordering = ['order']


class BoardMember(models.Model):
    ROLE_CHOICES = [
        ('president', 'President'),
        ('vice_president', 'Vice President'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('board_member', 'Board Member'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    qualifications = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='images/board/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)  # Example: {"linkedin": "url", "twitter": "url"}
    order = models.PositiveIntegerField(default=0)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='board_member')

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

    class Meta:
        ordering = ['order']


class Committee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    member_count = models.PositiveIntegerField(default=0)
    link_to_members = models.URLField(blank=True, null=True)
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Partnership(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Award(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['order', '-year']


class AnnualReport(models.Model):
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    file_upload = models.FileField(upload_to='files/annual_reports/', blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Annual Report {self.year}"

    class Meta:
        ordering = ['-year']


class ResourceCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ResourceItem(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('guideline', 'Guideline'),
        ('research_publication', 'Research Publication'),
        ('educational_material', 'Educational Material'),
        ('tool', 'Tool'),
        ('webinar', 'Webinar'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ResourceCategory, on_delete=models.SET_NULL, null=True, related_name='resources')
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    updated_date = models.DateField(blank=True, null=True)
    file_upload = models.FileField(upload_to='files/resources/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Webinar(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    presenter_name = models.CharField(max_length=255, blank=True, null=True)
    presenter_image_url = models.ImageField(upload_to='images/presenters/', blank=True, null=True)
    recorded_date = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    slides_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Member(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    research_interest = models.TextField(blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='images/members/', blank=True, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class OrganizationalValue(models.Model):
    VALUE_TYPE_CHOICES = [
        ('mission', 'Mission'),
        ('vision', 'Vision'),
        ('value', 'Value'),
    ]

    value_type = models.CharField(max_length=20, choices=VALUE_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.get_value_type_display()} - {self.title}"

    class Meta:
        ordering = ['value_type', 'order']
        verbose_name_plural = "Organizational Values"


class TimelineSection(models.Model):
    """A header section for the About page timeline.

    Contains an optional intro and icon; `TimelineItem` children represent
    individual timeline events ordered for display.
    """

    title = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class TimelineItem(models.Model):
    section = models.ForeignKey(TimelineSection, on_delete=models.CASCADE, related_name='items')
    event_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon_svg = models.ImageField(upload_to='images/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.section.title} - {self.title}"

    class Meta:
        ordering = ['order']