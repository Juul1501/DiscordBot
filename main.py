import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys


bot = commands.Bot(";")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(pass_context=True)
async def search(ctx, arg1):
    get_result(arg1)
    imgurl = links
    await bot.say("imgurl")





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
