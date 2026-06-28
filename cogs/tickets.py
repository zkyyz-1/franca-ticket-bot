import discord
from discord.ext import commands
from discord import app_commands

from views.ticket_view import TicketView


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ticket",
        description="Envia o painel de tickets."
    )
    async def ticket(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🎫 CENTRAL DE ATENDIMENTO",
            description=(
                "🇫🇷 **Bem-vindo à Central de Atendimento da Vivência RP | França #100!**\n\n"

                "Abra um ticket selecionando uma categoria no menu abaixo.\n\n"

                "**📂 Categorias Disponíveis**\n\n"

                "🔰 **Recrutamento**\n"
                "> Deseja fazer parte da França? Abra um ticket e aguarde um recrutador.\n\n"

                "⚖️ **Denúncias**\n"
                "> Reporte jogadores ou membros anexando todas as provas.\n\n"

                "❓ **Dúvidas**\n"
                "> Tire dúvidas sobre a organização ou funcionamento.\n\n"

                "🔄 **Transferência**\n"
                "> Solicite sua transferência enviando todas as informações necessárias.\n\n"

                "━━━━━━━━━━━━━━━━━━━━━━\n"

                "**📜 Regras do Atendimento**\n"
                "• Seja educado com a equipe.\n"
                "• Explique tudo com detalhes.\n"
                "• Envie provas quando necessário.\n"
                "• Aguarde seu atendimento.\n\n"

                "⬇️ **Selecione uma categoria no menu abaixo para abrir seu ticket.**"
            ),
            color=0xC1121F
        )

        file = discord.File(
            "backup/assets/banner.png",
            filename="banner.png"
        )

        embed.set_image(
            url="attachment://banner.png"
        )

        embed.set_footer(
            text="Vivência RP | França #100 • Sistema Oficial de Atendimento"
        )

        await interaction.channel.send(
            embed=embed,
            file=file,
            view=TicketView()
        )

        await interaction.response.send_message(
            "✅ Painel enviado com sucesso.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Tickets(bot))