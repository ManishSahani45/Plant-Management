from django.db import models

class Boiler_8_tph():
    Date=models.DateField()
    Steam_generated=models.IntegerField()
    Husk_consumed=models.IntegerField()
    Fuel_ratio=models.IntegerField()
    Condensate_recovery=models.IntegerField()
    Hot_water_recovered=models.IntegerField()
    Total_Recovery=models.IntegerField()
    Max_steam_consumption=models.IntegerField()
    Running_hour=models.IntegerField()
    Condensate_water_recovery=models.IntegerField()
    Feed_water_boiler=models.IntegerField()
    


