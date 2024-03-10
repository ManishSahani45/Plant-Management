from django.shortcuts import render
from . models import Machine_Usage_Sterile_Utility,Machine_usage_Oral_Utility
def Machine_usage_Sterile(request):
    if request.method =='POST': 
        Date=request.POST["Date"]
        Air_Compressor_01=request.POST['Air_Compressor_01']
        Air_Compressor_02=request.POST['Air_Compressor_02']
        Trane_chilled_water_compressor_01=request.POST['Trane_chilled_water_compressor_01']
        Trane_chilled_water_compressor_02=request.POST['Trane_chilled_water_compressor_02']
        Chilled_Water_pump_01=request.POST['Chilled_Water_pump_01']
        Chilled_Water_pump_02=request.POST['Chilled_Water_pump_02']
        Chilled_Water_pump_01=request.POST['Chilled_Water_pump_01']
        Brine_sec_pump_01=request.POST['Brine_sec_pump_01']
        Brine_sec_pump_02=request.POST['Brine_sec_pump_02']
        C_T_Water_Utility_pump_01=request.POST['C_T_Water_Utility_pump_01']
        C_T_Water_Utility_pump_02=request.POST['C_T_Water_Utility_pump_02']
        C_T_Water_Utility_pump_03=request.POST['C_T_Water_Utility_pump_03']
        C_T_W_Fan_Utility_01=request.POST['C_T_W_Fan_Utility_01']
        C_T_W_Fan_Utility_02=request.POST['C_T_W_Fan_Utility_02']
        CSI_Brine_Machine_01=request.POST['CSI_Brine_Machine_01']
        CSI_Brine_Machine_02=request.POST['CSI_Brine_Machine_02']
        CSI_Brine_Primary_Pump_01=request.POST['CSI_Brine_Primary_Pump_01']
        CSI_Brine_Primary_Pump_02=request.POST['CSI_Brine_Primary_Pump_02']
        CSI_Brine_Primary_Pump_03=request.POST['CSI_Brine_Primary_Pump_03']
        LYO_CT_water_pump_01=request.POST['LYO_CT_water_pump_01']
        LYO_CT_water_pump_02=request.POST['LYO_CT_water_pump_02']
        LYO_CT_water_pump_03=request.POST['LYO_CT_water_pump_03']
        LYO_CT_fan=request.POST['LYO_CT_fan']
        CSI_Brine_Machine_03=request.POST['CSI_Brine_Machine_03']
        obj1=Machine_Usage_Sterile_Utility(Date=Date,Air_Compressor_01=Air_Compressor_01,Air_Compressor_02=Air_Compressor_02,
                                           Trane_chilled_water_compressor_01=Trane_chilled_water_compressor_01,Trane_chilled_water_compressor_02=Trane_chilled_water_compressor_02,
                                           Chilled_Water_pump_01= Chilled_Water_pump_01,Chilled_Water_pump_02=Chilled_Water_pump_02,Brine_sec_pump_01=Brine_sec_pump_01,
                                           Brine_sec_pump_02=Brine_sec_pump_02,C_T_Water_Utility_pump_01=C_T_Water_Utility_pump_01,C_T_Water_Utility_pump_02=C_T_Water_Utility_pump_02,
                                           C_T_Water_Utility_pump_03=C_T_Water_Utility_pump_03,C_T_W_Fan_Utility_01=C_T_W_Fan_Utility_01,C_T_W_Fan_Utility_02=C_T_W_Fan_Utility_02,CSI_Brine_Machine_01=CSI_Brine_Machine_01,CSI_Brine_Machine_02=CSI_Brine_Machine_02,CSI_Brine_Machine_03=CSI_Brine_Machine_03,
                                           CSI_Brine_Primary_Pump_01=CSI_Brine_Primary_Pump_01,CSI_Brine_Primary_Pump_02=CSI_Brine_Primary_Pump_02,CSI_Brine_Primary_Pump_03=CSI_Brine_Primary_Pump_03,LYO_CT_water_pump_01=LYO_CT_water_pump_01,LYO_CT_water_pump_02=LYO_CT_water_pump_02,
                                           LYO_CT_water_pump_03=LYO_CT_water_pump_03,LYO_CT_fan=LYO_CT_fan)
        obj1.save()
        return render(request,'machine_01.html')
    return render (request,'machine_01.html')

