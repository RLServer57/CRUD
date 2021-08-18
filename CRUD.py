import mysql.connector
from Conexion import conectar

class CRUD:
    def crear(self,titulo,anio):
        try:
            conexion=conectar()
            try:
                cursor=conexion.cursor()
                sql="insert into peliculas(titulo, anio) values (%s,%s);"
                cursor.execute(sql, (titulo, anio))
                conexion.commit()
                print('Pelis agregadas')
            finally:
                conexion.close()
        except (mysql.connector.Error) as e:
            print("Ocurrió un error al conectar: ", e)

    def leer(self):
        try:
            conexion=conectar()
            try:
                cursor=conexion.cursor()
                sql="SELECT * FROM peliculas;"
                cursor.execute(sql)
                peliculas = cursor.fetchall()
                for pelicula in peliculas:
                    print(pelicula)
            finally:
                conexion.close()
        except (mysql.connector.Error) as e:
            print("Ocurrió un error al conectar: ", e)

    def actualizar(self,titulo,id):
        try:
            conexion=conectar()
            try:
                cursor=conexion.cursor()
                sql="UPDATE peliculas SET titulo = %s WHERE id = %s;"
                cursor.execute(sql, (titulo,id))
                conexion.commit()
                print('Pelicula editada')
            finally:
                conexion.close()
        except (mysql.connector.Error) as e:
            print("Ocurrió un error al conectar: ", e)

    def eliminar(self,id):
        try:
            conexion=conectar()
            try:
                cursor=conexion.cursor()
                sql="DELETE FROM peliculas WHERE id = %s;"
                cursor.execute(sql,(id,))
                conexion.commit()
                print('Pelicula eliminada')
            finally:
                conexion.close()
        except (mysql.connector.Error) as e:
            print("Ocurrió un error al conectar: ", e)