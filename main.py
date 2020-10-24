import mysql.connector

bd = mysql.connector.connect(user = 'angel', password = '12345678', database = 'mascota')
cursor = bd.cursor()

while True:
    print("1) Agregar Dueño ")
    print("2) Mostrar Dueños ")
    print("0) Salir")
    op = input("\nOpcion: ")

    if(op == "1"):
        foto = input("Foto: ")
        nom = input("Nombre: ")
        ap = input("Apellidos: ")
        domic = input("Domicilio: ")
        tel = input("Telefono: ")
        correo = input("Correo: ")

        consulta = "INSERT INTO duenio(foto, nombre, apellidos, domicilio, telefono, correo)" \
                   " VALUES(%s, %s, %s, %s, %s, %s)"

        cursor.execute(consulta, (foto, nom, ap, domic, tel, correo))
        bd.commit()

        if cursor.rowcount:
            print("Se agrego el dueño")
        else:
            print("Error")
    elif(op == "2"):
        consulta = "SELECT * FROM duenio"

        cursor.execute(consulta)

        for row in cursor.fetchall():
            print("Id: ", row[0])
            print("Foto: ", row[1])
            print("Nombre: ", row[2])
            print("Apellidos: ", row[3])
            print("Domicilio: ", row[4])
            print("Telefono: ",row[5])
            print("Correo: ", row[6]) 
            print("\n") 
    elif(op == "0"):
        break
