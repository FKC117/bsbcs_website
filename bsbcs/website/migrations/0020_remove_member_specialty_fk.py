from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_member_specialties_m2m'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='specialty_fk',
        ),
    ]
