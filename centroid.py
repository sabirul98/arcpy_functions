import arcpy

arcpy.env.workspace ="D:\UNOM 2nd  Sem\Paper writting"

input=("D:\UNOM 2nd  Sem\Paper writting\WB_Export_Output.shp")
output="D:\UNOM 2nd  Sem\Paper writting\WB_Export_Output_centeroid1.shp"

arcpy.FeatureToPoint_management(input,output,"CENTROID")
print arcpy.GetMessages()


