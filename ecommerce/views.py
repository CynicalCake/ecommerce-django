from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_avalible=True).order_by('created_date')

    for product in products:
        review = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': review,
    }

    return render(request, 'home.html', context)
