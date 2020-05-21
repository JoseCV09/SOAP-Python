from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
#Suma
a,b = int(input("a:")), int(input("b:"))

print("Suma de",a,"+",b,"es:",cliente.service.Add(a,b))
#Resta
print("Resta de",a,"-",b,"es:",cliente.service.Subtract(a,b))
#Multiplicación
print("Multiplicacion de",a,"*",b,"es:",cliente.service.Multiply(a,b))
#División
print("División de",a,"/",b,"es:",cliente.service.Divide(a,b))




