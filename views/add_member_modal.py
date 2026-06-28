import discord


class AddMemberModal(discord.ui.Modal):

    def __init__(self):
        super().__init__(title="Adicionar membro")

        self.usuario = discord.ui.TextInput(
            label="ID do usuário",
            placeholder="Cole o ID do usuário aqui",
            required=True
        )

        self.add_item(self.usuario)

    async def on_submit(self, interaction: discord.Interaction):

        try:
            membro = await interaction.guild.fetch_member(int(self.usuario.value))
        except Exception:
            await interaction.response.send_message(
                "❌ ID inválido.",
                ephemeral=True
            )
            return

        await interaction.channel.set_permissions(
            membro,
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )

        await interaction.response.send_message(
            f"✅ {membro.mention} foi adicionado ao ticket.",
            ephemeral=False
        )