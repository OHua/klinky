import discord

from config import DISCORD_BOT_TOKEN


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


if __name__ == "__main__":
    # This example requires the 'message_content' intent.
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(DISCORD_BOT_TOKEN)
