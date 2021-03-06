# Generated by Django 2.2.7 on 2019-11-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsapp', '0002_auto_20191107_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='info',
        ),
        migrations.AddField(
            model_name='info',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='danger',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='fond',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='house_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='last_changes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='serial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='stages',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='wall_mat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='wall_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='year_build',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='year_exp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='year_exp1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
