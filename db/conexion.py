import oracledb

def obtener_conexion():
    try:
        return oracledb.connect(
            user="C##cachipun",
            password="cachipun",
            dsn="localhost/xe")
    except oracledb.Error as ex:
        print("Error al conectar con la base de datos:",ex)
        return None
