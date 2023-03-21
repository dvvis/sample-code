# bot.py
import os
import time
import threading
from twill.commands import *
from bs4 import BeautifulSoup
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
#join server
@client.event
async def on_ready():
    client.activity = discord.Game(name="!help")
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    #await client.change_presence(activity=discord.Game(name="help"))

#waw map checker
def waw():
    rotation = ["Airfield", "Asylum", "Makin Day", "Breach", "Battery", "Castle", "Cliffside", "Courtyard", "Dome", "Downfall", "Hangar", "Bonzai", "Subway", "Nightfire", "Outskirts", "Docks", "Revolution", "Roundhouse", "Corrosion", "Castle", "Makin", "Seelow", "Kneedeep", "Upheaval", "Dome"]
    maps = {
    "mp_airfield": "Airfield",
    "mp_asylum": "Asylum",
    "mp_makin_day": "Makin Day",
    "mp_bgate": "Breach",
    "mp_drum": "Battery",
    "mp_castle": "Castle",
    "mp_shrine": "Cliffside",
    "mp_courtyard": "Courtyard",
    "mp_dome": "Dome",
    "mp_downfall": "Downfall",
    "mp_hangar": "Hangar",
    "mp_kwai": "Bonzai",
    "mp_subway": "Subway",
    "mp_nachtfeuer": "Nightfire",
    "mp_outskirts": "Outskirts",
    "mp_docks": "Sub Pens",
    "mp_vodka": "Revolution",
    "mp_roundhouse": "Roundhouse",
    "mp_stalingrad": "Corrosion",
    "mp_makin": "Makin",
    "mp_seelow": "Seelow",
    "mp_kneedeep": "Kneedeep",
    "mp_suburban": "Upheaval",
    }
    browser.go("https://www.gametracker.com/server_info/107.182.231.48:28960/")
    page = browser.html.strip()
    soup = BeautifulSoup(page, 'html.parser')
    #pulls raw mp_mapname
    curr_map = soup.find(id='HTML_curr_map').string.strip()
    players = soup.find(id='HTML_num_players').string.strip()
    #converts mp_mapname to normal mapname
    mapname = maps[curr_map]
    curr_pos = rotation.index(mapname)
    if mapname == "Castle":
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext: " + str(rotation[6]) + ", " + str(rotation[7]) + ", " + str(rotation[8]) + " or " + str(rotation[20]) + ", " + str(rotation[21])+ ", " + str(rotation[22])
    if mapname == "Dome":
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext: " + str(rotation[9]) + ", " + str(rotation[10]) + ", " + str(rotation[11]) + " or " + str(rotation[0]) + ", " + str(rotation[1])+ ", " + str(rotation[2])
    if curr_pos == 22:
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext: " + str(rotation[23]).capitalize() + ", " + str(rotation[24]).capitalize() + ", " + str(rotation[0]).capitalize()
    if curr_pos == 23:
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext: " + str(rotation[24]).capitalize() + ", " + str(rotation[0]).capitalize() + ", " + str(rotation[1]).capitalize()
    else: 
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext: " + str(rotation[curr_pos + 1]).capitalize() + ", " + str(rotation[curr_pos + 2]).capitalize() + ", " + str(rotation[curr_pos + 3]).capitalize()  #"steam://rungameid/10090/+connect%107.182.231.48:28960" 

