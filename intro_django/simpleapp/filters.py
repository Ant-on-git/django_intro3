from django_filters import FilterSet
from .models import Product


# создаем фильтр
class ProductFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Product
        # fields = ('name', 'price', 'quantity', 'category') # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
        # в такой редакции нужно вводить точные значения. изменим чтобы для некоторых полей был диапазон. для этого
        # нужно поменять список fields на словарь, в который прописываются критерии фильтрации.
        fields = {
            'name': ['icontains'],  # часть названия товара
            'quantity': ['gt'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'price': ['lt']  # цена должна быть меньше или равна тому, что указал пользователь
        }


