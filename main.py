import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio

import urllib
import urllib.request

bot = commands.Bot(";")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(pass_context=True)
async def search(ctx, *, query):
    channel = ctx.message.channel                                           #Dit is de channel waarin de text post is gemaakt
    if not get_result_bing(query):                                          #Als bing kut doet...
        get_result_google_thumb(query)                                      #doe dan google (al zijn dat alleen thumbnails)
    await bot.send_file(channel, "img.jpg", content=query)
    print ("search command used")

@bot.command(pass_context=True)
async def fn(ctx, *, query):
    channel = ctx.message.channel
    get_result_giphy(query)
    
    await bot.send_file(channel, "img.gif", content=query)
@bot.command(pass_context=True)
async def join(ctx): 
    author = ctx.message.author
    channel = author.voice_channel 
    voice = await bot.join_voice_channel(channel)
    player = bot.create_ffpmeg_player("./jesper.mp3")
    player.start()
    await VoiceClient.disconnect()




#Google Search
def get_result_google_thumb(search_term):
    try:    
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' #Deze header zorgt dat google niet gaat klagen dat we een bot zijn

        headers={'User-Agent':user_agent,}                                  #Zet de header in elkaar
        url = "http://www.google.com/search?tbm=isch&q="\
         + search_term.replace(" ", "+")                                    #Vervang spaties met plus-tekens zodat google niet zeurt.

        request=urllib.request.Request(url,None,headers)                    
        response = urllib.request.urlopen(request)                          
        data = str(response.read())                                        
        image_url = data.split('<a href="/url?q=')[1].split("src=")[1].split('"')[1]    

        urllib.request.urlretrieve(image_url, "img.jpg")
        return True
    except Exception:
        return False
#bing search
def get_result_bing(search_term):
    try:    
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' 

        headers={'User-Agent':user_agent,}                                  
        url = "https://www.bing.com/images/search?q="\
            + search_term.replace(" ", "+")                                 

        request=urllib.request.Request(url,None,headers)                    
        response = urllib.request.urlopen(request)                          
        data = str(response.read())                                         
        with open('output.txt','w') as file:
            file.write(data)
        image_url = data.split(".jpg&quot;,&quot;turl")[1].split("&quot;:&quot;")[-1]+".jpg" 

        urllib.request.urlretrieve(image_url, "img.jpg")
        return True
    except Exception:
        return False
#giphy search 
def get_result_giphy(search_term):
    try:
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

        headers={'User-Agent':user_agent,}

        url = "https://giphy.com/search/"\
        + search_term.replace(" ", "-")

        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        
        data = str(response.read())
        with open('outputgiphy.txt','w') as file:
            file.write(data)

        image_url = data.split('<a class = "_gifImage_1mf53_41 _gifLink_1mf53_51')[1].split("src=")[1].split('"')[1]+".gif"

        urllib.request.urlretrieve(image_url, "img.gif")
        
        return True
    except Exception:
        return False

bot.run("Mzk2MjUwNzY1MTI5NDE2NzA4.Deg_6A.NdjUG1wHUsogDdAX9K9aUPJguI0")
