# Generated by Django 2.1.3 on 2018-12-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0014_auto_20181118_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcd',
            name='_cwr',
            field=models.BooleanField(default=False, editable=False, verbose_name='CWR-Ready'),
        ),
        migrations.AlterField(
            model_name='alternatetitle',
            name='_cwr',
            field=models.BooleanField(default=False, editable=False, verbose_name='CWR-Ready'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='_cwr',
            field=models.BooleanField(default=False, editable=False, verbose_name='CWR-Ready'),
        ),
        migrations.AlterField(
            model_name='firstrecording',
            name='_cwr',
            field=models.BooleanField(default=False, editable=False, verbose_name='CWR-Ready'),
        ),
        migrations.AlterField(
            model_name='work',
            name='_cwr',
            field=models.BooleanField(default=False, editable=False, verbose_name='CWR-Ready'),
        ),
        migrations.AlterUniqueTogether(
            name='albumcd',
            unique_together=set(),
        ),
    ]