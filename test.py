'''
#Obtenemos  el historial de datos de una unidad
response = dashboard.sm.getNetworkSmDeviceCellularUsageHistory(
    network_id,
    device_id
)
'''
'''
#Obtenemos el historial de conectividad del telefono
response = dashboard.sm.getNetworkSmDeviceConnectivity(
    network_id,
    device_id,
    total_pages='all',
    direction='next'
)
'''
'''
###Eliminar un elemento del diccionario###
car = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}
print(car)
car.pop("c")
car_json = json.dumps(car,indent=4)
print(car_json)
'''
'''
#Insertar datos en la base de datos
from pydatabase import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO peliculas(titulo, anio) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Volver al futuro 1", 1985))
        cursor.execute(consulta, ("Pulp Fiction", 1994))
        cursor.execute(consulta, ("It", 2017))
        cursor.execute(consulta, ("Ready Player One", 2018))
        cursor.execute(consulta, ("Spider-Man: un nuevo universo", 2018))
        cursor.execute(consulta, ("Avengers: Endgame", 2019))
        cursor.execute(consulta, ("John Wick 3: Parabellum", 2019))
        cursor.execute(consulta, ("Toy Story 4", 2019))
        cursor.execute(consulta, ("It 2", 2019))
        cursor.execute(consulta, ("Spider-Man: lejos de casa", 2019))

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()
'''
'''
#Insertar varias columnas al mismo tiempo
from pydatabase import conexion
try:
    with conexion.cursor() as cursor:
        query = "INSERT INTO peliculas(titulo,anio) VALUES(?, ?)"
        valores = [
            ('TEST', 123),
            ('TEST2', 12),
            ('TEST3', 987),
        ]
        cursor.executemany(query, valores)
        conexion.commit()
        print("Se inserto con exito")
except Exception as e:
    print("Error al ingresar datos: ",e)
finally:
    conexion.close()
'''
from pydatabase import conexion
try:
    with conexion.cursor() as cursor:
        valores = [
            {
                'titulo': 'ff',
                'anio': 1999
            },
            {
                'titulo': 'fffff',
                'anio': 7854
            }
        ]
        #print(valores)
        for dict in valores:
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
            sql = "INSERT INTO %s (titulo,anio) VALUES ( %s );" % ('peliculas', values)
            print(sql)
            cursor.execute(sql)
            cursor.commit()
            print("Se ingreso con exito")
except Exception as e:
    print("Error al ingresar datos: ",e)
finally:
    conexion.close()