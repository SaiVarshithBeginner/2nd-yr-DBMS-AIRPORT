# Generated by Django 4.2.4 on 2023-11-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], max_length=45),
        ),
    ]
