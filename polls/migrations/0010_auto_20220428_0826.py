# Generated by Django 3.2.5 on 2022-04-28 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_facture_mission_refclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='facture',
            name='statut',
        ),
        migrations.AddField(
            model_name='facture',
            name='id_statut',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.statut'),
        ),
    ]
