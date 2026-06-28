import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

print("TOKEN carregado?", TOKEN is not None)

if TOKEN:
    print("Primeiros 5:", TOKEN[:5])
    print("Últimos 5:", TOKEN[-5:])
else:
    print("ERRO: TOKEN não encontrado no arquivo .env")
    exit()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot conectado como {bot.user}")


@bot.event
async def setup_hook():
    await bot.load_extension("cogs.tickets")


@bot.tree.command(name="ping", description="Verifica a latência do bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! {round(bot.latency * 1000)}ms",
        ephemeral=True
    )


bot.run(TOKEN)