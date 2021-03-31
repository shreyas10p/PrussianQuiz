from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import CreateView
from .forms import UserForm, ProfileForm, UpdateUserForm
from django.contrib.messages.views import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login as d_login
from django.http import JsonResponse
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required
# Create your views here.


def landingPage(request):
    if request.user.is_authenticated():
        return redirect('update')
    return render(request, 'landingPage.html')


class CreateUserView(CreateView):
    template_name = 'signup.html'
    form_class = UserForm
    success_url = 'landingPage'

    def form_valid(self, form, **kwargs):
        try:
            user = User.objects.get(email=form.instance.email)
        except:
            user = None
        if user is None:
            form.instance.is_active = True
            user = form.save()
           
            messages.success(
                self.request, "Sign up success")
            return redirect('landingPage')
            # return HttpResponseRedirect(reverse('signup'))
        else:
            form_class = UserForm()
            messages.error(self.request, "Sign up error")

            return self.render_to_response(self.get_context_data(form=form_class))
        return redirect('signup')


@api_view(['POST'])
def login(request, **kwargs):
    try:
        content = request.data
    except:
        return JsonResponse({'status': 'failure', 'message': 'Pass Valid  Data'}, status=400)
    username = content['username']
    password = content['password']
    try:
        user = authenticate(username=username, password=password)
    except:
        return JsonResponse({'status': 'failure', 'message': 'Invalid email or password. Try again.'}, status=401)

    if user is not None:
        if user.is_active:
            d_login(request, user)
            nexte = request.POST.get('next', settings.LOGIN_REDIRECT_URL)
            return JsonResponse({'status': 'success', 'next': nexte})
    
    return JsonResponse({'status': 'failure', 'message': 'User not Found'}, status=401)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            user = User.objects.get(username=request.user)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.username = request.POST.get('username')
            user.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })