from db.conexion import obtener_conexion

def agregar_resultado(nombre,jugador,computador, resultado):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO resultado VALUES(:1, :2, :3, :4)",
        [nombre,jugador,computador, resultado])
        conexion.commit()
    except Exception as ex:
        print("Error al insertar datos:",ex)
        raise
    finally:
        cursor.close()
        conexion.close()

def obtener_resultados():
    conexion = obtener_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, jugador, computador, resultado FROM resultado")
        resultados = cursor.fetchall()
        return resultados
    except Exception as ex:
        print("Error al obtener resultados:",ex)
        return []
    finally:
        cursor.close()
        conexion.close()

def borrar_resultados():
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM resultado")
        conexion.commit()
    except Exception as ex:
        print("Error al borrar resultados:",ex)
    finally:
        cursor.close()
        conexion.close()