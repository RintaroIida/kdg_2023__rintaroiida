# Generated by Django 4.2.9 on 2024-01-30 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_review_alter_post_image_delete_comment_review_book_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
