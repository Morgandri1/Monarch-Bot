from Config import Cload, server_data, Csave
import interactions

class events():
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_listener
    async def on_ready(self):
        for guild in self.bot.guilds:
            server_data[str(guild.id)] = Cload(guild)

    @interactions.extension_listener
    async def on_member_join(self, member):
        await member.get_guild()
        people = len(server.member_count)
        server = member.guild
        global channel
        channel = self.bot.get_channel(server_data[server.id]['Welcome'])
        if server_data[member.server.id]['join_message'] == -1:
            try:
                to_send = f'Welcome {member.mention} to {server.name}! member count: {people}'
                await channel.send(to_send)
            except AttributeError:
                print("no welcome channel found")
        if server_data[server.id]['join_role'] != -1:
                roleID = server_data[server.id]["join_role"]
                await member.add_roles(roleID, member.server.id)
        else:
            to_send = server_data[server.id]['join_message']
            await channel.send(to_send)
        return

    @interactions.extension_listener
    async def on_member_remove(self, member):
        await member.get_guild
        guild = member.guild
        people = len(guild.member_count)
        global channel
        channel = self.bot.get_channel(server_data[guild.id]['Welcome'])
        if server_data[guild.id]['leave_message'] == -1:
            try:
                to_send = f'dang. {member.mention} has left. this is so sad. alexa, play despacito. member count: {people}'
                await channel.send(to_send)
            except AttributeError:
                return
        else:
            to_send = server_data[guild.id]['leave_message']
            await channel.send(to_send)
        return

def setup(client):
    events(client) 
