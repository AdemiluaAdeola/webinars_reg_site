from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='webinar_list'),
    path('search/', search_view, name='search'),
    path('register/<int:webinar_id>/', register_for_webinar, name='register_for_webinar'),
    path('process_payment/<int:registration_id>/', process_payment, name='process_payment'),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
    path('dashboard/users/', user_list, name='dashboard_user_list'),
    path('dashboard/webinars/', webinar_list, name='dashboard_webinar_list'),
    path('dashboard/webinars/<int:webinar_id>/registrations/', users_registered, name='dashboard_users_registered'),
    path('dashboard/users/<int:user_id>/', user_detail, name='dashboard_user_detail'),
    path('dashboard/users/<int:user_id>/delete/', delete_user, name='dashboard_delete_user'),
    path('dashboard/webinars/create/', create_webinar, name='dashboard_create_webinar'),
    path('dashboard/webinars/<int:webinar_id>/update/', update_webinar, name='dashboard_update_webinar'),
    path('dashboard/webinars/<int:webinar_id>/delete/', delete_webinar, name='dashboard_delete_webinar'),
]
