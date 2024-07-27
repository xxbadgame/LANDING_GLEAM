# Generated by Django 5.0.6 on 2024-06-27 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_entreprise_webdatapass_entreprise_nombrecdc'),
        ('discover', '0002_cahierdescharges_delete_conversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collecte', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.entreprise')),
            ],
        ),
    ]