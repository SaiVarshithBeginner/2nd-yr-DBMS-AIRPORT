# Generated by Django 4.2.4 on 2023-11-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='passengers',
        ),
        migrations.AddField(
            model_name='ticket',
            name='passengers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
