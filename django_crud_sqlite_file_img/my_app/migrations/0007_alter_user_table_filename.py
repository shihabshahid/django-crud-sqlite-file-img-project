# Generated by Django 4.2.3 on 2023-07-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_user_table_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='filename',
            field=models.ImageField(upload_to='django_crud_sqlite_file_img/static/uploads'),
        ),
    ]