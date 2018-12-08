# func_simple_1.py
#
# T(°C) = (T(°F) - 32) × 5/9


fhtemp1 = 120
fhtemp2 = 260 
fhtemp3 = 300

ctemp1 = ( fhtemp1-32) * 5/9
ctemp2 = ( fhtemp2-32) * 5/9
ctemp3 = ( fhtemp3-32) * 5/9

print ("F = ", fhtemp1, "C= ", ctemp1 )

print ("F = ", fhtemp2, "C= ", ctemp2 )

print ("F = ", fhtemp3, "C= ", ctemp3 )

#########################################################

def F_to_C ( f ):
    c = ( f-32) * 5/9
    return c
	
ctemp1 = F_to_C ( fhtemp1 )
ctemp2 = F_to_C ( fhtemp2 )
ctemp3 = F_to_C ( fhtemp3 )

print ("after using functions")

print ("F = ", fhtemp1, "C= ", ctemp1 )

print ("F = ", fhtemp2, "C= ", ctemp2 )

print ("F = ", fhtemp3, "C= ", ctemp3 )
