# from api.crud import ALL THINGS I'LL NEED
from datetime import datetime

from django.shortcuts import render, redirect


# from XXX import get_all_products, Product

def index(request):
    # date = datetime.today()

    return render(request, "catalogue/index.html", context={"username": "évaluateur", "date": datetime.today()})
# add , {'products': get_all_products()} and similar
# from the same file (to be created) also import the method the Product class


def product_list(request):
    products = Product.objects.all()
    return render(request,
                  )


def add_product(request):
    name = request.POST.get("name")
    category = request.POST.get("category")
    description = request.POST.get("description")
    price = request.POST.get("price")
    # Pas sûr pour celle-ci !
    image = request.POST.get("image")

    product = Product(name=name, category=category, description=description, price=price, image=image)

    return redirect('index')

# Optionnel
# def delete_product(request):
#     name = request.POST.get("name")
#     product = Product(name="name")
#     Product.delete()
#
#     return redirect('index')
