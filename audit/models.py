from django.db import models

class database(models.Model):
    Date=models.DateTimeField()
    Turbine_Generator=models.IntegerField()
    State_board=models.IntegerField()
    DG=models.IntegerField()
    HSD=models.IntegerField()
    Oral_utility=models.IntegerField()
    FRICK_India=models.IntegerField()
    ORAL_BD_SRP=models.IntegerField()
    LYO=models.IntegerField()
    BD_plant=models.IntegerField()
    Trane_machine=models.IntegerField()
    CSI_02=models.IntegerField()
    Sterile_utility=models.IntegerField()
    STR_A=models.IntegerField()
    LYO_1=models.IntegerField()
    LYO_2=models.IntegerField()
    LYO_3=models.IntegerField()
    STR_C=models.IntegerField()
    AHU_STR_C=models.IntegerField()
    AHU_STR_A=models.IntegerField()
    RO_and_LAB=models.IntegerField()
    LYO_CT_pump_and_sterile_reactor=models.IntegerField()
    Lighting=models.IntegerField()
    Boiler_8_ton=models.IntegerField()
    Fire_hydrand_and_borewell=models.IntegerField()
    Canteen=models.IntegerField()



