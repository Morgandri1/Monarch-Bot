import interactions

class moderation(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(
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

    @interactions.extension_command(
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

def setup(client):
    moderation(client) 
