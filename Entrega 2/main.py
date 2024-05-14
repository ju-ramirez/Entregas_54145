from Set.cl_cliente import Cliente
from Set.bd_clientes import *



cliente_0 = Cliente('Julieta Ramirez', 'julieta@gmail.com',25 )

valor = int(input("Ingresar importe de pago si desea pasar a usuario 'Premium', sino indique importe 0: "))
cliente_0.modificar_perfil(valor)

print(cliente_0)

rubro = input("Ingresar Rubro de preferencia o pulse 'espacio+enter' para continuar: ")
while rubro != " ":
    cliente_0.indicar_preferencias(rubro)
    rubro = input("Ingresar Rubro de preferencia o 'enter' para continuar: ")

print(cliente_0.mostrar_preferencias())

