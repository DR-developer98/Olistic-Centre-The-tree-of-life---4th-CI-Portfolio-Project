# Generated by Django 4.2.23 on 2025-07-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0003_alter_treatment_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]
