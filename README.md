# Scapy
Práctica de Scapy
1. Canal encubierto IP
Enunciado

Requisitos previos: Python, Scapy, conocimientos de red

Objetivo: realizar un script Python que utilice un canal encubierto IP.

Enunciado:

Un canal encubierto IP (covert channel IP) es un canal de comunicación entre dos equipos que utilizan el ancho de banda de otro canal con el objetivo de transmitir información sin la autorización o conocimiento del propietario de la información o el administrador de la red.

Prepare este script Python empleando Scapy.

2. Detección de Rogue AP (Access Point)
Enunciado

Requisitos previos: Python, Scapy, conocimientos de red

Objetivo: preparar un script Python que detecte la presencia de un rogue AP en nuestra red.

Enunciado:

Cree un script Python utilizando Scapy que le permita detectar si hay un rogue AP en su red.

El fallo de seguridad llamado Rogue AP es el más temido a nivel empresarial (traduciremos rogue como indeseable, o canalla). Se produce cuando un usuario de la red, por comodidad a nivel de su oficina por ejemplo, conecta un punto de acceso a la toma Ethernet cableada, que le permite cierta movilidad con su equipo en el interior del entorno así creado. Estas instalaciones piratas, no necesariamente maliciosas, son especialmente peligrosas porque abren la red de la empresa al mundo Wi-Fi, por lo general con un nivel de seguridad muy bajo (autenticación reducida de tipo WEP con una clave de 40 bits, sin Firewall, IDS, o detección de intentos de ataques, etc.). En el peor de los casos, el ordenador puede funcionar como un puente, creando un Wireless Bridge: un vínculo "abierto" entre la red Wi-Fi y la red local cableada.


3. IP Spoofing
Enunciado

Requisitos previos: Python, Scapy, conocimientos de red

Objetivo: crear un script Python que permita realizar un IP spoofing.

Enunciado:

Sea el servidor siguiente:


import socket  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = ''  
port = 4000  
s.bind((host,port))  
while 1:  
        s.listen(1)  
        conn, addr = s.accept()  
        if(addr[0]=="195.221.189.111"):  
                print "ok"  
        else:  
                print "nok";  
conn.close()
 
Programar un script que permita hacer pasar a su equipo por otro.

4. Spoofing IPv6 de los vecinos
Enunciado

Requisitos previos: Python, Scapy, conocimientos de red y de IPv6

Objetivo: crear un script Python que permita realizar un IP spoofing IPv6.

Enunciado:

Fabrique su propio script Python que haga "spoof" (IPv6) de los vecinos.
