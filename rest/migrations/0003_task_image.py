# Generated by Django 3.2.11 on 2022-01-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
