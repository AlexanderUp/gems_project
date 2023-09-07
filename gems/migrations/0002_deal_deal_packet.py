# Generated by Django 4.2.5 on 2023-09-07 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='deal_packet',
            field=models.ForeignKey(
                default=1,
                help_text='Deal Packet',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='deals',
                to='gems.dealpacket',
                verbose_name='deal_packet',
            ),
            preserve_default=False,
        ),
    ]