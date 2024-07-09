'''
Conexión a base de datos Plantama
'''
import pymysql 

    #                    "direccion","user", "password","BD"
db = pymysql.connect(host = "localhost",
                     user = "root",
                     password = "0214",
                     database = "plantama",
                     cursorclass=pymysql.cursors.DictCursor)
print("hola")

def consulta(): 
    '''
    Imprimir consultas
    '''

    c = "select `humedad` from `registros` where `nombre_usuario` = 'a'"
    with db.cursor() as cursor:
        print(c)
        cursor.execute(c)
        result = cursor.fetchone()
        print("A ",result)
        return result

consulta()