from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1'
    )

    prod_code = models.IntegerField(default=100)

    for_user = models.CharField(max_length=300 , default='xyz')

    item_name = models.CharField(max_length=100)

    item_desc = models.CharField(max_length=300 , default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quos iusto qui aliquam ea corrupti? Libero quod, magnam illo ut nostrum cumque ex vitae esse eligendi vel ullam consequatur nobis accusamus!')

    item_price = models.IntegerField()

    item_image = models.CharField(max_length=500 , default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7OD-PXxcJaOcBjEXnay7aD8VNMoiUgfXm3Q&usqp=CAU")


    def __str__(self):
        return self.item_name
