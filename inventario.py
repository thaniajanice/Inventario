import mysql.connector

conexion= mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="inventario"
);

def create():
    print("__ AGREGAR RESERVA __")
    name=input("Nombre: ")
    print("-----------------------")
    age=int(input("Edad: "))
    print("-----------------------")
    lista=["Car = Q200","Motorcycle = 100","SUV = Q350"]
    for listas in lista:
        print(listas)
    typ_vehicle=input("Tipo de vehiculo: ").lower()
    print("-----------------------")
    days=int(input("Dias de renta: "))
    est="LongRental" if days >= 5 else "ShortRental"

    a=200
    b=100
    c=350
    if typ_vehicle== "car":
        total=a*days
    elif typ_vehicle == "motorcycle":
        total=b*days

    elif typ_vehicle == "SUV":
        total=c*days
    else:
        print("Error")

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="INSERT INTO renta(nombreCliente,edad,tipoVehiculo,diasRenta,precioFinal,estado) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,age,typ_vehicle,days,total,est))
        conexion.commit()
        print("Registro guardado")
        print(f"Su ID: {cursor.lastrowid}")


def read():
    print("__ Revisar registros __")
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="SELECT * FROM renta"
        cursor.execute(query,)
        invent=cursor.fetchall()
        for listas in invent:
            print(listas)

def update():
    print("--- ACTUALIZAR ---")
    id=int(input("Ingrese el número de ID: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM renta WHERE idrenta = %s",(id,))
        dato=cursor.fetchall()
        for lista in dato:
            print(lista)

        if dato:
            print("Registro encontrado")
            print("Ingrese los nuevos datos: ")
            new_name=input("Nombre: ")
            print("-------------------")
            new_age=int(input("Edad: "))
            print("-------------------")
            hola=["Car = Q200","Motorcycle = Q100","SUV = Q350"]
            for listas in hola:
                print(listas)
            new_typ=input("Tipo de vehiculo: ").lower()
            print("-------------------")
            new_days=int(input("Dias de renta: "))
            est="LongRental" if new_days >= 5 else "ShortRental"

            if new_typ == "car":
                new_total= 200*new_days
            elif new_typ == "motorcycle":
                new_total=100*new_days
            elif new_typ== "suv":
                new_total=350*new_days
            else:
                print("ERROR")

            query="""
                UPDATE renta
                SET nombreCliente=%s,
                    edad=%s,
                    tipoVehiculo=%s,
                    diasRenta=%s,
                    precioFinal=%s,
                    estado=%s

                WHERE idrenta=%s


"""
            cursor.execute(query,(new_name,new_age,new_typ,new_days,new_total,est,id))
            conexion.commit()
            print("Se actualizó correctamente")

        else:
            print("No se encontro el registro")

            


def delete():
    print("--- ELIMINAR ---")
    id=int(input("Ingrese el número de ID: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="DELETE FROM renta WHERE idrenta=%s"
        cursor.execute(query,(id,))
        conexion.commit()
        print("Se eliminó correctamnete")

def menu():
    print("BIENVENIDO AL MENU")
    while True:
        try:
            lista=["1. Agregar nueva reservar ","2. Revisar reservas ","3. Actualizar reservas","4. Eliminar reserva"]
            for listas in lista:
                print(listas)
            desi=int(input("Ingrese el número de opción a trabajar: "))
            break
        except ValueError:
            print("Esta no es una opcón")

    if desi==1:
        create()
    elif desi ==2:
        read()
    elif desi==3:
        update()
    elif desi ==4:
        delete()
    else:
        pass

menu()