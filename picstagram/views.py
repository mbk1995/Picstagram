from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db import IntegrityError
from .forms import picturesForm, UserForm, CaptchaTestForm
from .models import pictures
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

IMAGE_FILE_TYPES = ['png', 'jpg', 'gif']


# function to upload pictures.
def create_pictures(request):
	if not request.user.is_authenticated():
		return render(request, 'picstagram/index.html')
	else:
		form = picturesForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		pictures = form.save(commit=False)
		pictures.user = request.user
		pictures.images = request.FILES['images']
		file_type = pictures.images.url.split('.')[-1]
		file_type = file_type.lower()
		if file_type not in IMAGE_FILE_TYPES:
			context = {
				'pictures': pictures,
				'form': form,
				'error_message': 'Image file must be PNG, JPG, or gif',
			}
			return render(request, 'picstagram/create_pictures.html', context)
		
		pictures.save()
		return render(request, 'picstagram/index.html', {'pictures': pictures})
	context = {
		"form": form,
	}
	return render(request, 'picstagram/create_pictures.html', context)


#fuction for displaying 10 images 
def index(request):
	if request.user.is_authenticated():
		picture_list = pictures.objects.filter(user=request.user).order_by('-date')
	else:
		picture_list = pictures.objects.order_by('-date')
	paginator =  Paginator(picture_list, 10)
	page =request.GET.get('page')
	try:
		picture_page = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		picture_page= paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		picture_page = paginator.page(paginator.num_pages)
	return render(request, 'picstagram/index.html', {'picture_page': picture_page})

#delete images
def delete_pictures(request, pictures_id):
	pic = pictures.objects.get(pk=pictures_id)
	pic.delete()
	pics= pictures.objects.filter(user=request.user)
	return render(request, 'picstagram/index.html', {'pics': pics})

# editing caption, updates the image with new caption
def edit(request):
	pid = request.GET.get('id')
	newcaption = request.GET.get('caption')
	p=pictures.objects.filter(id=pid).update(caption=newcaption)
	return render(request, 'picstagram/index.html', {'p': p})
	
# logs the user out and redirects to the login page
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'picstagram/login.html', context)

# Logs user in. if user is authenticated then directs to his page. else stays at login page.
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		form = CaptchaTestForm(request.POST)
		if user is not None:
			if user.is_active:
				login(request, user)
				pics = pictures.objects.filter(user=request.user)
				return render(request, 'picstagram/index.html', {'pics': pics})
			else:
				return render(request, 'picstagram/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'picstagram/login.html', {'error_message': 'Invalid login'})
	return render(request, 'picstagram/login.html')
	
# if the visitor wants to register toupload pictures and edit them
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                pics = pictures.objects.filter(user=request.user)
                return render(request, 'picstagram/index.html', {'pics': pics})
    context = {
        "form": form,
    }
    return render(request, 'picstagram/register.html', context)
