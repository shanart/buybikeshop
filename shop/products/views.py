try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except:
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Product, Wishlist
from .forms import AddToWishlistForm
from cart.forms import CartAddProductForm
from cart.models import Cart
from comments.forms import CommentForm
from comments.models import Comment
from variaty.models import Category, Brand
from accounts.models import Profile

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
    products = Product.objects.all()
    user = request.user
    prod_ids_in_wishlist = []

    cart_product_form = CartAddProductForm()

    init_awlf = {
        "user" : request.user
    }
    addtowishlistform = AddToWishlistForm(initial=init_awlf)
    query = request.GET.get('q')
    if query:
        products = products.filter(
                Q(year__icontains=query) |
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(description__icontains=query) |
                Q(brand__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(subcategory__title__icontains=query)
            )

    if not user.is_anonymous():
        wishlist = Wishlist.objects.filter(user=request.user)
        for item in wishlist:
            prod_ids_in_wishlist.append(item.item.id)


    context = {
        "prod_ids_in_wishlist" : prod_ids_in_wishlist,
        "products" : products,
        "cart_product_form" : cart_product_form,
        "addtowishlistform" : addtowishlistform
    }
    return render(request, "catalog/list.html", context )

def product_detail(request, slug):
    userlist = [] # store all commented users
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    initial_data = {
        "content_type": product.get_content_type,
        "object_id": product.id,
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type          = comment_form.cleaned_data.get("content_type")
        content_type    = ContentType.objects.get(model=c_type)
        obj_id          = comment_form.cleaned_data.get('object_id')
        content_data    = comment_form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data
						)
        messages.success(request, "Comment created")

    comments = product.comments
    for cu in comments:
        user = Profile.objects.get(user=cu.user)
        userlist.append(user)


    commentitems = zip(comments, userlist)
    product = {
        "product": product,
        "commentitems" : commentitems,
        "cart_product_form" : cart_product_form,
        "comment_form": comment_form
    }
    return render(request, "catalog/detail.html", product )

def product_filter_by_category(request, slug):
    category_title = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category__slug=slug)
    cart_product_form = CartAddProductForm()
    product = {
        "products": products,
        "title" : category_title,
        "filter" : True,
        "cart_product_form" : cart_product_form
    }
    return render(request, "catalog/list.html", product )

def product_filter_by_brand(request, slug):
    brand_title = get_object_or_404(Brand, slug=slug)
    products = Product.objects.filter(brand__slug=slug)
    cart_product_form = CartAddProductForm()
    product = {
        "products": products,
        "title" : brand_title,
        "filter" : True,
        "cart_product_form" : cart_product_form
    }
    return render(request, "catalog/list.html", product )

def add_to_wishlist(request, id):
    wishlist = Wishlist.objects.filter(user=request.user)
    if wishlist:
        for wishitem in wishlist:
            if not int(wishitem.item.id) == int(id):
                new_wishitem = Wishlist(item=Product.objects.get(id=id), user=request.user)
                new_wishitem.save()
                messages.success(request, "Add to wishlist")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else: 
        new_wishitem = Wishlist(item=Product.objects.get(id=id), user=request.user)
        new_wishitem.save()        
        messages.success(request, "Add to wishlist")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_from_wishlist(request, id):
    wishlist = Wishlist.objects.filter(user=request.user)
    if wishlist:
        for wishitem in wishlist:
            if int(wishitem.item.id) == int(id):
                wishitem.delete()
                messages.success(request, "Remove to wishlist")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))