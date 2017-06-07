from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, UpdateProfile, ProfileForm
from orders.models import Order, OrderItem
from products.models import Product, Wishlist
from products.forms import AddToWishlistForm
from accounts.models import Profile

def login_view(request):
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "accessform.html", {"form":form, "title": title})



"""

"""
def register_view(request):
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "accessform.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def user_panel(request):
    user = request.user
    userFields = Profile.objects.get(user=user)
    orders = Order.objects.filter(user_id__username=user)
    wishlist = Wishlist.objects.filter(user=user)
    wishlist_products = []
    for item in wishlist:
        p = Product.objects.get(title=item.item)
        wishlist_products.append(p)
    wishlistarray = zip(wishlist, wishlist_products)
    init_awlf = {
        "user" : request.user
    }
    addtowishlistform = AddToWishlistForm(initial=init_awlf)
    context = {
        'user'  : user,
        'orders': orders,
        'userfileds': userFields,
        'wishlistarray': wishlistarray,
        "addtowishlistform" : addtowishlistform,
    }
    return render(request, "account/dashboard.html", context)

@login_required
def update(request):
    user = request.user
    extend_fields = Profile.objects.get(user=user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None,  instance=extend_fields)
    form = UpdateProfile(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid() and profile_form.is_valid():
        instance = form.save(commit=False)
        pinstance = profile_form.save(commit=False)
        pinstance.save()
        instance.save()
        messages.success(request, "Successfully update profile")
        return redirect("/user/dashboard/")

    context = {
        'user': user,
        'form': form,
        'profile_form': profile_form
    }
    return render(request, "account/personal-info.html", context)



"""
TODO:
- delete account view
- paste personal info ( if has ) in checkout form
- add destination location ( may by add GoogleMap service to calculate shipping )

"""
