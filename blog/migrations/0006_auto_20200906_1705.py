# Generated by Django 2.2.16 on 2020-09-06 17:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200906_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='authors',
            field=wagtail.core.fields.StreamField([('author', wagtail.core.blocks.CharBlock(max_length=50))], null=True),
        ),
    ]
