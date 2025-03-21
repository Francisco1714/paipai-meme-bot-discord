import discord
import requests
import json
import os
from dotenv import load_dotenv  # Importar dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token de las variables de entorno
TOKEN = os.getenv("Paipai_BOT")

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'¡Conectado como {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

client = MyClient(intents=intents)
client.run(TOKEN)  # Se usa la variable segura desde .env

