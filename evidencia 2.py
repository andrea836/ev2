import datetime
import csv

columnas=("Folio","FechaVenta","Articulo","Piezas","Precio con IVA")
datos=[]
precioFinal=0
respuestaWhile=1
respuesta=1
clave_venta=0


while respuesta==1:
    print("***MENU***")
    print("")
    print("1.Registrar venta")
    print("2.Consulta de venta")
    print("3.Reporte de fechas")
    print("4.Salir")
    print("")
    
    opcion=int(input("Ingrese una accion:\n"))
    
    if opcion==1:
    
        while respuestaWhile==1:
            clave_venta=clave_venta+1
            
            ventas=[]
            FechaCapturada=input("Dime la fecha de la venta (dd/mm/aaaa):\n")
            Articulo=input("Dime el articulo que fue vendido:\n")
            cantidad=int(input("Dime cuantas piezas fueron vendidas:\n"))
            precio=int(input("Dime el precio al cual fue vendido:\n"))
            preciofinal=precio*cantidad
            IVA=preciofinal*.16
            PrecioIVA=IVA+preciofinal
            ventas.append(clave_venta)
            ventas.append(FechaCapturada)
            ventas.append(Articulo)
            ventas.append(cantidad)
            ventas.append(PrecioIVA)
            datos.append(ventas)
            print(datos)
            print(f"El precio final ya con IVA es de {PrecioIVA}")
            
            respuestaWhile=int(input("¿Quiere realizar otra venta?: 1. SI o 0. NO\n"))
            
            with open("Ventas.csv","w",newline="") as archivo:
                registrador=csv.writer(archivo)
                registrador.writerow(columnas)
                registrador.writerows(datos)
                
                
    if opcion==2:
        
        with open("Ventas.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter = ",")
            registros = 0
    
            for Folio, FechaVenta, Articulo, Piezas, PrecioFinal in lector:
                if registros == 0:
                     columnas = (Folio, FechaVenta, Articulo, Piezas, PrecioFinal)
                     registros = registros + 1
                else:
                    Folio = int(Folio)
                    datos.append([Folio, FechaVenta, Articulo, Piezas, PrecioFinal])
        
        BuscarVenta=int(input("Que venta quieres buscar?: \n"))
        for ventas in datos :
            if ventas[0] == BuscarVenta:
                print(ventas)
                break
        else:
            print("Lo siento, esa venta no ha sido capturada")
        
        respuestaW=int(input("Quieres buscar otra venta?:  1 - SI o 0 - NO\n"))
      
    
    if opcion==3:
        
        respuestaW=1
        with open("Ventas.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter = ",")
            registros = 0
    
            for Folio, FechaVenta, Articulo, Piezas, PrecioFinal in lector:
                if registros == 0:
                     columnas = (Folio, FechaVenta, Articulo, Piezas, PrecioFinal)
                     registros = registros + 1
                else:
                    Folio = int(Folio)
                    datos.append([Folio, FechaVenta, Articulo, Piezas, PrecioFinal])
                    
        
        fechaBuscar = input("Dime una fecha (dd/mm/aaaa): \n")
        for ventas in datos:
            if ventas[1] == fechaBuscar:
                print(ventas)
                
        else:
            break

               
            
            respuestaW=int(input("Quiere buscar otra fecha?:  1 - SI o 0 - NO\n"))

    if opcion==4:
       print("Ha salido del programa correctamente")
       break
                               
                               