from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import os
import urllib.request
import string
import random
import time

import requests

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='insta!')

browser1 = webdriver.Firefox()

contas = [[]]

def login():
    global contas

    for i in contas:

        i[2].get('https://www.instagram.com/')

        time.sleep(5)

        i[2].find_element_by_name("username").clear()
        i[2].find_element_by_name("username").send_keys(i[0])
        i[2].find_element_by_name("password").clear()
        i[2].find_element_by_name("password").send_keys(i[1])
        i[2].find_element_by_name("password").send_keys(Keys.RETURN)

        time.sleep(2)

    print("All accounts are logged in.")

async def ban_account(ctx, account_to_ban, account_to_use, tentativas):

    try:
        if tentativas == 5:
            ctx.send('The bot couldnt finish the report within 5 retries, try again.')
            return

        account_to_use[2].get('https://www.instagram.com/' + account_to_ban)

        account_to_use[2].implicitly_wait(5)

        nome = account_to_use[2].find_element_by_class_name("rhpdm").text
        bio_help = account_to_use[2].find_element_by_class_name("-vDIg")
        try:
            bio = bio_help.find_element_by_tag_name("span").text
        except:
            bio = 0
        image_link = account_to_use[2].find_elements_by_tag_name('img')[0].get_attribute("src")
        try:
            link = account_to_use[2].find_element_by_class_name("yLUwa").text
        except:
            link = 0

        urllib.request.urlretrieve(image_link, "images/" + account_to_ban + ".jpg")

        account_to_use[2].implicitly_wait(5)

        account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()

        account_to_use[2].implicitly_wait(2)

        account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/a').click()

        account_to_use[2].implicitly_wait(2)

        rand_letters = ''.join(random.choice(string.ascii_lowercase) for i in range(2))

        username = account_to_ban + rand_letters + "7"

        account_to_use[2].find_element_by_id("pepUsername").clear()
        account_to_use[2].find_element_by_id("pepUsername").send_keys(username)

        account_to_use[2].find_element_by_id("pepName").clear()

        if(link != 0):
            account_to_use[2].find_element_by_id("pepWebsite").clear()
            account_to_use[2].find_element_by_id("pepWebsite").send_keys(link)
        else:
            account_to_use[2].find_element_by_id("pepWebsite").clear()

        if(bio != 0):
            account_to_use[2].find_element_by_id("pepBio").clear()
            account_to_use[2].find_element_by_id("pepBio").send_keys(bio)
        else:
            account_to_use[2].find_element_by_id("pepBio").clear()

        submit_help = account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div')
        submit_help.find_element_by_tag_name("button").click()
        time.sleep(2)

        foto = account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[2]/div/form/input')
        foto.send_keys(os.path.abspath("images/" + account_to_ban + ".jpg"))

        time.sleep(2)

        account_to_use[2].get('https://www.instagram.com/' + account_to_ban)

        account_to_use[2].implicitly_wait(5)

        account_to_use[2].find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/button').click()

        account_to_use[2].implicitly_wait(2)

        account_to_use[2].find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[3]').click()

        account_to_use[2].implicitly_wait(2)

        account_to_use[2].find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()

        account_to_use[2].implicitly_wait(2)

        account_to_use[2].find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()

        time.sleep(2)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.TAB) 

        time.sleep(0.25)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.TAB) 

        time.sleep(0.25)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.TAB) 

        time.sleep(0.25)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.TAB) 

        time.sleep(0.25)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.RETURN) 

        time.sleep(1)

        account_to_use[2].find_element_by_tag_name('body').send_keys(Keys.RETURN)
        
        account_to_use[2].find_element_by_xpath('//*[@id="igCoreRadioButtontag-0"]').click()

        account_to_use[2].implicitly_wait(2)

        account_to_use[2].find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[6]/button').click()

        await ctx.send("Reported already dones")
    except: 

        await ban_account(ctx, account_to_ban, account_to_use, tentativas + 1)

async def check_account(ctx, account_to_check):

    request = requests.get('https://www.instagram.com/' + account_to_check)

    if request.status_code == 200:
        await ctx.send("Account still up.")
    else:
        await ctx.send("Account got banned.")

@bot.command()
async def check(ctx, arg):

    await check_account(ctx, arg)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    login()

@bot.command()
async def ban(ctx, *args):
    global contas

    argumentos = list(args)

    print(argumentos)

    account_to_ban = argumentos[0]
    account_to_use = contas[int(argumentos[1]) - 1]

    await ban_account(ctx, account_to_ban, account_to_use, 0)

bot.run('')
