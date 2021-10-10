import discord
import oauth2client
import os
import time
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
token = "</>"
#
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
guildid = 777145760219004938
sycureid = 756302455393746996
guildc = 777145760219004939
sycurec = 773688893291495485
schannel = 812153914325467146
trigger = 0

def write(data, filename):
    with open(filename,"w") as f:
        print(data)
        json.dump(data,f,indent=4)
        f.close()

file = input("File:")


def load():
    with open(file,"r") as f:
        data = json.load(f)
        print("Loading...")
        data2 = data["settings"]
        data3 = data2[0]
        delay = data3["delay"]
        token = data3["token"]
        message = data3["message"]
        serverid = data3["serverid"]
        keyword = data3["keyword"]
        access = data3["key"]
        print("Key: {}".format(access))
        trigger = 0
        f.close()
        return delay,token,message,serverid,keyword,access
delay2,token,message,serverid,keyword,access = load()
serverid = int(serverid)
delay2 = float(delay2)


@client.event
async def on_message(message):
    Content = message.content
    content2 = Content[6:]
    #print("Message detected")
    if message.content.startswith("token"):
        with open(fi,"r+") as fi:
            json_obj = json.load(fi)
            json2 = json_obj["settings"]
            json3 = json2[0]
            Token = content2
            json3["token"] = Token
            f.close()
            write(json_obj,file)
    if message.content.startswith("load"):
        trigger = 1        
        channel = message.channel
        user = message.author
        server = client.get_guild(guildid)
        content = message.content
    if content == "Test":
        time.sleep(delay2)
        await channel.send("Test message detected.")

@client.event
async def on_guild_channel_create(channel):
    print("Channel detected")
    ticketname = channel.name
    Guild = channel.guild
    output = client.get_channel(schannel)
    #print(serverid,type(serverid))
    if Guild.id == serverid:
        #print("Guild detected")
        if keyword in ticketname:
            time.sleep(delay2)
            await channel.send("{}".format(message))



client.run(token,bot=False)
