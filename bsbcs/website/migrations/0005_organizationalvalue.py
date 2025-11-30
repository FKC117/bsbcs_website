# Generated migration for OrganizationalValue model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_footercolumn_rename_tag_line_sitesettings_tag_line_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationalValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_type', models.CharField(choices=[('mission', 'Mission'), ('vision', 'Vision'), ('value', 'Value')], max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon_svg', models.ImageField(blank=True, null=True, upload_to='images/icons/')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Organizational Values',
                'ordering': ['value_type', 'order'],
            },
        ),
    ]
