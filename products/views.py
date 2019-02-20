from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product


def main(request):
    return render(request, 'products/index.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['product_url'] and request.POST['product_body'] and request.FILES['product_icon'] and request.FILES['product_image']:
            product = Product()
            product.title = request.POST['title']
            if request.POST['product_url'].startswith('http://') or request.POST['product_url'].startswith('https://'):
                product.url = request.POST['product_url']
            else:
                product.url = 'http://' + request.POST['product_url']
            product.body = request.POST['product_body']
            product.icon = request.FILES['product_icon']
            product.image = request.FILES['product_image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
