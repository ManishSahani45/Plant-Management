from django.shortcuts import render
from . models import Raw_water,Soft_Water,DM_water,WFI
def Raw_Water_Consumption(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        Raw_Water_in_SRP=request.POST["Raw_Water_in_SRP"]
        Raw_Water_in_ORAL_A_Washrooms=request.POST["Raw_Water_in_ORAL_A_Washrooms"]
        Raw_Water_in_Overhead_tank_Sterile=request.POST["Raw_Water_in_Overhead_tank_Sterile"]
        Raw_Water_in_Canteen=request.POST["Raw_Water_in_Canteen"]
        Raw_Water_for_Soft_Water_Gen=request.POST["Raw_Water_for_Soft_Water_Gen"]
        Raw_Water_for_DG_CT_Fire_hydrant=request.POST["Raw_Water_for_DG_CT_Fire_hydrant"]
        Raw_Water_for_RO_plant=request.POST["Raw_Water_for_RO_plant"]
        Raw_Water_for_park=request.POST["Raw_Water_for_park"]
        Raw_Water_in_ADm_and_Lab_toilet=request.POST["Raw_Water_in_ADm_and_Lab_toilet"]
        Total_Raw_water=request.POST["Total_Raw_water"]
        obj4=Raw_water(Date=Date,Raw_Water_in_SRP=Raw_Water_in_SRP,Raw_Water_in_ORAL_A_Washrooms=Raw_Water_in_ORAL_A_Washrooms,Raw_Water_in_Overhead_tank_Sterile=Raw_Water_in_Overhead_tank_Sterile,
                       Raw_Water_in_Canteen=Raw_Water_in_Canteen,Raw_Water_for_Soft_Water_Gen=Raw_Water_for_Soft_Water_Gen,Raw_Water_for_DG_CT_Fire_hydrant=Raw_Water_for_DG_CT_Fire_hydrant,Raw_Water_for_RO_plant=Raw_Water_for_RO_plant
                       ,Raw_Water_for_park=Raw_Water_for_park,Raw_Water_in_ADm_and_Lab_toilet=Raw_Water_in_ADm_and_Lab_toilet,Total_Raw_water=Total_Raw_water)
        obj4.save()
        return render(request,'raw_water.html')
    return render (request,'raw_water.html')
def Soft_water_consumption(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        Soft_water_for_Oral_utility_Cooling_tower=request.POST["Soft_water_for_Oral_utility_Cooling_tower"]
        Soft_water_for_Oral_SRP_Cooling_tower_near_utility=request.POST["Soft_water_for_Oral_SRP_Cooling_tower_near_utility"]
        Soft_water_for_Sterile_utility_Cooling_tower=request.POST["Soft_water_for_Sterile_utility_Cooling_tower"]
        Soft_water_for_sterile_SRP_Cooling_tower_near_utility=request.POST["Soft_water_for_sterile_SRP_Cooling_tower_near_utility"]
        Soft_water_for_boiler_8_ton=request.POST["Soft_water_for_boiler_8_ton"]
        Soft_water_for_LYO_Cooling_tower=request.POST["Soft_water_for_LYO_Cooling_tower"]
        Soft_water_for_Oral_SRP_Cooling_tower_near_ETP=request.POST["Soft_water_for_Oral_SRP_Cooling_tower_near_ETP"]
        Soft_water_for_old_boiler=request.POST["Soft_water_for_old_boiler"]
        Soft_water_for_Frick_MC_cooling_tower_oral_utility=request.POST["Soft_water_for_Frick_MC_cooling_tower_oral_utility"]
        Soft_water_for_new_Cooling_tower_oral_utility=request.POST["Soft_water_for_new_Cooling_tower_oral_utility"]
        Soft_water_for_others=request.POST["Soft_water_for_others"]
        Total_soft_water_consumption=request.POST["Total_soft_water_consumption"]
        obj5=Soft_Water(Date=Date,Soft_water_for_Oral_utility_Cooling_tower=Soft_water_for_Oral_utility_Cooling_tower,Soft_water_for_Oral_SRP_Cooling_tower_near_utility=Soft_water_for_Oral_SRP_Cooling_tower_near_utility,
                        Soft_water_for_sterile_SRP_Cooling_tower_near_utility=Soft_water_for_sterile_SRP_Cooling_tower_near_utility,Soft_water_for_boiler_8_ton=Soft_water_for_boiler_8_ton,Soft_water_for_LYO_Cooling_tower=Soft_water_for_LYO_Cooling_tower,
                        Soft_water_for_Oral_SRP_Cooling_tower_near_ETP=Soft_water_for_Oral_SRP_Cooling_tower_near_ETP,Soft_water_for_old_boiler=Soft_water_for_old_boiler,Soft_water_for_Frick_MC_cooling_tower_oral_utility=Soft_water_for_Frick_MC_cooling_tower_oral_utility,Soft_water_for_new_Cooling_tower_oral_utility=Soft_water_for_new_Cooling_tower_oral_utility,
                        Soft_water_for_others=Soft_water_for_others,Total_soft_water_consumption=Total_soft_water_consumption)
        obj5.save()
        return render(request,'soft_water.html')
    return render (request,'soft_water.html')
def DM_water_consumption(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        DM_water_in_sterile=request.POST["DM_water_in_sterile"]
        DM_water_in_ORAL_A=request.POST["DM_water_in_ORAL_A"]
        DM_water_in_Boiler=request.POST["DM_water_in_Boiler"]
        Total_DM_water_consumption=(DM_water_in_sterile + DM_water_in_ORAL_A + DM_water_in_Boiler)
        obj6=DM_water(Date=Date,DM_water_in_sterile=DM_water_in_sterile,DM_water_in_ORAL_A=DM_water_in_ORAL_A,DM_water_in_Boiler=DM_water_in_Boiler,
                      Total_DM_water_consumption=Total_DM_water_consumption )
        obj6.save()
        return render(request,'DM.html')
    return render (request,'DM.html')
def WFI_consumption(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        WFI_generation=request.POST["WFI_generation"]
        WFI_for_pure_steam=request.POST["WFI_for_pure_steam"]
        WFI_in_STR_C=request.POST["WFI_in_STR_C"]
        Total_RO_plant_wastage=request.POST["Total_RO_plant_wastage"]
        obj7=WFI(Date=Date,WFI_generation=WFI_generation,WFI_for_pure_steam=WFI_for_pure_steam,WFI_in_STR_C=WFI_in_STR_C,
                 Total_RO_plant_wastage=Total_RO_plant_wastage)
        obj7.save()
        return render(request,'WFI.html')
    return render (request,'WFI.html')
def water_home(request):
    return render(request,'water_system.html')













