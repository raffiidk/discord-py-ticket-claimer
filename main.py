import discord
import os
import time
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
token = "NjUyMDY4NzE0MDU3MDM5ODcz.YHCJvg.72QmL95tfejmB1wXBeYR0rJpFqY"
creds = ServiceAccountCredentials.from_json_keyfile_name("nexchange-bfdbbd41e03d.json",scope)
client = gspread.authorize(creds)
sheet = client.open("Keys").sheet1
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

file = "settings.json"

def load():
    with open("settings.json","r") as f:
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
        #Settings.json is required in parent dir
delay2,token,message,serverid,keyword,access = load()
serverid = int(serverid)
delay2 = float(delay2)
#@client.event
#async def on_ready():
    #time.sleep(2)
    #keys = sheet.col_values(1)
    #print(keys)
    #if access in keys:
        #print('''Self-bot auto ticket claimer:
        
        #Your token is being used.
        #Follow guides on how to properly utilise this bot and avoid a discord ban.
        #By running this software, you are agreeing to the terms of service found in the Zeppelin Software discord server.
        #''')
    #else:
        #print("Key could not be validated.")
        #time.sleep(5)
        #exit()
#Authorisation - requires google sheets api keys

@client.event
async def on_message(message):
    Content = message.content
    content2 = Content[6:]
    #print("Message detected")
    if message.content.startswith("token"):
        with open(file,"r+") as f:
            json_obj = json.load(f)
            json2 = json_obj["settings"]
            json3 = json2[0]
            Token = content2
            json3["token"] = Token
            f.close()
            write(json_obj,file)
    if message.content.startswith("load"):
        trigger = 1
    if message.content.startswith("reset"):
        with open("settings.json","w") as f:
            f.write('''
                {
                    "settings": [
                    {
                        "delay": "0",
                        "token": "NjUyMDY4NzE0MDU3MDM5ODcz.YHCJvg.72QmL95tfejmB1wXBeYR0rJpFqY"
                    }
                ]
            }
''')
            f.close()            
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
            await output.send("Channel created")
            time.sleep(delay2)
            await channel.send("{}".format(message))



client.run(token,bot=False)
