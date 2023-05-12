from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product , Review
from .forms import ProductForm, ReviewForm ,CategoryForm

# Create your views here.
def index_redirect(request):
    return redirect('reviews:index')

def index(request):
    products = Product.objects.order_by('-pk')
    per_page = 5
    paginator = Paginator(products, per_page)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    context = {
        'products': page_obj,
    }
    return render(request,'reviews/index.html', context)

def category(request):
    return render(request, 'reviews/category.html')

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
    if request.user == review.user or request.user.is_superuser:
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