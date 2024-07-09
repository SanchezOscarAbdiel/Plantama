import telebot #libreria instalada desde PIP
import conexionBD
import re
import requests
import json

bot = telebot.TeleBot("6226389297:AAEzsmJtYbqEY4BhxKsoQucF-YF5DBL4Meo") #inicializacion de token dado por Telegram
regex = re.compile(r"/registro\n--(\d+)")
#comandos de ingreso

@bot.message_handler(commands=["help", "start","humedad","temperatura","estado","registro", "ayudaregistro"]) 

def enviar(message):
    Usuario = message.from_user.first_name
    Texto = message.text
    print(Texto)
    archivo = open("D:\Eclopse\Plantama\Main/texto.txt", "r") #Archivo .txt donde hay grandes bloques de texto
    texto = archivo.read().split('==') #Convierte el texto en una lista separando el txt en base a '=='

#--------------#
    def start():
        bot.reply_to(message,"Bienvenido a PlantamaBOT\nDesarrollado por CompasPemex") #respuesta de mensaje Start

    def help():
        bot.reply_to(message,texto[1])
        
    def AyudaRegistro():
        bot.reply_to(message, texto[2])

    def humedad():
        url = requests.get('https://19590325.tecsanjuan.com/PHPplantama/consultaHumedad.php?usuario=Sanchez%20Oscar')
        data = url.text
        humedad_str = re.search(r'"humedad":"(\d+)"', data)
        if humedad_str:
            humedad = "La humedad de tu planta es: "+humedad_str.group(1)
            print(humedad)
            bot.reply_to(message, humedad)
        else:
            bot.reply_to(message, "No se encontró la humedad")

        

    def estado():
        estado = conexionBD.consulta("select `estado` from `registros` where `nombre_usuario` = '"+Usuario+"'")
        reply = "El estado de tu planta es: "+ str(estado['estado'])
        bot.reply_to(message, reply)

    def registro():
    # Obtener el número después del comando /registro usando la expresión regular
        match = regex.search(Texto)
        if match:
            num_serie = match.group(1)
            url = 'https://19590325.tecsanjuan.com/PHPplantama/registro.php?serial_planta='+num_serie+'&usuario='+Usuario
            response = requests.post(url)
            print(response.text)
            if response.text == "ACCEPT":        
                bot.reply_to(message, f"Registro correctamente.")
            else:
                bot.reply_to(message, f"Error, ya tienes una planta registrada.")
        else:
            bot.reply_to(message, "No se encontró un número de serie en el comando.")

    menu = {
        "/start": start,
        "/help": help,
        "/ayudaregistro": AyudaRegistro,
        "/humedad": humedad,
        "/estado": estado,
        "/registro": registro
    }

    if Texto in menu:
        menu[Texto]()
    elif regex.match(Texto):
        registro()
    else:
        bot.reply_to(message, "El comando no existe o no ha sido implementado aun.")

        
    
'''
Recupera los mensajes de los usuarios
'''    
@bot.message_handler(func=lambda message:True) #comandos de ingreso
def mensaje(message):
    print(message)
    
    bot.reply_to(message," No es un comando. \n\nIngresa '/help' para conocer todas las funciones")

bot.polling()#Mantiene al bot escuchando
