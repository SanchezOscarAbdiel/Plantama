import re
import conexionBD
num_serie = "7"
Usuario = "Prototipo"
conexionBD.consulta("INSERT INTO `registros` (`serial_planta`, `nombre_usuario`) VALUES ('"+num_serie+"', '"+Usuario+"')")