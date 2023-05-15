from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product , Review
from .forms import ProductForm, ReviewForm
from .models import Product, Review
from .forms import ProductForm, ReviewForm
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index_redirect(request):
    return redirect('reviews:index')


def index(request):
    ranking_url = 'https://search.musinsa.com/ranking/best?u_cat_cd='
    res = requests.get(ranking_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    products_ranking = []
    for item in soup.select('.li_inner')[:10]:
        product = Product()
        product.product_id = item.select_one('a.img-block')['href'].split('?')[0].split('/')[-1]
        product.brand = item.select('.article_info > p > a')[0].text.strip()
        product.title = item.select('.article_info > p > a')[1].contents[-1].strip()
        product.photo = item.select('.lazyload')[0]['data-original']
        products_ranking.append(product)

    Product.objects.all().delete()

    Product.objects.bulk_create(products_ranking)

    products = Product.objects.order_by('-pk')
    per_page = 5
    paginator = Paginator(products, per_page)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    context = {
        'products': page_obj,
        'products_ranking': products_ranking,
    }
    return render(request,'reviews/index.html', context)


def search(request):
    query = request.GET.get('query')

    search_url = f'https://www.musinsa.com/search/musinsa/integration?q={query}' # 검색어 적용
    res = requests.get(search_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    products_search = []

    for item in soup.select('.li_inner'):
        product = Product()
        product.brand = item.select('.article_info > p > a')[0].text.strip()
        product.title = item.select('.article_info > p > a')[1].contents[-1].strip()
        product.photo = item.select('.lazyload')[0]['data-original']
        product.product_id = item.select_one('[data-bh-content-no]')['data-bh-content-no']
        products_search.append(product)

    Product.objects.all().delete()

    Product.objects.bulk_create(products_search)

    context = {
        'products_search': products_search,
        'query': query,
    }
    return render(request,'reviews/search.html', context)


def category(request, category_type):
    if category_type == 'top':
        category_url = 'https://www.musinsa.com/categories/item/001'
        category_title = '상의'
    elif category_type == 'outerwear':
        category_url = 'https://www.musinsa.com/categories/item/002'
        category_title = '아우터'
    elif category_type == 'bottoms':
        category_url = 'https://www.musinsa.com/categories/item/003'
        category_title = '하의'
    elif category_type == 'shoes':
        category_url = 'https://www.musinsa.com/categories/item/005'
        category_title = '신발'

    res = requests.get(category_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    products_category = []
    for item in soup.select('#goods_list .li_inner')[:20]:
        product = Product()
        product.product_id = item.select_one('a.img-block')['href'].split('?')[0].split('/')[-1]
        product.brand = item.select('.article_info > p > a')[0].text.strip()
        product.title = item.select('.article_info > p > a')[1].contents[-1].strip()
        product.photo = item.select('.lazyload')[0]['data-original']
        products_category.append(product)


    Product.objects.all().delete()

    Product.objects.bulk_create(products_category)

    context = {
        'products_category': products_category,
        'category_title': category_title,
    }
    return render(request, 'reviews/category.html', context)


def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    product_form = ProductForm()
    reviews = product.review_set.all()
    context = {
        'product': product,
        'product_form': product_form,
        'reviews': reviews,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('reviews:detail', product.pk)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


@login_required
def product_delete(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user == Product.user:
        product.delete()
    return redirect('reviews:index')


@login_required
def review_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user :
        review.delete()
    return redirect('reviews:index')


@login_required
def product_update(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user == product.user:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', product.pk)
        else:
            form = ProductForm(instance=product)
    else:
        return redirect('reviews:index')
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


def review_update(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', product_pk)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/update.html', context)


@login_required
def review_create(request, article_pk):
    product = Product.objects.get(pk=article_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.product = product
        review.user = request.user
        review.save()
        return redirect('reviews:detail', product.pk)
    context = {
        'product': product,
        'review_form': review_form,
    }
    return render(request, 'reviews/detail.html', context)