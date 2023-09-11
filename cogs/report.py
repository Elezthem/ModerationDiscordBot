import disnake
from disnake.ext import commands
import datetime

import time
import sqlite3

db = sqlite3.connect("server.db") 
cur = db.cursor()

class Button(disnake.ui.View):
    def __init__(self,member):
        super().__init__(timeout=None)
        self.member = member

    @disnake.ui.button(label="Accept", style=disnake.ButtonStyle.green)
    async def confirm(self,button: disnake.ui.Button,inter: disnake.MessageInteraction):
        await self.member.send(embed = disnake.Embed(
                    title = "Your report has been accepted!",
                    description = f"Your report has been accepted by the moderator - {inter.author.mention}\n",
                    ).set_thumbnail(
            url = self.member.avatar)
        )
        # await self.client.send_message(self.member, "Your message goes here")
        self.value = True
        self.stop()
        await inter.message.delete()
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [inter.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [inter.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(inter.author.id))
            cur.execute("UPDATE users SET reports = reports + 1 WHERE id = {}".format(inter.author.id))
            db.commit()
    
    @disnake.ui.button(label="Reject", style=disnake.ButtonStyle.red)
    async def decline(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await self.member.send(embed = disnake.Embed(
                    title = "Your application has been rejected",
                    description = f"{self.member.mention} Your report has been rejected by the moderator - {inter.author.mention}\n",
                    ).set_thumbnail(
            url = self.member.avatar)
        )
        self.value = True
        self.stop()
        await inter.message.delete();
        
class Reports(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.member = None
        print('Commands {} is loaded'.format(self.__class__.__name__))
    
    @commands.slash_command(name='report', description='File a complaint against a member/staff')

    async def report(self, inter, target: disnake.Member = commands.Param(name = "user"),message: str = commands.Param(name = "reason")):
        channel = self.client.get_channel(1110856776624119828)
        self.member = inter.author
        if target == inter.author:
            embed = disnake.Embed(
                title = "Member interaction",
                description = "You can't interact with yourself"
            ).set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            ).set_thumbnail(
                url = target.avatar
            )
            await inter.send(embed = embed, ephemeral = True)
            return True
        else:
            embed = disnake.Embed(
                    description = f"Complaint about {target.mention} was sent successfully",
                    color = 0x2f3136)
            
            await channel.send(
                    embed = disnake.Embed(
                title = "Report",
                description = "The user left a complaint"
            ).set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            ).set_thumbnail(
                url = target.avatar
            ).add_field(    
                    name = "Sender:",
                    value = f"{inter.author.mention}/`{inter.author.id}`",
                    inline = False
            ).add_field(
                    name = "User:",
                    value = f"{target.mention}/`{target.id}`",
                    inline = False
            ).add_field(    
                    name = "Reason:",
                    value = f"{message} ",
                    inline = False
            )
            )
            await inter.send(embed = embed,ephemeral = True)
            await channel.send(view=Button(self.member))
            
def setup(client):
    client.add_cog(Reports(client))