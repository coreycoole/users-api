# Generated by Django 2.2 on 2019-12-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField()),
                ('login_count', models.IntegerField()),
                ('project_count', models.IntegerField()),
            ],
        ),
    ]
