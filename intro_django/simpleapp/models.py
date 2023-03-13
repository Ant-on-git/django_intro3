from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(validators=[MinLengthValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products') # все продукты в категории будут доступны через поле products
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')], default=0)  # количество товара на складе

    def __str__(self):
        return f'{self.name}: {self.description[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        # делается для того, чтобы при создании объекта или переходе к его деталями не прописывать в каждом дженерике succes_url.
        return f'/products/{self.pk}'  # Django просто будет перенаправлять вас по ссылке, которая возвращается с get_absolute_url метода модели.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'



