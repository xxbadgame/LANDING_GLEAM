# Generated by Django 5.0.6 on 2024-06-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_entreprise_companyinformation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='WebDataPass',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='nombreCDC',
            field=models.IntegerField(default=0),
        ),
    ]
