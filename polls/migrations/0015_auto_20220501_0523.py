# Generated by Django 3.2.5 on 2022-05-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20220428_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='date_edit',
            field=models.DateField(verbose_name='date edition'),
        ),
        migrations.AlterField(
            model_name='societe',
            name='date_creation',
            field=models.DateField(verbose_name='date creation'),
        ),
    ]
