'''
URLs for the nofie_app app

'''

from django.urls import path
from . import views
from nofie_app.views import *

urlpatterns = [

    path('', views.index, name='index'),

    # Category Urls
    path('category/', views.category, name='category'),

    # Register Urls
    path('register_student/', views.register_student, name='register_student'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),

    # Notes Urls
    path('notes/', views.notes, name='notes'),

    # View Urls
    path('view_notes/', views.view_notes, name='view_notes'),
    path('view_students/', views.view_students, name='view_students'),
    path('view_teachers/', views.view_teachers, name='view_teachers'),

    # Delete Urls
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('delete_teacher/<int:id>/', views.delete_teacher, name='delete_teacher'),
    path('delete_note/<int:id>/', views.delete_notes, name='delete_note'),

    # Update Urls
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('update_teacher/<int:id>/', views.update_teacher, name='update_teacher'),
    path('update_note/<int:id>/', views.update_notes, name='update_note'),
    

]