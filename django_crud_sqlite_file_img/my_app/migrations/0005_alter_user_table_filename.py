# Generated by Django 4.2.3 on 2023-07-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_user_table_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='filename',
            field=models.ImageField(upload_to='uploads/%y'),
        ),
    ]
