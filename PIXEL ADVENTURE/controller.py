import sqlite3 as sql

def createDB():
    conn = sql.connect("sqlite/ranking.db")
    conn.commit()
    conn.close()

# createDB()

def createTable():
    with sql.connect("sqlite/ranking.db") as conexion:
        try:
            sentencia = '''create table puntaje
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            puntos integer,
                            nivel text
                        )
                    '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntaje")                       
        except sql.OperationalError:
            print("La tabla puntaje ya existe")

# createTable()

def insertRow(nombre,puntos,lvl):
    with sql.connect("sqlite/ranking.db") as conexion:
        
        conexion.execute("INSERT INTO puntaje(nombre,puntos,nivel) VALUES (?,?,?)", (nombre,puntos,lvl))
        conexion.commit()# Actualiza los datos realmente en la tabla

# insertRow("Player",0,"nivel_uno")
# insertRow("Player",0,"nivel_uno")
# insertRow("Player",0,"nivel_uno")

# insertRow("Player",0,"nivel_dos")
# insertRow("Player",0,"nivel_dos")
# insertRow("Player",0,"nivel_dos")

# insertRow("Player",0,"nivel_tres")
# insertRow("Player",0,"nivel_tres")
# insertRow("Player",0,"nivel_tres")

def readRows():#insertar solo una fila
    conn = sql.connect("sqlite/ranking.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM puntaje ORDER BY puntos DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devolver todos los datos seleccionados
    conn.commit()
    conn.close()
    return datos

def readRows2(lvl):#insertar solo una fila
    conn = sql.connect("sqlite/ranking.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM puntaje WHERE nivel = ? ORDER BY puntos DESC LIMIT 3"
    cursor.execute(instruccion,(lvl,))
    datos = cursor.fetchall()#devolver todos los datos seleccionados
    conn.commit()
    conn.close()
    return datos

# print(readRows2("nivel_uno"))

def insertRows(lista_data):
    conn = sql.connect("sqlite/ranking.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO puntaje VALUES(?,?,?)"
    cursor.executemany(instruccion,lista_data)#insertar varias filas
    conn.commit()
    conn.close()

def deleteRow(id_table):
    id = id_table
    with sql.connect("sqlite/ranking.db") as conexion:
        sentencia = "DELETE FROM puntaje WHERE id=?"
        cursor=conexion.execute(sentencia,(id,))

# deleteRow(1)

def updateRow(id,puntos_player):
    with sql.connect("sqlite/ranking.db") as conexion:
        sentencia = "UPDATE puntaje SET puntos = ? WHERE id = ?"
        cursor=conexion.execute(sentencia,(puntos_player,id,))
        filas=cursor.fetchall()
        return filas

# data = readRows()
# print(data)