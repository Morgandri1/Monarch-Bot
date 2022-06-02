import interactions
from ext import *

token = open("token.txt").readline()
bot = interactions.Client(token=token, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT)
version = 1

print(f"""
         __  __                            _     
        |  \/  |                          | |    
        | \  / | ___  _ __   __ _ _ __ ___| |__  
        | |\/| |/ _ \| '_ \ / _` | '__/ __| '_ \ 
        | |  | | (_) | | | | (_| | | | (__| | | |
        |_|  |_|\___/|_| |_|\__,_|_|  \___|_| |_|    {version} 
            
                Logged in and ready
            made with ❤️  by Morgandri1
""")
for cog in initial_extentions:
    bot.load(cog)
bot.start()