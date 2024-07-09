import requests
import re
import time
url = requests.post('https://19590325.tecsanjuan.com/PHPplantama/actualizaPlanta.php?humedad=102&serial_planta=117')
data = url.text
print(data)

