# Ejemplo 29: Uso sencillo de sqlite3 (DB-API 2.0)
import sqlite3

conexion = sqlite3.connect(":memory:")  # Base de datos en memoria
cursor = conexion.cursor()              # Crea cursor

cursor.execute("CREATE TABLE usuarios (id INTEGER, nombre TEXT)")  # Crea tabla
cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (1, "Ana"))   # Inserta fila
conexion.commit()                                                  # Confirma cambios

cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)  # Muestra (1, 'Ana')

conexion.close()  # Cierra la conexión
