from .models import Product

# для дженериков:
from django.views.generic import ListView, DetailView
    # ListView - класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
    # DetailView - класс получения деталей объекта
    # DetailView отличается от ListView тем, что возвращает какой-то конкретный объект, а не список всех объектов из БД
    # Для отображения продукта будет ссылка вида products/<product.pk>

# для пагинатора (ProductListPaginator):
from django.shortcuts import render
from django.views import View               # импортируем простую вьюшку
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Product
from .filters import ProductFilter


######################## вьюшки дженериками: ########################
class ProductsList(ListView):
    model = Product     # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'     # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции
                                        # о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'    # # это имя списка, в котором будут лежать все объекты, его надо указать,
                                        # чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-price']
    # Здесь, чтобы добавить пагинацию, нам надо добавить всего одно поле — paginate_by
    paginate_by = 2     # Это ограничивает количество объектов на странице и добавляет paginator и page_obj к context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        # настраиваем правильную работу пагинатора после фильтрации.
        request_copy = self.request.GET.copy()  # делаем копию get запроса ()
        # дальше нам нужно получить строку запроса (чистую, без указания страницы)
        # request_copy.pop('page', True) -  если в запросе есть page, то его вырезаем(pop). если нет, то возвратится True и перейдет к правой части and
        # благодаря чему в parametrs всегда записывается результат request_copy.urlencode()
        # request_copy.urlencode()  - преобразовываем объект get запроса в строку, содержащую запрос из фильтра (если запроса нет, то пусто)
        parametrs = request_copy.pop('page', True) and request_copy.urlencode()
        context['parametrs'] = parametrs

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'




######################## заменили вьюшки дженериками на постраниичный вывод пагинатором ########################
# В отличие от дженериков, которые мы уже знаем, код здесь надо писать самому, переопределяя типы запросов (например, get- или post-)
# при таком способе в html не передается пагинатор, либо передается не так, как в случае с дженериками  у меня его использовать не получлось
# в документациии такого способа нет, вместо него описан способ через функции (https://docs.djangoproject.com/en/4.1/topics/pagination/)
# НЕ СПОЛЬЗУЕТСЯ
class ProductListPaginator(View):
    def get(self, request):
        products = Product.objects.order_by('-price')
        paginator = Paginator(products, 4)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
        page_number = request.GET.get('page', 1)  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        productsInPage = paginator.get_page(page_number)  # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'products': productsInPage,
        }
        return render(request, 'products.html', data)


