# Este es el ID de una unidad de prueba
#device_id = 584342051651873968
# Este es un ejemplo de vehicle ID
#vechicle_Id = 123456789

def conectivity_info(vehicle_id, device_id):
    # Fechas con Python
    from datetime import datetime
    # Importamos libreria de Meraki
    import meraki
    # Importamos la clase de conexión
    from pydatabase import conexion

    # Clave API
    API_KEY = "407c11244ffb6289d3add7ffacc6945adefdfbb4"
    # Pasamos la clave al Dashboard de la API para la autenticación
    dashboard = meraki.DashboardAPI(API_KEY)

    # Este es el ID de la red en Meraki
    network_id = 'N_584342051651361715'

    # Obtenemos los datos, bateria, última conexión y posición
    response = dashboard.sm.getNetworkSmDevices(
        network_id,
        total_pages='all',
        fields=['batteryEstCharge', 'lastConnected', 'cellularDataUsed']
    )
    # Recorremos el diccionario para borrar unos indices que no nos sirven
    for i in range(len(response)):
        response[i].pop('name')
        response[i].pop('tags')
        response[i].pop('ssid')
        response[i].pop('wifiMac')
        response[i].pop('osName')
        response[i].pop('systemModel')
        response[i].pop('uuid')
        response[i].pop('serialNumber')
        response[i].pop('hasChromeMdm')

    # Comienza la insercion a la base de datos
    try:
        with conexion.cursor() as cursor:
            # Sustituimos los None por null en el dict
            for key in response:
                if key['cellularDataUsed'] == None:
                    key.update(cellularDataUsed='null')
                # Ingresamos la fecha de creación del registro
                key['Received_On'] = datetime.now()
                # Visualizamos el dict completo
                # print(key)
                values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in key.values())
                sql = "INSERT INTO %s (Vehicle_Id, Meraki_id, Battery_Level, Last_Connected, Data_Used, Location, Received_On) VALUES (%s, %s);" % ('conectivity_info_device', vehicle_id, values)
                # cursor.execute(sql)
                # cursor.commit()
                print(sql)
    except Exception as e:
        print("Ocurrio un error al insertar: ", e)
    finally:
        conexion.close()

conectivity_info(316, 584342051651873968)