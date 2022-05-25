from unicodedata import name
import interactions
from dicts import *
import random
import aiohttp
from Config import Cload, server_data, Csave

token = open("token.txt").readline()
bot = interactions.Client(token=token, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT)
version = "v"+"1"

@bot.event
async def on_ready():
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
    for guild in bot.guilds:
        server_data[str(guild.id)] = Cload(guild)
    interactions.ClientPresence(activities=[interactions.PresenceActivity(name=f"{version}", url="https://twitch.tv/Morgandri1", type =interactions.PresenceActivityType.STREAMING)])

@bot.command(name="debug", description="shows debug info")
async def debug(ctx: interactions.CommandContext):
    """shows bot info"""
    servers = str(len(bot.guilds))
    await ctx.send(f"""
i'm registered to {servers} guilds!
ping is {(int)(bot.latency * 1000)}ms
made with ❤️ by Morgandri1
    """)
    return

@bot.command(
    name="animal", 
    description="sends an animal picture!", 
    options= [
        interactions.Option(
            name="type",
            description="which animal would you like?",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Duck", value="duck"), 
                interactions.Choice(name="Otter", value="otter"), 
                interactions.Choice(name="Dog", value="dog"), 
                interactions.Choice(name="Cat", value="cat"),
            ],
        ),
    ],
)
async def animals(ctx: interactions.CommandContext, type: str):
    if type == "duck":
        index = random.randrange(0, len(duck_pics))
        embed = interactions.Embed(title="Duck", description="a picture of a Duck")
        embed.set_image(url=duck_pics[index])
        await ctx.send(embeds=embed)
    elif type == "otter":
        index = random.randrange(0, len(otter_pics))
        embed = interactions.Embed(title="Otter", description="a picture of an Otter")
        embed.set_image(url=otter_pics[index])
        await ctx.send(embeds=embed)
    elif type == "cat":
        index = random.randrange(0, len(cat_pics))
        embed = interactions.Embed(title="Cat", description="a picture of a Cat")
        embed.set_image(url=cat_pics[index])
        await ctx.send(embeds=embed)
    elif type == "dog":
        index = random.randrange(0, len(dog_pics))
        embed = interactions.Embed(title="Dog", description="a picture of a Dog")
        embed.set_image(url=dog_pics[index])
        await ctx.send(embeds=embed)

@bot.command(name="meme", description="sends a meme from r/memes")
async def memes(ctx: interactions.CommandContext):
    """sends a meme"""
    embed = interactions.Embed(title="here's a meme", description="from r/memes")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 50)]['data']['url'])
            await ctx.send(embeds=embed)

@bot.command(
    name="roast", 
    description="roasts a member", 
    options = [
        interactions.Option(
        name="member",
        description="which member would you like to roast?",
        type=interactions.OptionType.USER,
        required=True,
        )
    ]
)
async def roast(ctx: interactions.CommandContext, member: str):
    """roast's the mentioned member"""
    roasts = [
        f"{member.mention}'s GPA may be high but the number of bitches on their dick is low",
        f"I would roast {member.mention}, but my mom said I shouldnt burn trash",
        f"I wish I could meet {member.mention} again and walk away this time",
        f"whoever told {member.mention} to be themselves was lying",
        f"sorry i can't think of an insult dumb enough for {member.mention} to understand",
        f"i would call {member.mention} an idiot but that would be an insult to stupid people",
        f"No breath mint can obscure the sheer stench of the bullshit that just came out of {member.mention}'s mouth"
    ]
    index = random.randrange(0, len(roasts))
    await ctx.send(roasts[index])

@bot.command(name="joke", description="sends a dad joke")
async def joke(ctx: interactions.CommandContext):
    index = random.randrange(0, len(jokes))
    await ctx.send(jokes[index])

@bot.command(name="coin", description="flips a coin")
async def coin(ctx: interactions.CommandContext):
    """flips a coin"""
    flip = [
        "tails",
        "heads",
        "tails",
        "heads",
        "tails",
        "heads",
        "tails",
        "heads",
        "tails",
        "heads",
        "tails",
        "heads"        
    ]
    index = random.randrange(0, len(flip))
    await ctx.send(flip[index])

