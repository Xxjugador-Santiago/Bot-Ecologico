import discord
import random
import os
import requests
from discord.ext import commands

#--------BOT--------

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f'Welcome... Hemos iniciado sesión como {bot.user}')

#--------COMANDOS DEL BOT--------
#Basico :
@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola!, soy Bot-Ecologico ☘")

@bot.command()
async def adios(ctx):
    await ctx.send("¡Hasta Luego y no olvides cuidar el planeta! 🪐🌳☘")

@bot.command()
async def comandos(ctx):
    await ctx.send(f"comandos: 1 $hola : el bot saluda. 2 $adios : el bot se despide. 3 $comandos : lista de comandos.")

#Bot :

@bot.command()
async def plastico(ctx):
    await ctx.send(f"")

@bot.command()
async def tips(ctx):
    await ctx.send(f"Aqui tienes unos tips para reducir la contaminacion")
    await ctx.send(f"1) Usa transporte sostenible: Elige caminar, andar en bicicleta, o usa el transporte publico en vez de viajar en auto")
    await ctx.send(f"2) Participa en actividades de limpieza: Participa en grupos para limpiar playas, parques o plazas, y espacios publicos")
    await ctx.send(f"3) Compra productos ecologicos: Evita comprar aerosoles que contaminen, compra productos con certificacion ecologica, intenta comprar productos que no contaminen su uso y cuando lo desechas")

#--------ideas--------
#Tip de energías renovables
#Reutilización eficaz de las bolsas de plástico y bolsas reutilizables
#Mencione grupos sin fines de lucro que busquen ayuda para disminuir la contaminación
#Mencionar una serie de pasos o tips sencillos para reducir la contaminación
#Siembra de árboles en el hogar
#Mencionar una lista de 5 o más de los productos más desechados por las personas en un ranking mundial

#--------BOT KEY--------
bot.run("")
