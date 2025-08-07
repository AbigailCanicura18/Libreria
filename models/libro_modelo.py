from db.conexion_oracle import obtener_conexion

def agregar_libro(isbn,titulo,autor,anio,biblio):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO libro VALUES(:1, :2, :3, :4, :5)", 
                       [isbn,titulo,autor,anio,biblio])
        conexion.commit()
    except Exception as ex:
        print("Error:",ex)
        raise
    finally:
        cursor.close()
        conexion.close()
