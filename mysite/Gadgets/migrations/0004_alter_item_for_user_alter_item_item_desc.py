# Generated by Django 4.2.6 on 2023-10-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gadgets', '0003_item_for_user_item_prod_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='xyz', max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quos iusto qui aliquam ea corrupti? Libero quod, magnam illo ut nostrum cumque ex vitae esse eligendi vel ullam consequatur nobis accusamus!', max_length=300),
        ),
    ]