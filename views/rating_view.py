import discord

LOG_AVALIACAO = 1520546055924744434  # coloque o ID do canal de avaliações


class RatingView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    async def avaliar(self, interaction: discord.Interaction, nota: int):
        canal = interaction.guild.get_channel(LOG_AVALIACAO)

        embed = discord.Embed(
            title="⭐ Nova Avaliação",
            color=0xFFD700
        )

        embed.add_field(
            name="Usuário",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Nota",
            value="⭐" * nota,
            inline=False
        )

        if canal:
            await canal.send(embed=embed)

        await interaction.response.send_message(
            f"Obrigado pela avaliação! {'⭐' * nota}",
            ephemeral=True
        )

        self.stop()

    @discord.ui.button(label="⭐", style=discord.ButtonStyle.secondary)
    async def um(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.avaliar(interaction, 1)

    @discord.ui.button(label="⭐⭐", style=discord.ButtonStyle.secondary)
    async def dois(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.avaliar(interaction, 2)

    @discord.ui.button(label="⭐⭐⭐", style=discord.ButtonStyle.primary)
    async def tres(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.avaliar(interaction, 3)

    @discord.ui.button(label="⭐⭐⭐⭐", style=discord.ButtonStyle.success)
    async def quatro(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.avaliar(interaction, 4)

    @discord.ui.button(label="⭐⭐⭐⭐⭐", style=discord.ButtonStyle.success)
    async def cinco(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.avaliar(interaction, 5)