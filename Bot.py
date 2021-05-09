#recompiled by juanchi
#in process
#pip3 install pyTelegramBotAPI
import time
import requests
import telebot
from telebot import types

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
json = requests.get(URL).json()
TOKEN = 'Token_Here'

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Para empezar a usar el bot',
    'help'        : 'Obtener informacion de los comandos disponibles',
    'dolar'       : 'Para obtener los valores del dolar',
    'ping'        : '!ping',
    'pong'        : '!ping',
    'adminbirras' : 'Adminbirras',
}

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuario detectado, debe usar \"/start\" para empezar")
        return 0

# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener

# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hola extraño, te voy a escanear...")
        bot.send_message(cid, "Escaneo completo, ahora te conozco")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "Ya te conozco, no es necesario que te escanee devuelta")

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos son validos: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

# command dolar
@bot.message_handler(commands=['dolar'])
def command_dolar(m):
    cid = m.chat.id
    string1 = ''
    bot.send_message(cid, "💵 | compra | venta")
    for index, emoji in enumerate(("Oficial", "Blue   ", "Soja", "Liqui  ", "Bolsa  ", "Bitcoin", "Turista")):
        if(index!=2): #no tirar precio dolar soja
            compra = json[index]['casa']['compra'][:-1]
            venta = json[index]['casa']['venta'][:-1]
            string = emoji + '  | ' + compra + '  | ' + venta + '\n'
            string1 = string1 + string
    bot.send_message(cid, string1)

# command ping
@bot.message_handler(commands=['ping'])
def command_ping(m):
    cid = m.chat.id
    bot.send_message(cid, "/pong")

# command pong
@bot.message_handler(commands=['pong'])
def command_ping(m):
    cid = m.chat.id
    bot.send_message(cid, "/ping")

# command adminbeer
@bot.message_handler(commands=['adminbirras'])
def command_adminbirras(m):
    cid = m.chat.id
    bot.send_message(cid, "Fecha a definir, propongan 👀")

# command i love you
@bot.message_handler(commands=['Hola'])
def command_hola(m):
    cid = m.chat.id
    bot.send_message(cid, "I love you")

# command BOMB
@bot.message_handler(commands=['bomb'])
def command_bomb(m):
    cid = m.chat.id
    bot.send_message(cid, "Dale, escribi :(){ :|:& };:  en la terminal si tenes huevos 👀")

@bot.message_handler(func=lambda message: message.text == "Hola!")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you!")

bot.infinity_polling()
