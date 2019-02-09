from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from user.forms import *
# Create your views here.
def home(request):
	context = {
		'css' : 'shop/indexStyles.css',
		'groups' : Category.objects.all(),
	}
	return render(request, 'shop/index.html', context)

@login_required(login_url='/login')
def shop(request, id=0, order='none'):
	if request.user.profile.first_time:
		messages.info(request, 'Please update your profile')
		return redirect('user-profile')

	context = {
		'css' : 'shop/shopStyles.css',
		'category'  : id,
		'order'     : order,
		'groups' : Category.objects.all(),
	}

	#apply category order
	if id == 0:
		items = Item.objects.all()
	else:
		category = Category.objects.get(id = id)
		items = Item.objects.all().filter(category = category)

	#apply orders
	if order == 'price_lo_hi':
		items = items.order_by('price')
	elif order == 'price_hi_lo':
		items = items.order_by('-price')

	items = list(items)

	items.sort(key = lambda x: x.category.id)
	
	context['items'] = []
	curr_id = 0
	for item in items:
		if item.category.id != curr_id:
			#we have to make a new list
			curr_id = item.category.id
			context['items'].append([item])
		else:
			context['items'][-1].append(item)
	return render(request, 'shop/shop.html', context)

@login_required(login_url='/login')
def profile(request):
	context = {
		'css' : 'shop/profileStyles.css',
		'groups' : Category.objects.all(),
		'form'	: ProfileUpdateForm(instance = request.user.profile),
	}

	if request.method=='POST':
		form = ProfileUpdateForm(request.POST, instance = request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request, f'Profile updated for {request.user}')

	return render(request, 'shop/profile.html', context)

@login_required(login_url='/login')
def newItem(request):
	if not request.user.is_staff:
		return redirect("shop-home")
	context = {
		'css' : 'shop/newItemStyles.css',
		'form': ItemCreationForm(),
	}

	if request.method == 'POST':
		form = ItemCreationForm(request.POST)
		if form.is_valid():
			item = form.save()
			messages.success(request, f'New item, {item} succesfully added')

	return render(request, 'shop/newItem.html', context)


def register(request):
	context = {
		'form' : UserRegistrationForm()
	}

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, f'Account for {user.username} has been created')
			return redirect('login')

	return render(request, 'user/register.html', context)


#home is shop-home