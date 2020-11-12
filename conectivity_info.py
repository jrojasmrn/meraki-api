def conectivity_info():
    # Importamos libreria de Meraki
    import meraki
    # Importamos la clase de conexión
    from pydatabase import conexion

    # Clave API
    API_KEY = "407c11244ffb6289d3add7ffacc6945adefdfbb4"
    # Este es el ID de una unidad de prueba
    device_id = 584342051651875398
    # Pasamos la clave al Dashboard de la API para la autenticación
    dashboard = meraki.DashboardAPI(API_KEY)

    # Este es el ID de la red en Meraki
    network_id = 'N_584342051651361715'

    # Obtenemos  el historial de datos de una unidad
    response_data = dashboard.sm.getNetworkSmDeviceCellularUsageHistory(
        network_id,
        device_id
    )
    # Obtenemos el historial de conectividad del telefono
    response_con = dashboard.sm.getNetworkSmDeviceConnectivity(
        network_id,
        device_id,
        total_pages='all',
        direction='next'
    )

    # Comienza la insercion a la base de datos
    try:
        with conexion.cursor() as cursor:
            # Combinamos ambos dicts para generar uno solo
            for key in response_data:
                for key2 in response_con:
                    key.update(key2)
                    # Imprimimos Dict combinado
                    #print(key)
                    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in key.values())
                    sql = "INSERT INTO %s (Meraki_id, Received, Sent, Ts, First_Seen_At, Last_Seen_At, Received_On) VALUES (%s);" % ('conectivity_info_device', values)
                    print(sql)
    except Exception as e:
        print("Ocurrio un error al insertar: ", e)
    finally:
        conexion.close()

conectivity_info()