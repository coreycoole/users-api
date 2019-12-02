# Generated by Django 2.2 on 2019-12-02 01:18

from django.db import migrations

def populaute_UserProfiles(apps, schema_editor):
    UserProfile = apps.get_model('profiles_api', 'UserProfile')
    for profile in UserProfile.objects.all():
        profile.id = profile.id
        profile.username = profile.username
        profile.last_login = profile.last_login
        profile.login_count = profile.login_count
        profile.project_count = profile.project_count
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populaute_UserProfiles),
    ]
