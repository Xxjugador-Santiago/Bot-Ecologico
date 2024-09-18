import discord
import random
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
    print(f'Bienvenido Hemos iniciado sesión como {bot.user}')

#--------COMANDOS DEL BOT--------
#----Basico----:
@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola!, soy Bot-Ecologico ☘ , consulta los comandos con '$comandos' ")

@bot.command()
async def adios(ctx):
    await ctx.send("¡Hasta Luego y no olvides seguir cuidando el planeta! 🪐🌳☘")

@bot.command()
async def comandos(ctx):
    await ctx.send(f"Aqui tienes la lista de comandos")
    await ctx.send(f"1. '$hola' El bot saluda")
    await ctx.send(f"2. '$adios' El bot se despide")
    await ctx.send(f"3. '$comandos' El bot entrega una lista de comandos")
    await ctx.send(f"4. '$eco_grupos' Entrega una lista de grupos ecologicos")
    await ctx.send(f"5. '$bolsas' Entrega formas eficaces para reutilizar bolsas de plastico")
    await ctx.send(f"6. '$eco_tips' Entrega tips para reducir la contaminacion")
        
#--------Bot--------:

@bot.command()
async def eco_grupos(ctx):
    await ctx.send(f"Aqui te comparto 3 grupos mundiales sin fines de lucro para reducir la contaminacion")
    await ctx.send(f"1) 350.org: Es un movimiento internacional para poner fin los combustibles fósiles, y construir un mundo con energía renovable. Esta presente en mas de 70 paises, de, America, paises de Europa, America latina, Africa y Asia, consulta en https://350.org/es/ , hay un mapa para buscar tu pais!")
    await ctx.send(f"2) Fundación Terram: Aportan a la creación de una propuesta de modelo de desarrollo país, basada en la democracia, justicia ambiental, resguardo de la naturaleza y cuidado del entorno. Presente en Chile, puedes participar en https://www.terram.cl ")
    await ctx.send(f"3) MarViva: Es una organizacion que fomenta dinámicas de mercados responsables para productos y servicios marinos sostenible del mar. Presente en Costa rica, Panama, y Comlombia, participa en https://marviva.net ")
    
@bot.command()
async def bolsas(ctx):
    await ctx.send(f"Aqui te comparto formas eficaces de reutilizar bolsas de plastico")
    await ctx.send(f"1) Bolsas de basura: Utiliza las bolsas de plastico que no utilices o que vayas a desechar para los pequeños botes de basura de tu casa. Esto ayuda a reducir la necesidad de comprar bolsas de basura especificas")
    await ctx.send(f"2) Protege tus cosas: Puedes utilizar las bolsas de plastico que no uses para proteger tus cosas delicadas del polvo o humedad, le podras dar un segundo uso a las bolsas plasticas")
    await ctx.send(f"3) Almacenamiento: Puedes guardar un grupo de cosas en las bolsas de plastico y tener una mejor organizacion")
    await ctx.send(f"4) Comprar cosas: Utiliza las bolsas para llevar tus compras en ellas")

@bot.command()
async def eco_tips(ctx):
    await ctx.send(f"Aqui tienes unos tips para reducir la contaminacion")
    await ctx.send(f"1) Usa transporte sostenible: Elige caminar, andar en bicicleta, o usa el transporte publico en vez de viajar en auto")
    await ctx.send(f"2) Participa en actividades de limpieza: Participa en grupos para limpiar playas, parques o plazas, y espacios publicos")
    await ctx.send(f"3) Compra productos ecologicos: Evita comprar aerosoles que contaminen, compra productos con certificacion ecologica, intenta comprar productos que no contaminen su uso y cuando lo desechas")

#--------ideas--------
#------------✓------------
#Reutilización eficaz de las bolsas de plástico y bolsas reutilizables ✓, ✓
#Mencione grupos sin fines de lucro que busquen ayuda para disminuir la contaminación ✓, ✓
#Mencionar una serie de pasos o tips sencillos para reducir la contaminación ✓, ✓

#------------✕------------
#Tip de energías renovables ✕
#Siembra de árboles en el hogar ✕
#Mencionar una lista de 5 o más de los productos más desechados por las personas en un ranking mundial ✕



#--------BOT KEY--------
bot.run("")
