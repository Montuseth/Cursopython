mes = int(input("Prporciaona el mes del año (1 - 12) :"))

estacion = None
if mes in (1,2,12):
    estacion = "invierno"
elif mes in (3,4,5):
 estacion = "primavera"
elif mes in (9,10,11):
    estacion = "Otoño"
elif mes in (6,7,8):
    estacion = "Otoño"
else:
    estacion = "valor incorrecto!"

print ("estacion :", estacion, " Para el mes :", mes)

