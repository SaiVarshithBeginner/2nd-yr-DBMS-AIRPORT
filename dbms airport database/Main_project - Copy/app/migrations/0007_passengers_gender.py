# Generated by Django 4.2.4 on 2023-11-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_ticket_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengers',
            name='gender',
            field=models.CharField(default='Male', max_length=10, null=True),
        ),
    ]
