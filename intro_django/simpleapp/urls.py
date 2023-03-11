from django.urls import path
from .views import ProductsList, ProductDetail, ProductListPaginator  # импортируем наши представления


urlpatterns = [
    # path - означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', ProductsList.as_view()),  # т.к. сам по себе это класс, то нам надо представить этот класс в виде view.
                                       # Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view())  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
                                               # дженерик сам по названию понимает какое поле нужно
                                               # в итоге чтобы получить инф о 1 товаре нужно ввести адрес /products/1
]