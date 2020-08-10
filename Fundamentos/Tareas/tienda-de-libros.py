print("Proporciene los siguientes datos del libro: ")
nombre = input("proporciene el nombre : ")
Id =int(input("Proporciona el ID:"))
precio = float(input("Proporcione el precio de libro: "))
envioGratuito = input("Indica si el envio es gratuito (True / False): ")

if envioGratuito == "True":
    envioGratuito = True
elif (envioGratuito == "False"):
    envioGratuito = False
else:
    print("Valor variable invalido")

print("Nombre: ", nombre,"\nId: ",Id, "\nPrecio: ", precio, "\nenvio gratuito? ", envioGratuito)
print(type(envioGratuito))