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
# Insertar informacion desde un dict
# from pydatabase import conexion
# try:
#     with conexion.cursor() as cursor:
#         valores = [
#             {
#                 'titulo': 'ff',
#                 'anio': 1999
#             },
#             {
#                 'titulo': 'fffff',
#                 'anio': 7854
#             }
#         ]
#         #print(valores)
#         for dict in valores:
#             values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
#             sql = "INSERT INTO %s (titulo,anio) VALUES ( %s );" % ('peliculas', values)
#             print(sql)
#             cursor.execute(sql)
#             cursor.commit()
#             print("Se ingreso con exito")
# except Exception as e:
#     print("Error al ingresar datos: ",e)
# finally:
#     conexion.close()

# Combinar dos dicts
# dict1 = [
#     {
#         'Titulo': 'Juano',
#         'Edad': 23
#     },
#     {
#         'Titulo': 'Banano',
#         'Edad': 20
#     }
#
# ]
# dict2 = [
#     {
#         'Direccion': 'EDOMEX',
#         'Telefono': 5521190023
#     },
#     {
#         'Direccion': 'CDMX',
#         'Telefono': 5514691810
#     }
# ]
# for key in dict1:
#     for key2 in dict2:
#         key.update(key2)
# print(key)

#Fechas con Python
# from datetime import datetime
#
# date = {
#     'received_on': str(datetime.now())
# }
# print(date)

# Sustituir un valor de un key
# response_data = [
#     {
#         'received': 7156,
#         'sent': 2081,
#         'ts': '2020-10-28T00:00:00.000000Z'
#     },
#     {'received': None, 'sent': None, 'ts': '2020-10-29T00:00:00.000000Z'},
#     {'received': 1010, 'sent': 288, 'ts': '2020-10-30T00:00:00.000000Z'},
#     {'received': 540, 'sent': None, 'ts': '2020-11-04T00:00:00.000000Z'},
#     {'received': 18742, 'sent': None, 'ts': '2020-11-05T00:00:00.000000Z'}
# ]
# for i in response_data:
#     if i['received'] == None:
#         i.update(received='null')
#     if i['sent'] == None:
#         i.update(sent='null')
#
# print(i)

# Timestamp to datetime
# from datetime import datetime
# timestamp = 1606190465
# new_date = datetime.fromtimestamp(timestamp)
# print(new_date)

# Local time to UTC time
# import pytz, datetime
# local = pytz.timezone("America/Los_Angeles")
# naive = datetime.datetime.strptime("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
# local_dt = local.localize(naive, is_dst=None)
# utc_dt = local_dt.astimezone(pytz.utc)
# print(utc_dt)

#Prueba de cambio de formato de fechas a UTC
from datetime import datetime
import pytz
response = [
    {
        'id': '584342051651885713',
        'batteryEstCharge': '85',
        'lastConnected': 1606192497,
        'cellularDataUsed': 6457,
        'location': 'Dr. R. Michel 1310, Mirador',
        'Received_On': '2020-11-23 22:15:33.047195'
    },
    {
        'id': '584342051651885713',
        'batteryEstCharge': '85',
        'lastConnected': 1606192497,
        'cellularDataUsed': 6457,
        'location': 'Dr. R. Michel 1310, Mirador',
        'Received_On': '2020-11-23 22:15:33.047195'
    }
]
for key in response:
    # Cambiamos formato de campo lastConnected a datetime
    timestamp = key['lastConnected']
    new_date = datetime.fromtimestamp(timestamp)
    stamp_utc = new_date.astimezone(pytz.utc)
    key.update(lastConnected=stamp_utc)
    print(key)
