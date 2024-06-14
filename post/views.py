from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import PostIt
from django.contrib.auth.models import User
from .forms import PostItForm
from users.forms import UserUpdateInfoForm, UserImageExtensionForm
from django.contrib import messages

# Create your views here.

@login_required()
def home_page(request):
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'post/home.html',context)
@login_required()
def user_posts(request,user_id):
    posts = PostIt.objects.filter(posted_by=user_id)

    context = {
        'posts': posts,
        'usr': User.objects.filter(id=user_id)[0],
        'number_of_personal_posts': len(posts)
    }

    return render(request, 'post/user_posts.html', context)


@login_required()
def timeline_page(request):

    if request.method == 'POST':
        form = PostItForm(request.POST)
        form.instance.posted_by = request.user

        if form.is_valid():
            form.save()
            return redirect('post-timeline')
    else:
        form = PostItForm()

    number_of_posts = PostIt.objects.filter(posted_by=request.user.id).order_by('-posted_date')

    context = {
        'post_its': number_of_posts,
        'number_of_personal_posts': len(number_of_posts),
        'form': form
    }
    return render(request, 'post/timeline.html', context)
def about_page(request):
    return render(request, 'post/about.html')
@login_required()
def account_page(request):
    if request.method == 'POST':
        user_update_info_form = UserUpdateInfoForm(request.POST, instance=request.user)

        if hasattr(request.user,'userimageextension'):
            user_image_extension_form = UserImageExtensionForm(request.POST, request.FILES, instance=request.user.userimageextension)
        else:
            user_image_extension_form = UserImageExtensionForm(request.POST, request.FILES)
            user_image_extension_form.instance.user = request.user

        if user_update_info_form.is_valid() and user_image_extension_form.is_valid():
            user_update_info_form.save()
            user_image_extension_form.save()
            messages.success(request,'Account Updated')

            return redirect('post-account')
    else:
        user_update_info_form = UserUpdateInfoForm(instance=request.user)

        if hasattr(request.user, 'userimageextension'):
            user_image_extension_form = UserImageExtensionForm(instance=request.user.userimageextension)
        else:
            user_image_extension_form = UserImageExtensionForm()
    context = {
        'user_update_info_form': user_update_info_form,
        'user_image_extension_form': user_image_extension_form
    }
    return render(request,'post/account.html', context)