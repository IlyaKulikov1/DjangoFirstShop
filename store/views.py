from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Product, Category
from django.views.decorators.http import require_POST
from .forms import CreateProductForm
from django.db.models import Avg


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    # category = product.category
    # print(category)
    context = {
        'product': product,
        'request': request,
    }

    return render(request, 'product_page.html', context)


@require_POST
def product_rate(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    #Получаем объект продукта из базы по переданному product_id или возвращаем ошибку 404, если такого продукта нет.
    score = int(request.POST.get("score"))
    #получение оценки из данных формы (в поле "score") и преобразуем в целое число.
    total_votes = product.rating_votes
    current_avg = product.average_rating * total_votes
    total_votes += 1
    new_avg = (current_avg + score) / total_votes

    product.average_rating = new_avg
    product.rating_votes = total_votes
    product.save()

    return redirect('product_detail', product_id=product.id)

def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_instance = Product(**form.cleaned_data)
            product_instance.save()
            return redirect('create_product')
    else:
        form = CreateProductForm()
    return render(request, 'form.html', {"form": form})

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    # извлекает из БД все объекты модели Product/Category

    category_id = request.GET.get('category')
        #Получает из GET-параметров запроса значение параметра category (если он есть),
    #который может содержать ID категории для фильтрации.
        #GET-параметры — это часть URL-адреса, которая передаёт данные от клиента (браузера) к серверу в виде пар
    # «ключ=значение». Они располагаются после знака вопроса ? в адресной строке и разделяются символом &,
    # если параметров несколько
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    name = request.GET.get('name')
    rating = request.GET.get('rating')

    if category_id:
        products = products.filter(category__id=category_id)
        #Фильтрует queryset товаров по категории с указанным ID

    # Фильтр по максимальной цене, если указана lte — "less than or equal"
    if max_price:
        products = products.filter(price__lte=max_price)

    if min_price:
        products = products.filter(price__gte=min_price)

    if name:
        products = products.filter(name__istartswith=name)

    if rating:
        products = products.filter(average_rating__gte=rating)


    context = {
        'products': products,
        'categories': categories,
        'request': request,
    }
    return render(request, 'main.html', context)
