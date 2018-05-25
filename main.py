import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
<<<<<<< HEAD
=======
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

>>>>>>> b06638ceeee2bad9f5356eda910af4187ed0551d

bot = commands.Bot(";")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(pass_context=True)
<<<<<<< HEAD
async def cookie(ctx):
    await bot.say("koekje")
=======
async def search(ctx, arg1):
    get_result(arg1)
    imgurl = links
    await bot.say("imgurl")



>>>>>>> b06638ceeee2bad9f5356eda910af4187ed0551d


def get_result(search_term):
    url = "https://images.google.com/"
    browser = webdriver.Firefox()
    browser.get(url)
    search_box = browser.find_element_by_id("lst-ib")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    links = browser.find_element_by_xpath("//a")

    results = []

    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results
    
    


bot.run("Mzk2MjUwNzY1MTI5NDE2NzA4.Deg_6A.NdjUG1wHUsogDdAX9K9aUPJguI0")