def wawfind(reqmap):
    rotation = ["airfield", "asylum", "makin day", "breach", "battery", "castle", "cliffside", "courtyard", "dome", "downfall", "hangar", "bonzai", "subway", "nightfire", "outskirts", "docks", "revolution", "roundhouse", "corrosion", "castle", "makin", "seelow", "kneedeep", "upheaval", "dome"]
    maps = {
    "mp_airfield": "Airfield",
    "mp_asylum": "Asylum",
    "mp_makin_day": "Makin Day",
    "mp_bgate": "Breach",
    "mp_drum": "Battery",
    "mp_castle": "Castle",
    "mp_shrine": "Cliffside",
    "mp_courtyard": "Courtyard",
    "mp_dome": "Dome",
    "mp_downfall": "Downfall",
    "mp_hangar": "Hangar",
    "mp_kwai": "Bonzai",
    "mp_subway": "Subway",
    "mp_nachtfeuer": "Nightfire",
    "mp_outskirts": "Outskirts",
    "mp_docks": "Sub Pens",
    "mp_vodka": "Revolution",
    "mp_roundhouse": "Roundhouse",
    "mp_stalingrad": "Corrosion",
    "mp_makin": "Makin",
    "mp_seelow": "Seelow",
    "mp_kneedeep": "Kneedeep",
    "mp_suburban": "Upheaval",
    }
    browser.go("https://www.gametracker.com/server_info/107.182.231.48:28960/")
    page = browser.html.strip()
    soup = BeautifulSoup(page, 'html.parser')
    #pulls raw mp_mapname & player count
    curr_map = soup.find(id='HTML_curr_map').string.strip()
    players = soup.find(id='HTML_num_players').string.strip()
    #converts mp_mapname to normal mapname
    mapname = maps[curr_map]
    curr_pos = rotation.index(mapname.lower())
    #returns next map
    #if reqmap[1] == "next":
    #    if curr_pos == 24:
    #        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext map: " + rotation[0].capitalize()
    #    else:
    #        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nNext map: " + rotation[curr_pos + 1].capitalize()
    req_pos = rotation.index(reqmap[1])
    ttm = (req_pos - curr_pos)
    # 2nd half of rotation for dome/castle
    if curr_pos > 8 and reqmap[1] == "dome":
        ttm = 24 - curr_pos
        if ttm * 13 <= 60:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(ttm * 13) + " minutes"
        else:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(divmod(ttm * 13, 60)[0]) + " hours and " + str(divmod(ttm * 13, 60)[1]) + " minutes"
    if curr_pos > 8 and curr_pos < 19 and reqmap[1] == "castle":  
        ttm = 19 - curr_pos
        if ttm * 13 <= 60:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(ttm * 13) + " minutes"
        else:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(divmod(ttm * 13, 60)[0]) + " hours and " + str(divmod(ttm * 13, 60)[1]) + " minutes"
    #if neg, gotta wrap around to beginning of array/rotation
    if req_pos < curr_pos:
        ttm = (25 - curr_pos) + req_pos
        if ttm * 13 <= 60:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(ttm * 13) + " minutes"
        else:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(divmod(ttm * 13, 60)[0]) + " hours and " + str(divmod(ttm * 13, 60)[1]) + " minutes"
    #checks for castle/dome since its in rotation twice
    if curr_pos == 5 or curr_pos == 8 or curr_pos == 9 or curr_pos == 24:
        return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\n" + "Check again in 10 mins for accurate time"
    else:        
        if ttm * 13 <= 60:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(ttm * 13) + " minutes"
        else:
            return "Map: " + mapname + "\nPlayers: " + players + "\n`\connect 107.182.231.48:28960`\nTime until " + reqmap[1].capitalize() + " ~" + str(divmod(ttm * 13, 60)[0]) + " hours and " + str(divmod(ttm * 13, 60)[1]) + " minutes"

#Message listener
@client.event
async def on_message(message):
    modmsg = message.content.lower()
    if message.author == client.user:
        return
    if modmsg == 'command' or modmsg == 'commands' or modmsg == 'help':
        response = "`Command`\n`waw`: Server stats\n`waw mapname`: Time until that map\n`a OR b`: decide that\n`flip that`: flips that"
        await message.channel.send(response)

    if modmsg == 'test that':
        response = "testing that"
        await message.channel.send(response)

    if modmsg == 'flip that':
        if random.randint(0, 100) <= 50:
            response = "yup"
        else:
            response = "nope"
        await message.channel.send(response)

    if message.content.find(" OR ") >= 0:
        choices = modmsg.split(" or ", 1)
        if random.randint(0, 100) <= 50:
            response = choices[0]
        else:
            response = choices[1]
        await message.channel.send(response)

    if modmsg.startswith('waw'):
        try:
            if modmsg == 'waw rotation':
                rotation = ["airfield", "asylum", "makin day", "breach", "battery", "castle", "cliffside", "courtyard", "dome", "downfall", "hangar", "bonzai", "subway", "nightfire", "outskirts", "docks", "revolution", "roundhouse", "corrosion", "castle", "makin", "seelow", "kneedeep", "upheaval", "dome"]
                await message.channel.send(rotation)
                return
            if modmsg == 'waw':
                response = waw()
                await message.channel.send(response)
            else:
                response = wawfind(modmsg.split('waw '))
                await message.channel.send(response)
        except:
            response = "Server down and/or you requested invalid map."
            await message.channel.send(response)
            
client.run(TOKEN)