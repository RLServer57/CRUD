import mysql.connector

def conectar():
    conexion=mysql.connector.connect(host="localhost",user="rodrigo",passwd="lopsan",database="Peliculas")  
    return conexion