#!/usr/bin/python3
#recompiled by juanchi
#in process
#python3 -m pip install --upgrade pyTelegramBotAPI
#python3 -m pip install --upgrade python-dotenv
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
#libreria a instalar primero
import math
import subprocess
import requests
import telebot
import math
import os
from PIL import Image, ImageDraw, ImageFont
from subprocess import PIPE
from dotenv import load_dotenv
load_dotenv()
TOKEN_SYS = os.getenv('SYS_TOKEN')
URL_DOLAR = os.getenv('URL_DOLAR')
URL_BTC = os.getenv('URL_BTC')
TOKEN_WEATHER = os.getenv('WEATHER_TOKEN')
IDGROUP = os.getenv('ID_GROUP_SYS')
global cont
cont = 0
bot = telebot.TeleBot(TOKEN_SYS)
commands = {
    'start'       : 'Para empezar a usar el bot',
    'help'        : 'Obtener informacion de los comandos disponibles',
    'dolar'       : 'Para obtener los valores del dolar',
    'ping'        : '!ping',
    'pong'        : '!ping',
    'adminbirras' : 'Adminbirras',
    'git'         : 'Te manda el link del repo',
    'search'      : '/search "lo que quieras buscar" y te manda a google',
    'clima'       : 'Tenes que poner la ciudad despues del comando, ej: /clima Concordia',
    'setbeer'     : 'Setear la fecha y lugar de la birra',
    'btc'         : 'Binance, bitcoin',
    'dns'         : 'Era-el-dns.png',
}

#command start
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, "Hola, este es el bot de la comunidad de SYSARMY Concordia")
    command_help(m) 

#command help
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos son validos: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)

#command dolar
@bot.message_handler(commands=['dolar', 'dólar', 'dolor'])
def dolar(m):
    global cont
    cid = m.chat.id
    a = telebot.util.extract_arguments(m.text)
    json = requests.get(URL_DOLAR).json()
    string1 = "💵 | compra | venta" + "\n"
    shampoo = False
    c = 0
    if len(a) != 0 and any(map(str.isdigit, a)) != True and a.find('e') != -1 or a.find('E') != -1:
        cont = cont + 1
        shampoo = True
    elif len(a) != 0:
        a = a.replace(",", ".")
        if check_float(a) == True:
            b = float(a)
            for index, emoji in enumerate(("Oficial", "Blue   ", "Soja", "Liqui  ", "Bolsa  ", "Bitcoin", "Solidario")):
                if(index!=2 and index!=5):
                    compra = json[index]['casa']['compra'][:-1]
                    venta = json[index]['casa']['venta'][:-1]
                    if (compra != 'No Cotiz'):
                        compra = compra.replace(",", ".")
                        compra = float(compra) * b
                        compra = str(compra)
                        compra = compra.replace(".", ",")
                    venta = venta.replace(",", ".")
                    venta = float(venta) * b
                    if math.isinf(venta) == True:
                        c = 1
                    venta = str(venta)
                    venta = venta.replace(".", ",")
                    string = emoji + '  | ' + compra + '  | ' + venta + '\n'
                    string1 = string1 + string
            if c == 1:
                bot.send_message(cid, "Sera que iba a tener plata")
            else:
                bot.send_message(cid, string1)
        else:
            shampoo = True
            cont = cont + 1
    elif len(a) == 0 or a == 1:
        for index, emoji in enumerate(("Oficial", "Blue   ", "Soja", "Liqui  ", "Bolsa  ", "Bitcoin", "Solidario")):
            if(index!=2 and index != 5):
                compra = json[index]['casa']['compra'][:-1]
                venta = json[index]['casa']['venta'][:-1]
                string = emoji + '  | ' + compra + '  | ' + venta + '\n'
                string1 = string1 + string
        bot.send_message(cid, string1)
    else:
        shampoo = True
        cont = cont + 1
    if cont == 5:
        bot.send_message(cid, "Se acabo el shampoo, deja de ser tan pelotudo")
        cont = 0
    elif shampoo == True:
        bot.send_message(cid, "Por gente como vos, el Shampoo trae instrucciones")
    else:
        None

