from django.urls import path
from . import views
urlpatterns = [
    path("",views.water_home),
    path("raw/",views.Raw_Water_Consumption),
    path("soft/",views.Soft_water_consumption),
    path("DM/",views.DM_water_consumption),
    path("WFI/",views.WFI_consumption),

]
