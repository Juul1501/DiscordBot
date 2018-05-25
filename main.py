import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

bot = commands.Bot("%")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(pass_context=True)
async def cookie(ctx):
    await bot.say("koekje")

bot.run("Mzk2MjUwNzY1MTI5NDE2NzA4.Deg_6A.NdjUG1wHUsogDdAX9K9aUPJguI0")



    
    
