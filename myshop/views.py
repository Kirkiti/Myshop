from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from userauths.models import ContactUs
from django.http import JsonResponse
from django.contrib import messages

from myshop.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address


def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products": products
    }
    return render(request, 'myshop/index.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'myapp/category-list.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products": products
    }
    return render(request, 'myshop/product-list.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        "products": products
    }
    return render(request, 'myshop/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'myshop/category-list.html', context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category": category,
        "products": products,
    }

    return render(request, "myshop/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors": vendors,
    }
    return render(request, "myshop/vendor-list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)

    context = {
        "vendor": vendor,
    }
    return render(request, "myshop/vendor-detail.html", context)


def contact(request):
    return render(request, 'myshop/contact.html')


def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    data = {
        'bool': True,
        'message': "Message Sent Successfully"
    }

    return JsonResponse({"data": data})


def shop(request):
    return render(request, 'myshop/shop.html')


def cart(request):
    return render(request, 'myshop/cart.html')


def checkout_view(request):
    return render(request, 'myshop/checkout.html')

