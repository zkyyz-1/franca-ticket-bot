import discord
from discord.ui import View, Select

from views.manage_view import ManageView

CATEGORY_ID = 1490505207115943960


class TicketSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Recrutamento",
                emoji="🔰",
                description="Desejo entrar para a França."
            ),
            discord.SelectOption(
                label="Denúncias",
                emoji="⚖️",
                description="Denunciar um jogador ou membro."
            ),
            discord.SelectOption(
                label="Dúvidas",
                emoji="❓",
                description="Tirar dúvidas sobre a França."
            ),
            discord.SelectOption(
                label="Transferência",
                emoji="🔄",
                description="Solicitar transferência."
            ),
        ]

        super().__init__(
            placeholder="📂 Selecione uma categoria...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):

        categoria = interaction.guild.get_channel(CATEGORY_ID)

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(
                view_channel=False
            ),
            interaction.user: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True,
            ),
            interaction.guild.me: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                manage_channels=True,
            ),
        }

        canal = await interaction.guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=categoria,
            overwrites=overwrites,
        )

        embed = discord.Embed(
            title="🎫 Ticket Aberto",
            description=(
                f"Olá {interaction.user.mention}!\n\n"
                f"**Categoria:** **{self.values[0]}**\n\n"
                "Explique detalhadamente o motivo da abertura do ticket.\n"
                "Nossa equipe responderá o mais rápido possível."
            ),
            color=0xC1121F,
        )

        embed.add_field(
            name="📌 Status",
            value="🟢 Aguardando atendimento",
            inline=False,
        )

        embed.add_field(
            name="👤 Criado por",
            value=interaction.user.mention,
            inline=True,
        )

        embed.add_field(
            name="📂 Categoria",
            value=self.values[0],
            inline=True,
        )

        embed.set_footer(
            text="Vivência RP | França #100"
        )

        await canal.send(
            embed=embed,
            view=ManageView()
        )

        await interaction.response.send_message(
            f"✅ Seu ticket foi criado: {canal.mention}",
            ephemeral=True,
        )


class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketSelect())