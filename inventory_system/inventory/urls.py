from django.urls import path
from .views import register, login
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # category
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.get_category, name='get_category'),
    path('categories/<int:category_id>/update/', views.update_category, name='update_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    # items
    path('items/', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.get_item, name='get_item'),
    path('items/<int:item_id>/update/', views.update_item, name='update_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('items/list/', views.list_items, name='list_items'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
