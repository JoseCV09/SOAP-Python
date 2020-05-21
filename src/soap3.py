from zeep import Client

cliente = Client(wsdl='https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl')

#Conversion de numero a letras

print(cliente.service.wsasidepto("C","2011-12","B142",""))
print(cliente.service.wsareasdpto("C","V","E"))