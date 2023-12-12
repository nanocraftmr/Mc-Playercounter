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
        if 'list' in data['players'] and data['players']['list']:
            player_names = ', '.join(data['players']['list'])
            # Discord has a limit of 128 characters for custom statuses
            if len(player_names) > 128:
                player_names = player_names[:125] + "..."
        else:
            player_names = "Nobody Online!"

        # Define the new channel name, customize it as needed
        new_channel_name = f'Minecraft Online: {players_online}'

        # Get the channel object using the channel ID
        channel = client.get_channel(CHANNEL_ID)

        # Update the channel name
        if channel and channel.name != new_channel_name:
            try:
                await channel.edit(name=new_channel_name)
                print(f'Updated the channel name to "{new_channel_name}"')
            except Exception as e:
                print(f'Failed to update channel name: {e}')

        # Update the bot's Playing status with the list of player names or the message "Nobody Online!"
        activity = discord.Game(name=player_names)
        await client.change_presence(status=discord.Status.online, activity=activity)

        # Wait before the next check
        await asyncio.sleep(60*10)  # Update every 10 minutes


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.loop.create_task(update_minecraft_status())

client.run(TOKEN)
