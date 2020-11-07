# Función para obtener el catalogo de dispositivos
def devide_catalogue():
    # Importamos libreria de Meraki
    import meraki
    # Importamos la clase de conexión
    from pydatabase import conexion

    # Clave API
    API_KEY = "407c11244ffb6289d3add7ffacc6945adefdfbb4"
    # Pasamos la clave al Dashboard de la API para la autenticación
    dashboard = meraki.DashboardAPI(API_KEY)

    # Este es el ID de la organización en la MDM
    organization_id = '584342051651322784'
    # Este es el ID de la red en Meraki
    network_id = 'N_584342051651361715'

    # Obtenemos el catalogo de dispositivos totales (lo regresa como diccionario)
    response = dashboard.sm.getNetworkSmDevices(
        network_id,
        total_pages='all',
        direction='next'
    )

    # Recorremos el diccionario para borrar unos indices que no nos sirven
    for i in range(len(response)):
        # Eliminamos los indices 'tags', 'ssid' y 'hasChromeMdm'
        response[i].pop('tags')
        response[i].pop('ssid')
        response[i].pop('hasChromeMdm')

    # Imprimimos el diccionario
    # print(response)

    # Comienza la insercion a la base de datos
    try:
        with conexion.cursor() as cursor:
            for dict in response:
                values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
                sql = "INSERT INTO %s (Id,Name,Wifi_Mac,Os_Name,System_Model,Uuid,Serial_Number) VALUES (%s);" % (
                'device_catalogue', values)
                cursor.execute(sql)
                cursor.commit()
        print("Se ingreso con exito")
    except Exception as e:
        print("Ocurrio un problema al insertar: ", e)
    finally:
        conexion.close()

devide_catalogue()