from django.urls import path
from myshop.views import category_list_view, index, product_list_view, category_product_list_view, vendor_list_view, vendor_detail_view, contact, ajax_contact_form, shop, cart, checkout_view

app_name = "myshop"

urlpatterns = [

    # Homepage
    path('', index, name='index'),
    path("products/", product_list_view, name="product-list"),


    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),

    # Vendors
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name="vendor-detail"),

    # Contact
    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),

    # Shop
    path("shop/", shop, name="shop"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout_view, name="checkout"),

]
