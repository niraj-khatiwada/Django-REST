# Generated by Django 3.0.3 on 2020-02-23 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_profilefeed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeed',
            old_name='feed',
            new_name='feed_user',
        ),
    ]
