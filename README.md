# Minecraft Player Counter Discord Bot

This bot updates a Discord channel's name with the current player count from a Minecraft server using the mcsrvstat.us API.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Latest version of Python 3
- Discord account, created a bot on the Discord Developer Portal
- `.env` file containing your bot's token, the Discord channel ID, and Minecraft server address

## Installation

To install the required Python packages, run the following command:
`pip install -r requirements.txt`


## Configuration

1. Create a `.env` file in the root directory with the following variables:
```
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_discord_channel_id
MINECRAFT_SERVER=your_minecraft_server_address
```

Replace `your_discord_bot_token` with your Discord bot's token, `your_discord_channel_id` with the ID of the channel you want to update, and `your_minecraft_server_address` with the address of your Minecraft server.

## Usage

Run the bot using the following command: `python main.py`

The bot will update the specified Discord channel's name with the current player count every 10 minutes.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is [MIT licensed](https://opensource.org/licenses/MIT).
