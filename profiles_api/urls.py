from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


#intancia de router
router = DefaultRouter()
#registrar router
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset') #Nombre base base_name

urlpatterns = [
    #PAra poder carcar la clase usamos .as_view()
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)), #retorna la lista de urls de router
]
