import interactions
from Config import *

class tools(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client
        
    @interactions.extension_command(
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

    @interactions.extension_command(
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

    @interactions.extension_command(
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

    @interactions.extension_command(
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

    @interactions.extension_command(
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