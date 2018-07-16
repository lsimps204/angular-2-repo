from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

# API data routes
urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name='recipe_list'),
    path('create', views.RecipeCreateAPIView.as_view(), name='recipe_create'),
    path('<int:pk>', views.RecipeDetailAPIView.as_view(), name='recipe_detail'),
    path('<int:pk>/edit', views.RecipeUpdateAPIView.as_view(), name='recipe_update'),
    path('<int:pk>/delete', views.RecipeDeleteAPIView.as_view(), name='recipe_delete'),
]

# JWT/Auth routes
urlpatterns += [
    path('api-token-auth', obtain_jwt_token),
    path('api-token-refresh', refresh_jwt_token),
    path('register', views.RegisterAPIView.as_view(), name='register'),
]