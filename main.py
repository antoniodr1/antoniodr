import discord
from discord.ext import commands

intents = discord.Intents.default()  # Creates a default set of intents
intents.message_content = True  # Allows access to message content

client = commands.Bot(command_prefix="!!", intents=intents)

@client.event
async def on_ready():
    print("The bot is online")

@client.command()
async def send(ctx, *, message: str):
    user_message = await ctx.send(message)  # Sending the bot's response
    await ctx.message.delete()  # Deleting the user's message

@client.event
async def on_message(message):
    if "Hello" in message.content:
        # Tagga @goldie_1227 quando qualcuno scrive Hello
        goldie = discord.utils.get(message.guild.members, name="goldie_1227")
        if goldie:
            await message.channel.send(f"Better if you tag {goldie.mention}")
    await client.process_commands(message)

client.run("MTEyNTAzNTA5MzQ2ODExOTE0MA.GHD76U.bQf6lbdpIRGKSI7Elwc7VdSEW-nGeJoGFSlz1c")
