# Generated by Django 5.0.6 on 2024-06-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0011_remove_tache_niveau_cahierdecharge_justificationnote_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tache',
            old_name='description',
            new_name='descriptionTache',
        ),
        migrations.RenameField(
            model_name='tache',
            old_name='prixTaches',
            new_name='prixTache',
        ),
        migrations.RenameField(
            model_name='tache',
            old_name='prixTachesConcurrents',
            new_name='prixTacheConcurrents',
        ),
        migrations.AddField(
            model_name='cahierdecharge',
            name='tempsProjet',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tache',
            name='tempsTache',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cahierdecharge',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cahierdecharge',
            name='justificationNote',
            field=models.TextField(null=True),
        ),
    ]
