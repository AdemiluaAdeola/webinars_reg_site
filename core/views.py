from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
# @login_required(login_url='login')
# def index(response):
#     return render(response, 'core/index.html')

@login_required(login_url='login')
def index(response):
    webinars = Webinar.objects.all()
    return render(response, 'core/webinar_list.html', {'webinars': webinars})

@login_required(login_url='login')
def register_for_webinar(response, webinar_id):
    webinar = Webinar.objects.get(id=webinar_id)
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = response.user
            registration.paid = False
            registration.save()
            return redirect('process_payment', registration.id)
    else:
        form = RegistrationForm()
    return render(response, 'core/register_for_webinar.html', {'form': form, 'webinar': webinar})

@login_required(login_url='login')
def process_payment(response, registration_id):
    registration = Registration.objects.get(id=registration_id)
    if response.method == 'POST':
        token = response.POST.get('stripeToken')
        charge = stripe.Charge.create(
            amount=int(registration.webinar.price * 100),
            currency='usd',
            description=f'Payment for {registration.webinar.title}',
            source=token,
        )
        if charge.status == 'succeeded':
            registration.paid = True
            registration.save()
            send_mail(
                'Webinar Link',
                f'You can join the webinar using the following link: {registration.webinar.link}',
                settings.EMAIL_HOST_USER,
                [registration.user.email],
                fail_silently=False,
            )
            return redirect('webinar_list')
    return render(response, 'core/process_payment.html', {
        'registration': registration,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def staff_dashboard(response):
    return render(response, 'dashboard/dashboard.html')

def user_list(response):
    users = User.objects.all()
    return render(response, 'dashboard/user_list.html', {'users': users})


def webinar_list(response):
    webinars = Webinar.objects.all()
    return render(response, 'dashboard/webinar_list.html', {'webinars': webinars})


def users_registered(response, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    registrations = Registration.objects.filter(webinar=webinar)
    return render(response, 'dashboard/users_registered.html', {
        'webinar': webinar,
        'registrations': registrations,
    })

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'dashboard/user_detail.html', {'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_list')


def create_webinar(request):
    if request.method == 'POST':
        form = WebinarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webinar_list')
    else:
        form = WebinarForm()
    return render(request, 'dashboard/create_webinar.html', {'form': form})


def update_webinar(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    if request.method == 'POST':
        form = WebinarForm(request.POST, instance=webinar)
        if form.is_valid():
            form.save()
            return redirect('webinar_list')
    else:
        form = WebinarForm(instance=webinar)
    return render(request, 'dashboard/create_webinar.html.html', {'form': form})


def delete_webinar(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    webinar.delete()
    return redirect('webinar_list')



def search_view(response):
    
    results = []
    if 'query' in response.GET:
        query = response.POST['query']
            
        results = Webinar.objects.filter(Q(title__icontains=query))
    return render(response, 'core/search.html', {'results': results})

def blog_list(response):
    posts = Blog.objects.all()
    return render(response, 'core/blog.html', {'posts': posts})

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'dashboard/create_blog.html', {'form': form})

def delete_blogpost(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    webinar.delete()
    return redirect('webinar_list')