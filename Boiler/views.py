from django.shortcuts import render
from . models import Boiler_8_tph
def boiler_data(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        Steam_generated=request.POST["Steam_generated"]
        Husk_consumed=request.POST["Husk_consumed"]
        Fuel_ratio=request.POST["Fuel_ratio"]
        Condensate_recovery=request.POST["Condensate_recovery"]
        Hot_water_recovered=request.POST["Hot_water_recovered"]
        Total_Recovery= Condensate_recovery +  Hot_water_recovered 
        Max_steam_consumption=request.POST["Max_steam_consumption"]
        Running_hour=request.POST['Running_hour']
        
        Feed_water_boiler=request.POST["Feed_water_boiler"]
        Condensate_water_recovery=Total_Recovery/Feed_water_boiler
        obj7=Boiler_8_tph(Date=Date,Steam_generated=Steam_generated,Husk_consumed=Husk_consumed,Fuel_ratio=Fuel_ratio,
                          Condensate_recovery=Condensate_recovery,Hot_water_recovered=Hot_water_recovered,Total_Recovery=Total_Recovery,
                          Max_steam_consumption=Max_steam_consumption,Running_hour=Running_hour,Condensate_water_recovery=Condensate_water_recovery,
                           Feed_water_boiler=Feed_water_boiler)
        obj7.save()
        return render(request,'boiler.html')
    return render (request,'boiler.html')





