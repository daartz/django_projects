# Generated by Django 3.2.5 on 2022-04-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='nom',
            new_name='raison_sociale',
        ),
        migrations.AddField(
            model_name='client',
            name='interlocuteur',
            field=models.CharField(default='Nothing', max_length=200),
            preserve_default=False,
        ),
    ]
