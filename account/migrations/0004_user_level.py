# Generated by Django 5.0.2 on 2024-05-04 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_level'),
        ('blog', '0004_level_blog_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.level'),
        ),
    ]