@bot.command(
    name="kick", 
    description="kicks a member", 
    default_member_permissions=interactions.Permissions.KICK_MEMBERS,
    options = [
        interactions.Option(
        name="member",
        description="which member would you like to kick?",
        type=interactions.OptionType.USER,
        required=True,
        )
    ]
)
async def kick(ctx: interactions.CommandContext, member: interactions.Member):
    """roast's the mentioned member"""
    await member.kick(guild_id=int(ctx.guild_id))
    await ctx.send(f'User {member.mention} has been kicked')

@bot.command(
    name="ban", 
    description="bans a member", 
    default_member_permissions=interactions.Permissions.BAN_MEMBERS,
    options = [
        interactions.Option(
        name="member",
        description="which member would you like to ban?",
        type=interactions.OptionType.USER,
        required=True,
        )
    ]
)
async def ban(ctx: interactions.CommandContext, member: interactions.Member):
    """roast's the mentioned member"""
    await member.ban(member)
    await ctx.send(f'User {member.mention} has been banned')

@bot.command(
    name="number",
    description="picks between two random numbers",
    options=[
        interactions.Option(
            name="first_number",
            description="the first number in the range",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
        interactions.Option(
            name="second_number",
            description="the first number in the range",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def number(ctx, first_number, second_number):
    """picks a number. ex: .number 1 10"""
    if first_number is None or second_number is None:
        await ctx.send("must have 2 values")
    if first_number == second_number:
        await ctx.send("must have 2 different numbers")
    rand = int(random.randint(first_number-1, second_number-1))
    await ctx.send(f"picked {rand} from {first_number}-{second_number}")

@bot.command(
            name="poll",
            description="creates a poll for users to vote on!",
            options=[
                interactions.Option(
                    name="text",
                    description="what would you like the poll to say?",
                    type=interactions.OptionType.STRING,
                    required=True
                )
            ]
)
async def poll(ctx, text: str()):
    """creates a poll"""
    m = await ctx.send(f"{text}")
    await m.create_reaction("⬆️")
    await m.create_reaction("⬇️")  

@bot.command(
            name="config",
            description="allows admins to configure certain systems of the bot *make sure to copy the ID of any object*",
            default_member_permissions=interactions.Permissions.ADMINISTRATOR,
            options=[
                interactions.Option(
                    name="config",
                    description="which system would you like to change?",
                    type=interactions.OptionType.STRING,
                    required=True,
                    choices=[
                        interactions.Choice(name="mute role", value="MR"), 
                        interactions.Choice(name="welcome message", value="WM"), 
                        interactions.Choice(name="welcome channel", value="WC"), 
                        interactions.Choice(name="announcement channel", value="AC"),
                        interactions.Choice(name="people not to roast", value="pussies"),
                        interactions.Choice(name="filter", value="filter"),
                        interactions.Choice(name="join role", value="JR"),
                        interactions.Choice(name="public role", value="PR"),
                        interactions.Choice(name="leave message", value="LM")
                    ],
                ),
                interactions.Option(
                    name="value",
                    description="what is the new value you'd like to associate? (for color, input anything)",
                    type=interactions.OptionType.STRING,
                    required=True,            
                )
            ],
)
async def config(ctx, config: str(), value: str()):
    """allows admins to configure certain systems of the bot"""
    if config == "MR":
        await ctx.get_guild()
        if not value.isdigit():
            await ctx.send('integer not passed')
            return
        server_data[ctx.guild.id]['mute_role'] = int(value)
        Csave()
        await ctx.send(f"Set the mute role to id <@&{value}>")
        return
    elif config == "WM":
        await ctx.get_guild()
        msg = value
        data = server_data[ctx.guild.id]['join_message']
        if data != -1:
            await ctx.send(f"you already have a message set! it is currently ``{data}``, but you're changing it to ``{value}``", ephermal=True)
            pass
        server_data[ctx.guild.id]["join_message"] = str(msg)
        Csave()
        await ctx.send("set welcome message.")
        return
    elif config == "WC":
        await ctx.get_guild()
        channel = value
        data = server_data[ctx.guild.id]["Welcome"]
        if data != -1 and data != value:
            await ctx.send("you already have a Welcome channel set! make sure its the right one!", ephermal=True)
            pass
        if data == value:
            await ctx.send("that's already your welcome channel!", ephermal=True)
            pass
        server_data[ctx.guild.id]['Welcome'] = int(channel)
        Csave()
        await ctx.send("set your welcome channel.")
        return
    elif config == "AC":
        await ctx.get_guild()
        channel = value
        data = server_data[ctx.guild.id]["announcement"]
        if data != -1:
            await ctx.send("you have already set an announcement channel. use ``.config clear announcment`` to reset it.")
        else:
            server_data[ctx.guild.id]['announcement'] = int(channel)
            Csave()
            await ctx.send("added an announcement channel.")
        return
    elif config == "pussies":
        await ctx.get_guild()
        if not value.isdigit():
            await ctx.send('integer not passed')
            return
        server_data[ctx.guild.id]['pussies'].append(value)
        Csave()
        await ctx.send(f"Added <@{value}> to the list of pussies")
        return
    elif config == "filter":
        await ctx.get_guild()
        filters = server_data[ctx.guild.id]['filter']
        if filter in filters:
            await ctx.send("already added to the list of filters")
            return
        filters.append(value)
        Csave()
        await ctx.send("appended the filter list")
        return  
    elif config == "JR":
        await ctx.get_guild()
        roleID = int(value)
        data = server_data[ctx.guild.id]['join_role']
        if data != -1:
            await ctx.send("you already have a join role set!")
        else:
            server_data[ctx.guild.id]['join_role'] = int(roleID)
            Csave()
            await ctx.send("set your join role.")
        return
    elif config == "PR":
        await ctx.get_guild()
        roleID = int(value)
        server_data[ctx.guild.id]['publicroles'] = int(roleID)
        Csave()
        await ctx.send("added an opt role.")
        return
    elif config == "LM":
        await ctx.get_guild()
        msg = value
        data = server_data[ctx.guild.id]['leave_message']
        if data != -1:
            await ctx.send(f"you already have a message set! it is currently ``{data}``")
        else:
            server_data[ctx.guild.id]["leave_message"] = str(msg)
            Csave()
            await ctx.send("set leave message.")
        return

@bot.command(
    name="mute",
    description="mutes a user",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
    options=[
        interactions.Option(
        name="member",
        description="which member would you like to ban?",
        type=interactions.OptionType.USER,
        required=True,
        )
    ],
)
async def mute(ctx, member):
    """allows mods to mute a user"""
    await ctx.get_guild()
    userIn = member
    roleID = int(server_data[ctx.guild.id]['mute_role'])
    if roleID == -1:
        await ctx.send("You have not set a mute role!")
        return
    await member.add_role(roleID, ctx.guild.id)
    await ctx.send(f"Muted {userIn}") 
    return

@bot.command(
    name="unmute",
    description="unmutes a user",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
    options=[
        interactions.Option(
        name="member",
        description="which member would you like to ban?",
        type=interactions.OptionType.USER,
        required=True,
        )
    ],
)
async def unmute(ctx, member):
    """allows mods to unmute a user"""
    await ctx.get_guild()
    roleID = int(server_data[ctx.guild.id]['mute_role'])
    if roleID == -1:
        await ctx.send("You have not set a mute role!")
        return
    await member.remove_role(roleID, ctx.guild.id)
    await ctx.send(f"Unmuted {member}")
    return

# @bot.command(
#     name="roll",
#     description="rolls dice",

# )
# async def roll():
#     """"""

@bot.command(
    name="math",
    description="helps you do math",
    options=[
        interactions.Option(
            name="type",
            description="which type of math would you like to do?",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="addition", value="add"),
                interactions.Choice(name="subtraction",value="minus"),
                interactions.Choice(name="multiply",value="x"),
                interactions.Choice(name="divide",value="div"),
            ],
        ),
        interactions.Option(
            name="first_number",
            description="x",
            type=interactions.OptionType.INTEGER,
            required=True
        ),
        interactions.Option(
            name="second_number",
            description="x",
            type=interactions.OptionType.INTEGER,
            required=True
        ),
    ],
)
async def math(ctx, type, first_number: int(), second_number: int()):
    if type == "add":
        await ctx.send(f"``{first_number} + {second_number} = {first_number+second_number}``", ephemeral=True)
    if type == "minus":
        await ctx.send(f"``{first_number} - {second_number} = {first_number-second_number}``", ephemeral=True)
    if type == "x":
        await ctx.send(f"``{first_number} x {second_number} = {first_number*second_number}``", ephemeral=True)
    if type == "div":
        await ctx.send(f"``{first_number} ÷ {second_number} = {first_number/second_number}``", ephemeral=True)
    return
        

bot.start()
