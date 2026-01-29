from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
  path('', views.index_view, name='index'),
  path('save-data/', views.save_data, name='save_data'),
  path('edit-data/', views.edit_data, name='edit_data'),
  path('update-stage/', views.update_stage, name='update_stage'),
  path('update-order/', views.update_order, name='update_order'),
  path('delete/', views.delete, name='delete'),
  path('book/', views.ListBookView.as_view(), name='list-book'),
  path('book/<int:pk>/detail', views.DetailBookView.as_view(), name='detail-book'),
  path('book/create/', views.CreateBookView.as_view(), name='create-book'),
  path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
  path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
  path('login/', LoginView.as_view(), name='login'),
]
