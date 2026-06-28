import discord
import asyncio

from datetime import datetime

LOG_CHANNEL_ID = 1520546055924744434


class CloseModal(discord.ui.Modal):

    def __init__(self):
        super().__init__(title="Fechar Ticket")

        self.motivo = discord.ui.TextInput(
            label="Motivo do fechamento",
            placeholder="Ex: Resolvido, Inatividade, Dúvida sanada...",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=300
        )

        self.add_item(self.motivo)

    async def on_submit(self, interaction: discord.Interaction):

        log = interaction.guild.get_channel(LOG_CHANNEL_ID)

        agora = datetime.now()

        embed = discord.Embed(
            title="📜 Ticket Fechado",
            color=0xC1121F,
            timestamp=agora
        )

        embed.set_thumbnail(
            url=interaction.user.display_avatar.url
        )

        embed.add_field(
            name="👤 Staff que fechou",
            value=f"{interaction.user.mention}\n`{interaction.user.id}`",
            inline=False
        )

        embed.add_field(
            name="📁 Ticket",
            value=interaction.channel.name,
            inline=False
        )

        embed.add_field(
            name="📝 Motivo",
            value=self.motivo.value,
            inline=False
        )

        embed.add_field(
            name="📅 Data",
            value=agora.strftime("%d/%m/%Y"),
            inline=True
        )

        embed.add_field(
            name="🕒 Horário",
            value=agora.strftime("%H:%M:%S"),
            inline=True
        )

        embed.set_footer(
            text="Vivência RP | França #100 • Sistema de Tickets"
        )

        if log:
            await log.send(embed=embed)

        await interaction.response.send_message(
            "🔒 Ticket será fechado em 3 segundos...",
            ephemeral=True
        )

        await asyncio.sleep(3)

        await interaction.channel.delete(
            reason=f"Fechado por {interaction.user}"
        )