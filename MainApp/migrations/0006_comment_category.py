# Generated by Django 3.2.18 on 2023-05-15 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_rename_name_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='MainApp.category'),
            preserve_default=False,
        ),
    ]
