from django.db import models

# Create your models here.


# without DB

# class Destination:
#     def dest(self, obj):
#         self.id: int = obj['id']
#         self.name: int = obj['name']
#         self.img: int = obj['img']
#         self.price: int = obj['price']
#         self.description: int = obj['description']
#         self.offer: bool = obj['offer']

# with DB
class Destination(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
