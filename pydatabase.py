import pyodbc

server = 'localhost'
database = 'Meraki'
username = 'sa'
password = 'jrojas123'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    #Conexión exitosa
    print("Conectada")
except Exception as e:
    #Atrapamos el error
    print("Ocurrió un error al conectar a SQL Server: ", e)