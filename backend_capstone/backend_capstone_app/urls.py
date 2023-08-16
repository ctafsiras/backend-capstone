from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# router = DefaultRouter()
# router.register(r'menu', MenuView)

# router.register(r'users',UserViewSet)

# urlpatterns = [
# 	path('books/', views.BookView.as_view(listCreate)),
#     path('books/<int:pk>',views.BookView.as_view(deleteUpdate)),
# ]
urlpatterns = [
    # path('',include(router.urls)),
    path('menu-items/',views.MenuView.as_view()),
    path('menu-items/<int:pk>/',views.SingleMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('books/', views.BookingViewSet.as_view()),
]