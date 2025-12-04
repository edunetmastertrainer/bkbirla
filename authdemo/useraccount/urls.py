from django.urls import path,include
from useraccount import views
urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("addprofile/",views.addprofile,name='addprofile'),
]
