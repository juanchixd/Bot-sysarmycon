#!/usr/bin/python3
#recompiled by juanchi
#in process
#pip3 install pyTelegramBotAPI
#libreria a instalar primero
import math
import time
import subprocess
import os
import sys
import requests
import telebot
import math
from subprocess import Popen, PIPE
from telebot import types
URL_DOLAR = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
global cont
cont = 0
TOKEN = 'INSERT TOKEN'

commands = {  # command description used in the "help" command
    'start'       : 'Para empezar a usar el bot',
    'help'        : 'Obtener informacion de los comandos disponibles',
    'dolar'       : 'Para obtener los valores del dolar',
    'ping'        : '!ping',
    'pong'        : '!ping',
    'adminbirras' : 'Adminbirras',
    'btc'         : 'Binance, bitcoin',
    'dns'         : 'Era-el-dns.png',
}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, "Hola, este es el bot de la comunidad de SYSARMY Concordia")
    command_help(m)  # show the new user the help page

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos son validos: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

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
    print(cont)
    if cont == 5:
        bot.send_message(cid, "Se acabo el shampoo, deja de ser tan pelotudo")
        cont = 0
    elif shampoo == True:
        bot.send_message(cid, "Por gente como vos, el Shampoo trae instrucciones")
    else:
        None

@bot.message_handler(commands=['btc', 'bitcoin', 'bit'])
def bit(m):
    global cont
    cid = m.chat.id
    a = telebot.util.extract_arguments(m.text)
    json = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
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
        f = open('beer.txt', 'w')
        f.write(arg)
        f.close()
        bot.send_message(cid, "ANOTADO\nVamos por unas birras? Fecha: %s %s\nLugar: %s\nSe prenden?\nEl que no va se lo pierde\nVamos a repartir calcos 👀👀" %(corte[0], corte[1], corte[2]))
    elif arg.count(',') > 2:
        bot.send_message(cid, "Te dije solo 3 argumentos con comas entre medio")
    else:
        None

#command adminbeer
@bot.message_handler(commands=['adminbirras'])
def command_adminbirras(m):
    f = open('beer.txt','r')
    cid = m.chat.id
    arg = f.read()
    f.close()
    corte = arg.split(',')
    corte = [s.strip() for s in corte]
    bot.send_message(cid, "Vamos por unas birras? Fecha: %s %s\nLugar: %s\nSe prenden?\nEl que no va se lo pierde\nVamos a repartir calcos 👀👀" %(corte[0], corte[1], corte[2]))

@bot.message_handler(commands=['hola'])
def command_hola(m):
    cid = m.chat.id
    bot.send_message(cid, "I love you")

@bot.message_handler(commands=['bomb'])
def command_bomb(m):
    cid = m.chat.id
    bot.send_message(cid, "Dale, escribi :(){ :|:& };:  en la terminal si tenes huevos 👀")

#Command era-el-dns.png
@bot.message_handler(commands=['dns'])
def command_dns(m):
    cid = m.chat.id
    p = open('dns.png', 'rb')
    bot.send_photo(cid, p)

#Command uptime
@bot.message_handler(commands=['uptime'])
def uptim(m):
    cid = m.chat.id
    uptime = subprocess.getoutput('uptime -p')
    bot.send_message(cid, "Uptime: {}".format(uptime));

#Command temperatura
@bot.message_handler(commands=['temperatura'])
def temperatura(m):
    cid = m.chat.id
    temp    = round(int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3, 2)
    tempgpu = subprocess.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace("'C", '')
    bot.send_message(cid, "Temperatura:\nCPU: {}  °C\nGPU: {}  °C". format(temp, tempgpu));

@bot.message_handler(func=lambda message: message.text == "Hola!")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you!")

#command search
@bot.message_handler(commands=['search'])
def google(m):
    cid = m.chat.id
    a = telebot.util.extract_arguments(m.text)
    string = 'https://letmegooglethat.com/?q=' + a
    string = string.replace(" ", "+")
    bot.send_message(cid, str(string) + " Era muy complicado? Sound: Probaste googleando - Nerdearla")
    audio = open('/home/pi/BOTS/google.mp3', 'rb')
    bot.send_audio(cid, audio)

def check_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

bot.infinity_polling()