def Machine_Usage_Oral(request):
    if request.method =="POST":
        Date=request.POST["Date"]
        Brine_Unit_Howden_01=request.POST['Brine_Unit_Howden_01']
        Brine_Unit_Howden_02=request.POST['Brine_Unit_Howden_02']
        Chilled_water_howden_unit_01=request.POST['Chilled_water_howden_unit_01']
        Chilled_water_CSI_unit_02=request.POST['Chilled_water_CSI_unit_02']
        Air_Compressor_01=request.POST['Air_Compressor_01']
        Air_Compressor_02=request.POST['Air_Compressor_02']        
        Air_Compressor_03=request.POST['Air_Compressor_03']
        Brine_PRM_pump_01=request.POST['Brine_PRM_pump_01']
        Brine_PRM_pump_02=request.POST['Brine_PRM_pump_02']
        Brine_PRM_pump_03=request.POST['Brine_PRM_pump_03']
        Brine_SEC_pump_01=request.POST['Brine_SEC_pump_01']
        Brine_SEC_pump_02=request.POST['Brine_SEC_pump_02']
        Brine_SEC_pump_03=request.POST['Brine_SEC_pump_03']
        CHW_PRM_Pump_01=request.POST['CHW_PRM_Pump_01']
        CHW_PRM_Pump_02=request.POST['CHW_PRM_Pump_02']
        CHW_PRM_Pump_03=request.POST['CHW_PRM_Pump_03']
        AWAM_02_feed_pump_01=request.POST['AWAM_02_feed_pump_01']
        AWAM_02_feed_pump_02=request.POST['AWAM_02_feed_pump_02']
        CHW_SEC_pump_03=request.POST['CHW_SEC_pump_03']
        CHW_SEC_pump_04=request.POST['CHW_SEC_pump_04']
        CHW_SEC_pump_05=request.POST['CHW_SEC_pump_05']
        CT_Water_utility_pump_01=request.POST['CT_Water_utility_pump_01']
        CT_Water_utility_pump_02=request.POST['CT_Water_utility_pump_02']
        CT_Water_utility_pump_03=request.POST['CT_Water_utility_pump_03']
        SRP_CT_water_pump_01=request.POST['SRP_CT_water_pump_01']
        SRP_CT_water_pump_02=request.POST['SRP_CT_water_pump_02']
        CTW_Fan_utility_01=request.POST['CTW_Fan_utility_01']
        SRP_CT_fan_02=request.POST['SRP_CT_fan_02']
        Screw_compressor_low_stage=request.POST['Screw_compressor_low_stage']
        Vilter_compressor_High_stage=request.POST['Vilter_compressor_High_stage']
        MEOH_PRM_pump_01=request.POST['MEOH_PRM_pump_01']
        MEOH_PRM_pump_02=request.POST['MEOH_PRM_pump_02']
        MEOH_SEC_pump_01=request.POST['MEOH_SEC_pump_01']
        MEOH_SEC_pump_02=request.POST['MEOH_SEC_pump_02']
        MEOH_CT_Water_pump_01=request.POST['MEOH_CT_Water_pump_01']
        MEOH_CT_Water_pump_02=request.POST['MEOH_CT_Water_pump_02']
        MEOH_CT_fan_01=request.POST['MEOH_CT_fan_01']
        MEOH_CT_fan_02=request.POST['MEOH_CT_fan_01']
        AVAM_soln_pump_01=request.POST['AVAM_soln_pump_01']
        AVAM_soln_pump_02=request.POST['AVAM_soln_pump_02']
        CHW_SEC_pump_06=request.POST['CHW_SEC_pump_06']
        CT_new_pump_01=request.POST['CT_new_pump_01']
        CT_new_pump_02=request.POST['CT_new_pump_02']
        CT_new_pump_03=request.POST['CT_new_pump_03']
        CT_new_fan_01=request.POST['CT_new_fan_01']
        CT_new_fan_02=request.POST['CT_new_fan_02']
        obj2=Machine_usage_Oral_Utility(Date=Date,Brine_Unit_Howden_01=Brine_Unit_Howden_01,Brine_Unit_Howden_02=Brine_Unit_Howden_02,
                                        Chilled_water_howden_unit_01=Chilled_water_howden_unit_01,Chilled_water_CSI_unit_02=Chilled_water_CSI_unit_02,Air_Compressor_01=Air_Compressor_01,
                                        Air_Compressor_02=Air_Compressor_02,Air_Compressor_03=Air_Compressor_03,Brine_PRM_pump_01=Brine_PRM_pump_01,
                                        Brine_PRM_pump_02=Brine_PRM_pump_02,Brine_PRM_pump_03=Brine_PRM_pump_03,Brine_SEC_pump_01=Brine_SEC_pump_01,
                                        Brine_SEC_pump_02=Brine_SEC_pump_02 ,Brine_SEC_pump_03=Brine_SEC_pump_03,CHW_PRM_Pump_01=CHW_PRM_Pump_01,CHW_PRM_Pump_02=CHW_PRM_Pump_02,
                                        CHW_PRM_Pump_03=CHW_PRM_Pump_03,AWAM_02_feed_pump_01=AWAM_02_feed_pump_01,AWAM_02_feed_pump_02=AWAM_02_feed_pump_02,CHW_SEC_pump_03=CHW_SEC_pump_03,
                                        CHW_SEC_pump_04=CHW_SEC_pump_04,CHW_SEC_pump_05=CHW_SEC_pump_05,CT_Water_utility_pump_01=CT_Water_utility_pump_01,CT_Water_utility_pump_02=CT_Water_utility_pump_02,
                                        CT_Water_utility_pump_03=CT_Water_utility_pump_03,SRP_CT_water_pump_01=SRP_CT_water_pump_01,SRP_CT_water_pump_02=SRP_CT_water_pump_02,
                                        CTW_Fan_utility_01=CTW_Fan_utility_01,SRP_CT_fan_02=SRP_CT_fan_02,Screw_compressor_low_stage=Screw_compressor_low_stage,Vilter_compressor_High_stage=Vilter_compressor_High_stage,
                                        MEOH_PRM_pump_01=MEOH_PRM_pump_01,MEOH_PRM_pump_02=MEOH_PRM_pump_02,MEOH_SEC_pump_01=MEOH_SEC_pump_01,MEOH_SEC_pump_02=MEOH_SEC_pump_02,
                                        MEOH_CT_Water_pump_01=MEOH_CT_Water_pump_01,MEOH_CT_Water_pump_02=MEOH_CT_Water_pump_02,MEOH_CT_fan_01=MEOH_CT_fan_01,
                                        MEOH_CT_fan_02=MEOH_CT_fan_02,AVAM_soln_pump_01=AVAM_soln_pump_01,AVAM_soln_pump_02=AVAM_soln_pump_02,CHW_SEC_pump_06=CHW_SEC_pump_06,CT_new_pump_01=CT_new_pump_01,
                                        CT_new_pump_02=CT_new_pump_02,CT_new_pump_03=CT_new_pump_03,CT_new_fan_01=CT_new_fan_01,CT_new_fan_02=CT_new_fan_02,
                                        )
        obj2.save()
        return render(request,'Oral_utility.html')
    return render(request,'Oral_utility.html')
def home_view(request):
    return render(request,'home.html')
    