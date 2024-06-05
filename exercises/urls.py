
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('list-users/', views.list_users, name='list_users'),
    path('person/<uuid:person_id>/routines/', views.person_routines, name='person_routines'),
    path('routine/<uuid:routine_id>/', views.routine_detail, name='routine_detail'),
    path('routine_today/<uuid:person_id>/', views.routine_today, name='routine_today'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)