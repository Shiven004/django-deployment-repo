# Generated by Django 3.0.3 on 2020-05-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
    ]
