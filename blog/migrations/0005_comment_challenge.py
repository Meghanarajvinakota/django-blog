# Generated by Django 4.2.15 on 2024-09-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='this_is_a_slug'),
            preserve_default=False,
        ),
    ]
