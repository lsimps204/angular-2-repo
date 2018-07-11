from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name='recipe_list'),
    path('create', views.RecipeCreateAPIView.as_view(), name='recipe_create'),
    path('<int:pk>', views.RecipeDetailAPIView.as_view(), name='recipe_detail'),
    path('<int:pk>/edit', views.RecipeUpdateAPIView.as_view(), name='recipe_update'),
    path('<int:pk>/delete', views.RecipeDeleteAPIView.as_view(), name='recipe_delete')
]