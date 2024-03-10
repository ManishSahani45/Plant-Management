from django.urls import path
from . import views
urlpatterns = [
    path("sterile/",views.Machine_usage_Sterile),
    path("oral/",views.Machine_Usage_Oral),
    path('',views.home_view),
]   