# Generated by Django 4.2.6 on 2023-10-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gadgets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7OD-PXxcJaOcBjEXnay7aD8VNMoiUgfXm3Q&usqp=CAU', max_length=500),
        ),
    ]
