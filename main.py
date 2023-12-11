import discord
import asyncio
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Channel ID should be an integer
MINECRAFT_SERVER = os.getenv('MINECRAFT_SERVER')

# Set up intents
intents = discord.Intents.default()
intents.guilds = True

client = discord.Client(intents=intents)

async def update_minecraft_status():
    while True:
        # Fetch server status from the Minecraft API
        response = requests.get(f'https://api.mcsrvstat.us/2/{MINECRAFT_SERVER}')
        data = response.json()

        players_online = data['players']['online']
        # Define the new channel name, customize it as needed
        new_channel_name = f'Minecraft Online: {players_online}'

        # Get the channel object using the channel ID
        channel = client.get_channel(CHANNEL_ID)

        # Update the channel name
        if channel and channel.name != new_channel_name:
            await channel.edit(name=new_channel_name)
            print(f'Updated the channel name to "{new_channel_name}"')

        # Wait before the next check
        await asyncio.sleep(60*10)  # Update every 10 minutes

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.loop.create_task(update_minecraft_status())

client.run(TOKEN)
