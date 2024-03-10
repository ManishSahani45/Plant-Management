from django.db import models

class Raw_water():
    Date=models.DateField()
    Raw_Water_in_SRP=models.IntegerField()
    Raw_Water_in_ORAL_A_Washrooms=models.IntegerField()
    Raw_Water_in_Overhead_tank_Sterile=models.IntegerField()
    Raw_Water_in_Canteen=models.IntegerField()
    Raw_Water_for_Soft_Water_Gen=models.IntegerField()
    Raw_Water_for_DG_CT_Fire_hydrant=models.IntegerField()
    Raw_Water_for_RO_plant=models.IntegerField()
    Raw_Water_for_park=models.IntegerField()
    Raw_Water_in_ADm_and_Lab_toilet=models.IntegerField()
    Total_Raw_water=models.IntegerField()

class Soft_Water():
    Date=models.DateField()
    Soft_water_for_Oral_utility_Cooling_tower=models.IntegerField()
    Soft_water_for_Oral_SRP_Cooling_tower_near_utility=models.IntegerField()
    Soft_water_for_Sterile_utility_Cooling_tower=models.IntegerField()
    Soft_water_for_sterile_SRP_Cooling_tower_near_utility=models.IntegerField()
    Soft_water_for_boiler_8_ton=models.IntegerField()
    Soft_water_for_LYO_Cooling_tower=models.IntegerField()
    Soft_water_for_Oral_SRP_Cooling_tower_near_ETP=models.IntegerField()
    Soft_water_for_old_boiler=models.IntegerField()
    Soft_water_for_Frick_MC_cooling_tower_oral_utility=models.IntegerField()
    Soft_water_for_new_Cooling_tower_oral_utility=models.IntegerField()
    Soft_water_for_others=models.IntegerField()
    Total_soft_water_consumption=models.IntegerField()
class DM_water():
    Date=models.DateField()
    DM_water_in_sterile=models.IntegerField()
    DM_water_in_ORAL_A=models.IntegerField()
    DM_water_in_Boiler=models.IntegerField()
    Total_DM_water_consumption=models.IntegerField()
class WFI():
    Date=models.DateField()
    WFI_generation=models.IntegerField()
    WFI_for_pure_steam=models.IntegerField()
    WFI_in_STR_C=models.IntegerField()
    Total_RO_plant_wastage=models.IntegerField()

