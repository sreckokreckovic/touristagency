"""
URL configuration for touristagency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.settings import api_settings
from authentication.views import UserRegistration, UserLogin,UserLogout

from touristagency import settings
from rest_framework.routers import DefaultRouter
import offers.views as offer_view
import reservations.views as reservation_view
import testimonials.views as testimonial_view



router = DefaultRouter()
router.register("offers",offer_view.OfferViewSet, basename='offer')
router.register("categories",offer_view.CategoryViewSet, basename='category')
router.register("reservations",reservation_view.ReservationViewSet, basename='reservation')
router.register("testimonials",testimonial_view.TestimonialViewSet, basename='testimonial')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('top-offers/', offer_view.TopOffersView.as_view(), name ='top_offers'),
    path('register/',UserRegistration.as_view(),name = 'registration'),
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/', UserLogout.as_view(),name = 'logout')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
