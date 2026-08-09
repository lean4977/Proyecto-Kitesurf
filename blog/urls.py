from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='lista_posts'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detalle_post'),
    path('nuevo/', views.PostCreateView.as_view(), name='nuevo_post'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='eliminar_post'),
]