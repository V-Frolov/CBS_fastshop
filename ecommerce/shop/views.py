from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from .forms import ReviewForm, OrderCreateForm
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile(request):
    return render(request, 'shop/profile.html')


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews})


@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/add_review.html', {'form': form})


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()  # Зберігаємо продукти у ManyToMany поле
            return redirect('order_success')
    else:
        form = OrderCreateForm()

    return render(request, 'shop/create_order.html', {'form': form,})


def order_success(request):
    return render(request, 'shop/order_success.html')
