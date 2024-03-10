from django.shortcuts import render
from . models import database
def results(request):
    if request.method == "POST":
        Date=request.post['Date']
        Turbine_Generator =request.post['Turbine_Generator']
        State_board=request.post['State_board']
        DG=request.post['DG']
        HSD=request.post['HSD']
        Oral_utility=request.post['Oral_utility']
        FRICK_India=request.post['FRICK_India']
        Oral_BD_SRP=request.post['Oral_BD_utility']
        LYO= LYO_1 + LYO_2 + LYO_3
        BD_plant=request.post['BD_plant']
        Trane_machine=request.post['Trane_machine']
        CSI_02=request.post['CSI_02']
        Sterile_utilty=request.post['Sterile_utilty']
        STR_A=request.post['STR_A']
        LYO_1=request.post['LYO_1']
        LYO_2=request.post['LYO_2']
        LYO_3=request.post['LYO_3']
        STR_C=request.post['STR_C']
        AHU_STR_C=request.post['AHU_STR_C']
        AHU_STR_A=request.post['AHU_STR_A']
        RO_and_LAB=request.post['RO_and_LAB']
        LYO_CT_pump_and_sterile_reactor=request.post['LYO_CT_pump_and_sterile_reactor']
        Lighting=request.post['Lighting']
        Boiler_8_ton=request.post['Boiler_8_ton']
        Fire_hydrand_and_borewell=request.post['Fire_hydrand_and_borewellnt']
        Canteen=request.post['Canteen']
        obj3=database(Date=Date,Turbine_Generator=Turbine_Generator , State_board=State_board , DG=DG ,HSD=HSD ,Oral_utility=Oral_utility ,
                     FRICK_India =FRICK_India ,Oral_BD_SRP = Oral_BD_SRP ,LYO=LYO,BD_plant=BD_plant ,
                     Trane_machine=Trane_machine ,CSI_02=CSI_02,Sterile_utilty=Sterile_utilty,STR_A=STR_A,
                     LYO_1=LYO_1,LYO_2=LYO_2,LYO_3=LYO_3,STR_C=STR_C,AHU_STR_C=AHU_STR_C ,AHU_STR_A=AHU_STR_A ,
                     RO_and_LAB=RO_and_LAB ,LYO_CT_pump_and_sterile_reactor=LYO_CT_pump_and_sterile_reactor ,
                     Lighting=Lighting ,Boiler_8_ton=Boiler_8_ton,Fire_hydrand_and_borewell=Fire_hydrand_and_borewell ,
                     Canteen=Canteen )
        obj3.save()
        return render(request,'energy.html')
    return render (request,'energy.html')



