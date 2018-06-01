import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import os.path
import urllib
import urllib.request

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

class Juulbot:

    def __init__(self, bot):
        self.voice_states = {}
        self.bot = bot

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    @commands.command(pass_context=True)
    async def search(self, ctx, *, query):
        channel = ctx.message.channel                                           #Dit is de channel waarin de text post is gemaakt
        if not get_result_bing(query):                                           #Als bing kut doet...
            get_result_google_thumb(query)                                      #doe dan google (al zijn dat alleen thumbnails)
        await bot.send_file(channel, "img.jpg", content=query)
        print ("search command used")

    @commands.command(pass_context=True)
    async def pl(self, ctx):
        channel = ctx.message.channel
        lijst = []
        files = os.listdir('./bin/')
        for name in files:
            lijst.append(name[:-4])
            print(lijst)
        await bot.send_message(channel,content=lijst)

    @commands.command(pass_context=True)
    async def p(self, ctx, query):

        state = self.get_voice_state(ctx.message.server)
        author = ctx.message.author
        channel = author.voice_channel
        if state.voice is None:
            state.voice = await bot.join_voice_channel(channel)
        player = state.voice.create_ffmpeg_player('./bin/'+query+'.mp3')
        player.start()



    #Google Search
def get_result_google_thumb(self, search_term):
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

bot = commands.Bot(command_prefix=commands.when_mentioned_or(";"), desciption='Juulbot')
bot.add_cog(Juulbot(bot))

@bot.event
async def on_ready():
    print("Bot online")


bot.run("Mzk2MjUwNzY1MTI5NDE2NzA4.Deg_6A.NdjUG1wHUsogDdAX9K9aUPJguI0")
