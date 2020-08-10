valor = int(input("favor ingresar evaluacion \n(este debe ser un numero entre 1 y 10): "))
evaluacion = None
if valor in (9,10):
    evaluacion = "A"
elif valor == 8 or valor <= 9:
    evaluacion = "B"
elif valor == 7 or valor <= 8:
    evaluacion = "A"
elif valor == 6 or valor <= 7:
    evaluacion = "A"
elif valor > 0 and valor < 6:
    evaluacion = "A"
else:
    evaluacion = "Evaluacion: #NA, reingrese evaluacion"
    
print("Su evaluacion es = ", evaluacion)
    