#command btc
@bot.message_handler(commands=['btc', 'bitcoin', 'bit'])
def bit(m):
    global cont
    cid = m.chat.id
    a = telebot.util.extract_arguments(m.text)
    json = requests.get(URL_BTC).json()
    string1 = "💰 | 💲(USD)" + "\n" + "Binance "
    shampoo = False
    c = 0
    if len(a) != 0 and any(map(str.isdigit, a)) != True and a.find('e') != -1 or a.find('E') != -1:
        cont = cont + 1
        shampoo = True
    elif len(a) != 0:
        a = a.replace(",", ".")
        if check_float(a) == True:
            b = float(a)
            string1 = string1 + str(float(json['price']) * b)
            precio = float(json['price']) * b
            if math.isinf(precio) == True:
                c = 1
            if c == 1:
                bot.send_message(cid, "Sera que iba a tener plata")
            else:
                bot.send_message(cid, string1)
        else:
            shampoo = True
            cont = cont + 1
    elif len(a) == 0 or a == 1:
        string1 = string1 + str(float(json['price']))
        bot.send_message(cid, string1)
    else:
        shampoo = True
        cont = cont + 1
    if cont == 5:
        bot.send_message(cid, "Se acabo el shampoo, deja de ser tan pelotudo")
        cont = 0
    elif shampoo == True:
        bot.send_message(cid, "Por gente como vos, el Shampoo trae instrucciones")
    else:
        None

#command git
@bot.message_handler(commands=['git'])
def git(m):
    cid = m.chat.id
    bot.send_message(cid, "El repo del bot es: https://github.com/juanchixd/Bot-sysarmycon")

#command ping
@bot.message_handler(commands=['ping'])
def command_ping(m):
    cid = m.chat.id
    bot.send_message(cid, "/pong")

#command pong
@bot.message_handler(commands=['pong'])
def command_ping(m):
    cid = m.chat.id
    bot.send_message(cid, "/ping")

#command weather
@bot.message_handler(commands=['clima'])
def clima(m):
    cid = m.chat.id
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?units=metric&" + "appid=" + TOKEN_WEATHER + "&q=" + telebot.util.extract_arguments(m.text)) 
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"] 
        z = x["weather"] 
        p = x["sys"]
        bot.send_message(cid, "Ciudad = " + str(x["name"]) + ", " + str(p["country"]) + " - temp = " + str(y["temp"]) + " - humedad = " + str(y["humidity"]) + "%"+ str(icono(z[0]["icon"]))) 
    else: 
        bot.send_message(cid, "Ciudad no encontrada") 

