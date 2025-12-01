from django.db import migrations, models


def copy_specialty_fk_to_m2m(apps, schema_editor):
    Member = apps.get_model('website', 'Member')
    Speciality = apps.get_model('website', 'Speciality')
    for member in Member.objects.all():
        try:
            # If a specialty FK exists, add it to the new M2M
            if member.specialty_fk_id:
                sp = Speciality.objects.filter(pk=member.specialty_fk_id).first()
                if sp:
                    member.specialties.add(sp)
        except Exception:
            # Keep migration resilient; ignore rows that fail
            pass


def reverse_copy(apps, schema_editor):
    Member = apps.get_model('website', 'Member')
    for member in Member.objects.all():
        # set specialty_fk to first specialty if present
        try:
            specs = member.specialties.all()
            if specs.exists():
                member.specialty_fk = specs.first()
                member.save()
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_remove_member_research_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='specialties',
            field=models.ManyToManyField(related_name='members_specialties', blank=True, to='website.Speciality'),
        ),
        migrations.RunPython(copy_specialty_fk_to_m2m, reverse_code=reverse_copy),
    ]
