import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import selenium.webdriver as webdriver


bot = commands.Bot("%")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(pass_context=True)
async def luca(ctx):
    await bot.say("Kanker")

bot.run("Mzk2MjUwNzY1MTI5NDE2NzA4.Deg_6A.NdjUG1wHUsogDdAX9K9aUPJguI0")



    
    
