from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from products.models import Basket, Products
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались ')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html',context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    
    context = { 'form': form }
    return render(request, 'users/login.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data=request.POST, files = request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance = request.user)

    context = {'form': form, 'baskets': Basket.objects.filter(user=request.user)}
    return render(request, 'users/profile.html', context) 


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])