from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreateView, ProductUpdateVeiw, ProductDeleteView


urlpatterns = [
    # path - означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', ProductsList.as_view()),  # т.к. сам по себе это класс, то нам надо представить этот класс в виде view.
                                       # Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
                                                # дженерик сам по названию понимает какое поле нужно
                                                # в итоге чтобы получить инф о 1 товаре нужно ввести адрес /products/1
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateVeiw.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]