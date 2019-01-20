from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from. import views
from django.urls import path, include
router = DefaultRouter()
router.register('hello-viewset', views.Helloviewset, base_name='hello-viewset')
router.register('profile', views.userprofileViewset)
router.register('login', views.Loginviewset, base_name='login')
urlpatterns = [
    url(r'^api/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))

]