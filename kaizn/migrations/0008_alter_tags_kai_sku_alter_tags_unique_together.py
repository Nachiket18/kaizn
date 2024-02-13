# Generated by Django 5.0.2 on 2024-02-13 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizn', '0007_remove_users_kai_insert_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='kai_SKU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='kaizn.items'),
        ),
        migrations.AlterUniqueTogether(
            name='tags',
            unique_together={('kai_SKU', 'kai_tags')},
        ),
    ]
