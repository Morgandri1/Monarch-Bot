import interactions

class TestCommand(interactions.Extension):
    def __init__(self, client):
      self.bot: interactions.Client = client

    @interactions.extension_command(name="debug", description="shows debug info")
    async def debug(self, ctx: interactions.CommandContext):
        """shows bot info"""
        servers = str(len(self.bot.guilds))
        await ctx.send(f"i'm registered to {servers} guilds!\nping is {(int)(self.bot.latency * 1000)}ms\nmade with ❤️ by Morgandri1")
        return

def setup(client):
    TestCommand(client)