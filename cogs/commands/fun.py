import interactions
import random
from dicts import *
import aiohttp

class fun(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(name="meme", description="sends a meme from r/memes")
    async def memes(self, ctx: interactions.CommandContext):
        """sends a meme"""
        embed = interactions.Embed(title="here's a meme", description="from r/memes")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 50)]['data']['url'])
                await ctx.send(embeds=embed)

    @interactions.extension_command(
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
    async def roast(self, ctx: interactions.CommandContext, member: str):
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

    @interactions.extension_command(name="joke", description="sends a dad joke")
    async def joke(self, ctx: interactions.CommandContext):
        index = random.randrange(0, len(jokes))
        await ctx.send(jokes[index])

    @interactions.extension_command(
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
    async def animals(self, ctx: interactions.CommandContext, type: str):
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

def setup(client):
    fun(client) 