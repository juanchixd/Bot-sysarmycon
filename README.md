# Bot de telegram de la comunidad de SysArmy Concordia

[![Python](https://www.python.org/static/community_logos/python-powered-w-200x80.png)](https://www.python.org)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Comandos actuales
>/start: Para empezar a usar el bot
>
>/help: Obtener informacion de los comandos disponibles
>
>/dolar: Para obtener los valores del dolar
>
>/ping: !ping
>
>/pong: !ping
>
>/adminbirras: Adminbirras
>
>/search: /search "lo que quieras buscar" y te manda a google
>
>/clima: Tenes que poner la ciudad despues del comando, ej: /clima Concordia
>
>/setbeer: Setear la fecha y lugar de la birra
>
>/btc: Binance, bitcoin
>
>/dns: Era-el-dns.png

## Instalación
Tener instalado previamente python3. Si no lo tenes instalado, te dejo el tutorial:
[Pagina oficial de python][pydownload]

Primero instalar las siguientes librerias
```sh
python3 -m pip install --upgrade pyTelegramBotAPI
python3 -m pip install --upgrade python-dotenv
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

```

>Luego creamos un bot con BotFather y nos guardamos el token que nos genera

>Conseguir un token para la api de [Open Weather Map][weather] y la guardamos

>Copiamos este repositorio y lo pegamos en donde querramos

>Creamos un archivo .env dentro de la misma carpeta donde tengamos nuestro archivo .py que contenga lo siguiente:

```sh
SYS_TOKEN= TOKEN que te da BotFather
URL_DOLAR=https://www.dolarsi.com/api/api.php?type=valoresprincipales
URL_BTC=https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
WEATHER_TOKEN= aca ponemos el TOKEN de openweathermap.org
ID_GROUP_SYS= id del grupo para el comando recordatorio
```
Y lo guardamos

## Ejecución

Terminado de configurar el .env, ejecutamos nuestro codigo con:
```sh
python3 Bot.py
```
Le hablamos al privado de nuestro bot, le ingresamos un /start y nos tendria que responder lo siguiente

![Telegram chat](https://raw.githubusercontent.com/juanchixd/Bot-sysarmycon/main/1.jpg)

Y listo, tendriamos andando nuestro bot, solo faltaria meterlo en crontab o systemd para que arranque automaticamente

## Links de interes


| Content | Link |
| ------ | ------ |
| PyTelegramBotAPI | [Repositorio][pyapi] |
| Telegram Core API | [Bot Api][telegram] |
| Mi telegram | [Contact][contactTG] |
| Python | [Official][py] |
| Web | [My web][web] |

[//]: # 
   [weather]: <https://openweathermap.org/>
   [pydownload]: <https://www.python.org/downloads/>
   [py]: <https://www.python.org/>
   [pyapi]: <https://github.com/eternnoir/pyTelegramBotAPI>
   [telegram]: <https://core.telegram.org/bots/api>
   [contactTG]: <https://t.me/Juanbgon>
   [web]: <https://juangonzalez.com.ar>
