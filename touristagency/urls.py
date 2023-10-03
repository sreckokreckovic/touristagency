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

from authentication.views import UserRegistration, UserProfileView

from touristagency import settings
from rest_framework.routers import DefaultRouter
import offers.views as offer_view
import reservations.views as reservation_view
import testimonials.views as testimonial_view
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register("destinations",offer_view.OfferViewSet, basename='offer')
router.register("categories",offer_view.CategoryViewSet, basename='category')
router.register("reservations",reservation_view.ReservationViewSet, basename='reservation')
router.register("testimonials",testimonial_view.TestimonialViewSet, basename='testimonial')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('top-destinations/', offer_view.TopOffersView.as_view(), name ='top_destinations'),
    path('register/',UserRegistration.as_view(),name = 'registration'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('destinations/category/<int:category_id>/', offer_view.OfferListByCategory.as_view(), name='destination-list-by-category'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('api/user/profile/', UserProfileView.as_view(), name='user_profile'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
