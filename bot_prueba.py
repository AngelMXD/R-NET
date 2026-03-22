import os
import discord
from discord.ext import commands
import subprocess
import asyncio

# --- TOKEN DE DISCORD ---
TOKEN = "MTQ4MzIyNTc3Mzc5OTM3OTEwNA.G1RBBq.nZgmGOE9GcDYEFzLgFt9_YH9-8Y7A3II_aRs7Q"

class BotAdmin(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = BotAdmin()

class ControlPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🚀 Rotar y Desplegar R-NET", style=discord.ButtonStyle.danger, custom_id="btn_rotar")
    async def deploy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        
        def run_script():
            return subprocess.run(
                ["python", "manager.py"], 
                capture_output=True, 
                text=True, 
                errors="replace", 
                shell=False
            )

        try:
            resultado = await asyncio.to_thread(run_script)
            salida = resultado.stdout

            if resultado.returncode == 0 and "CLAVE_GENERADA:" in salida:
                partes = salida.split("CLAVE_GENERADA:")
                nueva_clave = partes[1].split("\n")[0].strip()

                nuevo_embed = discord.Embed(
                    title="🛡️ Panel de Seguridad R-NET",
                    description=f"✅ **¡Sitio web actualizado en Netlify!**\n\n**👤 Usuario:** `staff`\n**🔑 Clave Vigente:** `{nueva_clave}`\n\n*Presiona el botón abajo para volver a rotar las credenciales.*",
                    color=discord.Color.green(),
                    timestamp=discord.utils.utcnow()
                )
                nuevo_embed.set_footer(text="Última rotación")

                await interaction.message.edit(embed=nuevo_embed, view=self)
                await interaction.followup.send(f"✅ ¡Completado! Nueva clave: {nueva_clave}", ephemeral=True)
            else:
                error_log = resultado.stderr if resultado.stderr else salida
                mensaje = f"⚠️ **Detalle en el proceso:**\n```text\n{error_log.strip()}\n```"
                await interaction.followup.send(mensaje, ephemeral=True)

        except Exception as e:
            await interaction.followup.send(f"❌ **Error crítico del Bot:** {e}", ephemeral=True)

@bot.event
async def on_ready():
    print(f"🤖 Bot de Control R-NET encendido como {bot.user}")

@bot.command()
async def panel(ctx):
    """Manda el panel con el botón"""
    await ctx.send("🛡️ **Panel de Seguridad Reino Estelar**", view=ControlPanel())

@bot.tree.command(name="deploy", description="Despliega y rota la clave vía panel")
async def deploy(interaction: discord.Interaction):
    await interaction.response.send_message("Iniciando despliegue...", view=ControlPanel(), ephemeral=True)


if __name__ == "__main__":
    if TOKEN == "TU_TOKEN_NUEVO_AQUI":
        raise ValueError("Por favor, configura el token como variable de entorno DISCORD_TOKEN")
    bot.run(TOKEN)
