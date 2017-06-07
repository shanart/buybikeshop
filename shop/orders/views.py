from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product
from .forms import OrderCreateForm
from cart.models import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST )
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = request.user
            order.save()
            # order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            return render(request,'orders/order/created.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form': form})

@login_required
def order_detail(request, id):
    list = [] # store all items
    order = get_object_or_404(Order, id=id)
    orderitems = OrderItem.objects.filter(order=order)
    for item in orderitems:
        product = Product.objects.get(title=item.product)
        list.append(product)


    orderdetailitems = zip(list, orderitems)
    context = {
        "order": order,
        "orderdetailitems": orderdetailitems
    }
    return render(request, "orders/order/detail.html", context)
