# Generated by Django 4.2.3 on 2023-07-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일'),
        ),
    ]
