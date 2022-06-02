import interactions
import random

class chance(interactions.Extension):
    """"""
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(name="coin", description="flips a coin")
    async def coin(self, ctx: interactions.CommandContext):
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

    @interactions.extension_command(
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

def setup(client):
    chance(client) 
