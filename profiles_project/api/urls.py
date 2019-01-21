from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from. import views
from django.urls import path, include
router = DefaultRouter()
router.register('hello-viewset', views.Helloviewset, base_name='hello-viewset')
router.register('profile', views.userprofileViewset)
router.register('login', views.Loginviewset, base_name='login')
router.register('feedback', views.profilefeedbackviewset)
"""we don need to specify a base name coz its already in the models file"""
urlpatterns = [
    url(r'^api/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))

]