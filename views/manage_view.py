import discord
from discord.ui import View

from views.add_member_modal import AddMemberModal
from views.remove_member_modal import RemoveMemberModal
from views.close_modal import CloseModal

STAFF_ROLES = [
    1490505205752528899,
    1490505205781889124,
    1490505205752528902,
    1490505205752528903,
    1490505205752528904,
    1490505205752528905,
    1490505205761179809,
    1490505205761179810,
    1490505205761179811,
    1490505205761179812,
    1490505205781889125,
    1490505205781889130,
    1490505205761179813,
    1490505205781889132,
    1490505205752528900,
    1490505205790408704,
    1490505205723168819,
    1490505205647671334,
    1490505205647671332,
    1490505205740081266,
    1490505205740081264,
    1490505205769441419,
    1490505205740081265,
    1490505205740081267,
    1490505205740081268,
    1490505205740081269,
    1490505205740081262,
    1490505205740081270,
    1490505205740081271,
    1490505205752528896,
    1490505205752528901,
    1490505205752528898,
    1520600853638025226
]


class ManageView(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def verificar_permissao(self, interaction: discord.Interaction):
        if not any(role.id in STAFF_ROLES for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Você não tem permissão para usar este botão.",
                ephemeral=True
            )
            return False
        return True

    @discord.ui.button(
        label="👮 Assumir",
        style=discord.ButtonStyle.primary
    )
    async def assumir(self, interaction: discord.Interaction, button: discord.ui.Button):

        if not await self.verificar_permissao(interaction):
            return

        embed = interaction.message.embeds[0]

        if len(embed.fields) >= 4:
            return await interaction.response.send_message(
                "❌ Este ticket já foi assumido.",
                ephemeral=True
            )

        embed.set_field_at(
            0,
            name="📌 Status",
            value="🟡 Em atendimento",
            inline=False
        )

        embed.add_field(
            name="👮 Atendente",
            value=interaction.user.mention,
            inline=False
        )

        try:
            await interaction.channel.edit(
                name=f"{interaction.channel.name}-atendido"
            )
        except:
            pass

        button.disabled = True
        button.label = "✅ Assumido"

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

        await interaction.followup.send(
            f"👮 {interaction.user.mention} assumiu este ticket."
        )

    @discord.ui.button(
        label="➕ Adicionar",
        style=discord.ButtonStyle.success
    )
    async def adicionar(self, interaction: discord.Interaction, button: discord.ui.Button):

        if not await self.verificar_permissao(interaction):
            return

        await interaction.response.send_modal(AddMemberModal())

    @discord.ui.button(
        label="➖ Remover",
        style=discord.ButtonStyle.secondary
    )
    async def remover(self, interaction: discord.Interaction, button: discord.ui.Button):

        if not await self.verificar_permissao(interaction):
            return

        await interaction.response.send_modal(RemoveMemberModal())

    @discord.ui.button(
        label="🔒 Fechar",
        style=discord.ButtonStyle.danger
    )
    async def fechar(self, interaction: discord.Interaction, button: discord.ui.Button):

        if not await self.verificar_permissao(interaction):
            return

        await interaction.response.send_modal(CloseModal())