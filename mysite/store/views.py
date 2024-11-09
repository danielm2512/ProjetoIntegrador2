"""shortcuts"""
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Profile, Material
from .forms import MaterialForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CartItem
from django.shortcuts import render


from django.contrib.auth.forms import AuthenticationForm

def home(request):
    """View for the home page displaying all products."""
    products = Product.objects.all()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cart')
            else:
                login_form.add_error(None, "Invalid username or password")

    return render(request, 'store/home.html', {'products': products, 'login_form': login_form})


def product_detail(request):
    """View for displaying product detail page."""
    return render(request, 'store/product_detail.html', {})

@login_required
def cart(request):
    """View for the shopping cart."""
    # Implementar a lógica do carrinho de compras
    return render(request, 'store/cart.html')

def cart_view(request):
    cart_items = CartItem.objects.all()  # Obtenha os itens do carrinho do usuário atual
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)



def is_inventory_admin(user):
    """Check if the user is an inventory admin."""
    return user.is_inventory_admin

@login_required
@user_passes_test(is_inventory_admin)
def manage_stock(request):
    """View for managing stock, accessible only to inventory admins."""
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_stock')
    else:
        form = MaterialForm()
    materials = Material.objects.all()
    return render(request, 'store/manage_stock.html', {'materials': materials, 'form': form})

@login_required
def filter_products(request):
    """View for filtering products based on the user's profile."""
    profile = get_object_or_404(Profile, user=request.user)
    products = Product.objects.all()

    # Filtrar produtos com base no perfil do usuário
    if profile.gender:
        products = products.filter(description__icontains=profile.gender)
    if profile.age:
        products = products.filter(description__icontains=str(profile.age))
    if profile.interests:
        for interest in profile.interests.split(','):
            products = products.filter(description__icontains=interest.strip())

    return render(request, 'store/home.html', {'products': products})