#command setadminbeer
@bot.message_handler(commands=['setbeer'])
def set_beer(m):
    cid = m.chat.id
    arg = telebot.util.extract_arguments(m.text)
    if len(arg) == 0:
        bot.send_message(cid, 'Junto al comando escribi separado por comas "FECHA, HORA, LUGAR"')
    elif len(arg) != 0 and arg.count(',') == 2:
        corte = arg.split(',')
        corte = [s.strip() for s in corte]
        f = open('txt/beer.txt', 'w')
        f.write(arg)
        f.close()
        fecha = corte[0] + ' ' + corte[1]
        lugar = corte[2]
        image = Image.open('img/plantilla.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 35)
        if len(lugar) > 30:
            lugar = lugar[:30] + "...\n" + lugar[30:]
        text = """nerd@Concordia:~/SysArmyCon$ cat Adminbirras.txt
Vamos por unas birras? Fecha: %s
Lugar: %s
Se prenden?
El que no va se lo pierde
Vamos a repartir calcos
nerd@Concordia:~/SysArmyCon$ apt-get install Beer""" % (fecha, lugar)
        draw.multiline_text((50, 150), text, font=font, fill="white")
        image.save('img/beer.png')
        bot.send_photo(cid, open('img/beer.png', 'rb'))
        bot.send_message(cid, "ANOTADO\nVamos por unas birras? Fecha: %s %s\nLugar: %s\nSe prenden?\nEl que no va se lo pierde\nVamos a repartir calcos 👀👀" %(corte[0], corte[1], corte[2]))
        bot.send_poll(cid, "Se prenden?", ['Si', 'No'], is_anonymous=False)
    elif arg.count(',') > 2:
        bot.send_message(cid, "Te dije solo 3 argumentos con comas entre medio")
    elif arg.count(',') < 2:
        bot.send_message(cid, "Y los otros argumentos?")
    else:
        None

#command adminbeer
@bot.message_handler(commands=['adminbirras'])
def command_adminbirras(m):
    f = open('txt/beer.txt','r')
    cid = m.chat.id
    arg = f.read()
    f.close()
    corte = arg.split(',')
    corte = [s.strip() for s in corte]
    bot.send_message(cid, "Vamos por unas birras? Fecha: %s %s\nLugar: %s\nSe prenden?\nEl que no va se lo pierde\nVamos a repartir calcos 👀👀" %(corte[0], corte[1], corte[2]))
    bot.send_photo(cid, open('img/beer.png', 'rb'))

#command recordatorio
@bot.message_handler(commands=['recordatorio'])
def recordatorio(m):
    f = open('txt/beer.txt','r')
    arg = f.read()
    f.close()
    corte = arg.split(',')
    corte = [s.strip() for s in corte]
    bot.send_message(IDGROUP, "HOY %s %s, ADMINBIRRAS EN %s. NO FALTES" %(corte[0], corte[1], corte[2]))

#command hola
@bot.message_handler(commands=['hola'])
def command_hola(m):
    cid = m.chat.id
    bot.send_message(cid, "I love you")

#command bomb
@bot.message_handler(commands=['bomb'])
def command_bomb(m):
    cid = m.chat.id
    bot.send_message(cid, "Dale, escribi :(){ :|:& };:  en la terminal si tenes huevos 👀")

#command dns
@bot.message_handler(commands=['dns'])
def command_dns(m):
    cid = m.chat.id
    p = open('img/dns.png', 'rb')
    bot.send_photo(cid, p)

#command uptime
@bot.message_handler(commands=['uptime'])
def uptim(m):
    cid = m.chat.id
    uptime = subprocess.getoutput('uptime -p')
    bot.send_message(cid, "Uptime: {}".format(uptime));

#command message=hi
@bot.message_handler(func=lambda message: message.text == "Hola!")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you!")

#command google
@bot.message_handler(commands=['search'])
def google(m):
    cid = m.chat.id
    a = telebot.util.extract_arguments(m.text)
    string = 'https://letmegooglethat.com/?q=' + a
    string = string.replace(" ", "+")
    bot.send_message(cid, str(string) + " Era muy complicado? Sound: Probaste googleando - Nerdearla")
    audio = open('google.mp3', 'rb')
    bot.send_audio(cid, audio)

def check_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def icono(i):
    icon = (
        ("01d", "☀️"),
        ("01n", "🌙"),
        ("02d", "🌥"),
        ("02n", "🌥"),
        ("03d", "☁️"),
        ("03n", "☁️"),
        ("04d", "☁️"),
        ("04n", "☁️"),
        ("09d", "🌦"),
        ("09n", "🌦"),
        ("10d", "🌧"),
        ("10n", "🌧"),
        ("11d", "⛈"),
        ("11n", "⛈"),
        ("13d", "🌨"),
        ("13n", "🌨"),
        ("50d", "🌫"),
        ("50n", "🌫"),
    )
    for a, b in icon:
        i = i.replace(a,b)
    return i

bot.infinity_polling()
