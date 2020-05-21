from zeep import Client

cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')

#Conversion de numero a letras
a = int(input("a:"))
print(cliente.service.NumberToWords(a))

#Conversion de numero a dolares
b = float(input("b:"))
print(cliente.service.NumberToDollars(b))

