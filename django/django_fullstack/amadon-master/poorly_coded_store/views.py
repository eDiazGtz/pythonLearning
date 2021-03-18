from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if(request.method == "POST"):
        quantity_from_form = int(request.POST["quantity"])

        productId = request.POST["productId"]
        product = Product.object.get(id=productId)
        price = float(product.price)
        

        total_charge = quantity_from_form * price
        print("Charging credit card...")
        newProduct = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        id = newProduct.id
        return redirect(f"checkout/{id}")
    return redirect("/")

def checkoutPage(request, orderId):
    recentOrder = Order.objects.get(id=orderId)
    context = {
        "order":recentOrder
    }
    return render(request, "store/checkout.html", context)