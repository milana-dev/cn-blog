from django.urls import path
from blogs import views as blog_views

urlpatterns = [
    path('', blog_views.all_blogs, name = 'all_blogs'),
    path('create/', blog_views.create_blog, name = 'create_blog'),
    path('detail/<int:pk>/', blog_views.detail_blog, name = 'detail_blog'),
    path('update/<int:pk>/', blog_views.update_blog, name = 'update_blog'),
    path('delete/<int:pk>/', blog_views.delete_blog, name = 'delete_blog'),
]