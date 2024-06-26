# Generated by Django 5.0.6 on 2024-06-24 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_entreprise_webdatapass_entreprise_nombrecdc'),
        ('discover', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CahierDesCharges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.entreprise')),
            ],
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
