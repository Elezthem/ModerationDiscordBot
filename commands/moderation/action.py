import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
import sqlite3
import asyncio

from chess import pgn

from datetime import date, time, timedelta, datetime

db = sqlite3.connect("server.db") 
cur = db.cursor()

class Back(disnake.ui.View):

    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)

    @disnake.ui.button(label="Back", style=ButtonStyle.red)
    async def Back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction —\n{self.target}",
            description = f"{self.author.mention}, Choose an option to interact with {self.target.mention}"
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        guild = self.client.get_guild(1148955538080677959)
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, guild))

class Back_two(disnake.ui.View):
    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)

    @disnake.ui.button(label="Cancel", style=ButtonStyle.red)
    async def Back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        guild = self.client.get_guild(1148955538080677959)
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, guild))

class Warns(disnake.ui.Button):
    def __init__(self, label, author, target, con):
        super().__init__(label = label, style = disnake.ButtonStyle.primary)
        self.author = author
        self.target = target
        self.con = con

    async def callback(self, interaction):
        cur.execute("DELETE FROM warn WHERE _rowid_ = ?", [self.con])

        db.commit()
        await self.target.send(embed = disnake.Embed(
                    title = "You have been punished",
                    description = f"{interaction.author.mention}, removed your warning",
                    ).set_thumbnail(
            url = self.target.avatar)
        )
        await interaction.response.edit_message(embed = disnake.Embed(
            title = "Action completed",
            description = f" User {self.target.mention}\n  warning was lifted - {self.author.mention}" 
            
        
        ),view = None)
class Back_one(disnake.ui.Button):
    def __init__(self, client, author, target):
        super().__init__(label = "Cancel", style = disnake.ButtonStyle.red)
        self.client = client
        self.author = author
        self.target = target

    async def callback(self, interaction):
        embed = disnake.Embed(
            title = f"Member interaction",
            description = f"{self.author.mention}, Choose an option to interact with {self.target.mention}"
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target))
class MuteVoice(disnake.ui.View):
    def __init__(self, client, author, target,guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
    
    async def interaction_check(self, interaction):
        if interaction.user == self.author or interaction.user == self.author:
            return True
        else:
            return False

    @disnake.ui.button(label="30 min", style=ButtonStyle.gray)
    async def one(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1067554815690952835)
        VoiceMute = disnake.utils.get(interaction.guild.roles, id = 1067827578972422185)
        modal = ReasonVoice(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )

        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(VoiceMute)
        await asyncio.sleep(1800) 
        await self.target.remove_roles(VoiceMute)
        
        

    @disnake.ui.button(label="1 hour", style=ButtonStyle.gray)
    async def two(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1148955538080677959)
        types = "VoiceMute"
        reason = "**Reason**"
        VoiceMute = disnake.utils.get(interaction.guild.roles, id = 1067827578972422185)
        modal = ReasonVoice(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )

        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(VoiceMute)
        await asyncio.sleep(3600)
        await self.target.remove_roles(VoiceMute)

    @disnake.ui.button(label="2 hours", style=ButtonStyle.gray)
    async def three(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1148955538080677959)
        types = "VoiceMute"
        reason = "**Reson**"
        VoiceMute = disnake.utils.get(interaction.guild.roles, id = 1067827578972422185)
        modal = ReasonVoice(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        
        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(VoiceMute)
        await asyncio.sleep(7200)
        await self.target.remove_roles(VoiceMute)


    @disnake.ui.button(label = "Cancel", style=ButtonStyle.red, row = 1)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, self.guild))

class MuteText(disnake.ui.View):
    def __init__(self, client, author, target,guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
    
    async def interaction_check(self, interaction):
        if interaction.user == self.author or interaction.user == self.author:
            return True
        else:
            return False

    @disnake.ui.button(label="30 min", style=ButtonStyle.gray)
    async def one(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1148955538080677959)
        TextMute = disnake.utils.get(interaction.guild.roles, id = 1149257769522823209)
        modal = ReasonText(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(TextMute)
        await asyncio.sleep(1800) 
        await self.target.remove_roles(TextMute)
        
        

    @disnake.ui.button(label="1 hour", style=ButtonStyle.gray)
    async def two(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1148955538080677959)
        TextMute = disnake.utils.get(interaction.guild.roles, id = 1149257769522823209)
        modal = ReasonText(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(TextMute)
        await asyncio.sleep(3600)
        await self.target.remove_roles(TextMute)

    @disnake.ui.button(label="2 hours", style=ButtonStyle.gray)
    async def three(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        guild = self.client.get_guild(1148955538080677959)

        TextMute = disnake.utils.get(interaction.guild.roles, id = 1149257769522823209)
        modal = ReasonText(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        
        await interaction.response.send_modal(modal)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        await self.target.add_roles(TextMute)
        await asyncio.sleep(7200)
        await self.target.remove_roles(TextMute)


    @disnake.ui.button(label = "Cancel", style=ButtonStyle.red, row = 1)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        
class Warns(disnake.ui.Button):
    def __init__(self, label, author, target, con):
        super().__init__(label = label, style = disnake.ButtonStyle.primary)
        self.author = author
        self.target = target
        self.con = con

    async def callback(self, interaction):
        cur.execute("DELETE FROM warn WHERE _rowid_ = ?", [self.con])
        db.commit()
        await interaction.response.edit_message(embed = disnake.Embed(
            title = "Action completed",
            description = f" у {self.target.mention} the warning has been removed by the administrator - {self.author.mention}" 
        ),view = None)

class Back_one(disnake.ui.Button):
    def __init__(self, client, author, target):
        super().__init__(label = "Cancel", style = disnake.ButtonStyle.red)
        self.client = client
        self.author = author
        self.target = target

    async def callback(self, interaction):
        embed = disnake.Embed(
            title = f"Member interaction —\n{self.target}",
            description = f"{self.author.mention}, Choose an option to interact with {self.target.mention}"
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        # guild = self.client.get_guild(1028268015298560100)
        await interaction.response.edit_message(embed = embed, view = Back(self.client, self.author, self.target))

class ReasonVoice(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Mute reason",
            custom_id="Reason",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Issuance of punishment", description = f"{self.user.mention} made a voice mut - {self.target.mention} \n\n**Reason:** {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        types = "VoiceMute"
        reason = interaction.text_values['name']
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"You have successfully issued a mute {self.target.mention}"
        ), ephemeral = True)
        
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.user.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.user.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.user.id))
            cur.execute("UPDATE users SET mutes = mutes + 1 WHERE id = {}".format(self.user.id))
            cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.user.id, reason, types,datetime.today().replace(microsecond=0)])
            db.commit()
        # await channel.send(view=BroadButton(self.user))
class ReasonVerifBan(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Mute reason",
            custom_id="Reason",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="   ", description = f"{self.user.mention} выдал недопуск - {self.target.mention} \nПричина: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"Вы успешно выдали недопуск {self.target.mention}"
        ), ephemeral = True)
        # await channel.send(view=BroadButton(self.user))
class ReasonUnVerifBan(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. НИЖЕ ОПИШИТЕ ПРИЧИНУ",
                placeholder="Пример: 1.8",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Причина мута",
            custom_id="Reason",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="   ", description = f"{self.user.mention} снял недопуск - {self.target.mention} \nПричина: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"Вы успешно сняли недопуск {self.target.mention}"
        ), ephemeral = True)
        # await channel.send(view=BroadButton(self.user))

class ReasonText(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Mute reason",
            custom_id="ReasonText",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Issuance of punishment", description = f"{self.user.mention} issued a text mute - {self.target.mention} \nReason: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        types = "TextMute"
        reason = interaction.text_values['name']
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"You have successfully issued a mute {self.target.mention}"
        ), ephemeral = True)
        
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.user.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.user.id))
            cur.execute("UPDATE users SET mutes = mutes + 1 WHERE id = {}".format(self.user.id))
            cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.user.id, reason, types,datetime.today().replace(microsecond=0)])
            db.commit()
        # await channel.send(view=BroadButton(self.user))

class ReasonUnVoice(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Reason mute",
            custom_id="ReasonText",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Досрочное снятие наказания", description = f"{self.user.mention} снял голосовой мут - {self.target.mention} \nПричина: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"Вы успешно сняли голосовой мут {self.target.mention}"
        ), ephemeral = True)
        # await channel.send(view=BroadButton(self.user))
class ReasonUnText(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Reason mute",
            custom_id="ReasonText",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Early removal of punishment", description = f"{self.user.mention} removed the text mute - {self.target.mention} \nReason: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"You have successfully removed the text mute {self.target.mention}"
        ), ephemeral = True)
        # await channel.send(view=BroadButton(self.user))
class ReasonBan(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Reason ban",
            custom_id="ReasonText",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Issuance of punishment", description = f"{self.user.mention} issued a ban - {self.target.mention} \nReason: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        reason = interaction.text_values['name']
        types = "Ban"
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"You have successfully issued a ban {self.target.mention}"
        ), ephemeral = True)
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.user.id]).fetchone() is None:
                cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.user.id, 0, 0, 0, 0, 0, 0, 0, 0])
                db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 10 WHERE id = {}".format(self.user.id))
            cur.execute("UPDATE users SET bans = bans + 1 WHERE id = {}".format(self.user.id))
            cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.user.id, reason, types,datetime.today().replace(microsecond=0)])
            db.commit()

class ReasonUnBan(disnake.ui.Modal):
    def __init__(self, user, guild, target):
        self.user = user
        self.guild = guild
        self.target = target
        components = [
            disnake.ui.TextInput(
                label="1. DESCRIBE THE REASON BELOW",
                placeholder="Example: 10",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(
            title="Reason for early ban removal",
            custom_id="ReasonText",
            components=components,
        )
    async def callback(self, interaction):
        emb = disnake.Embed(title="Early removal of punishment", description = f"{self.user.mention} removed the ban - {self.target.mention} \nReason: {interaction.text_values['name']}")
        channel = self.guild.get_channel(1148964080682549268)
        reason = interaction.text_values['name']
        types = "Ban"
        await channel.send(embed=emb)
        await interaction.response.send_message(embed = disnake.Embed(
            description = f"You have successfully removed the ban {self.target.mention}"
        ), ephemeral = True)

class MuteButtons(disnake.ui.View):
    def __init__(self, client, author, target, guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def text(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        types = "VoiceMute"
        Obed = disnake.Embed(
            title = f"Взаимодействие с участником — {self.target}",
            description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
        )
        Obed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        Obed.set_thumbnail(
            url = self.target.avatar
        )
        
        embed = disnake.Embed(
            title = "Issue mute",
            description = "Choose a mute time"
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = MuteVoice(self.client, self.author, self.target, self.guild))

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        # await msg.delete()
        cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.author.id, reason, types,datetime.today().replace(microsecond=0)])
        db.commit()
        # await self.target.add_roles(muteVoice)
        # await interaction.send(embed=disnake.Embed(
        #     description = f"Вы успешно выдали голосовой мут - {self.target.mention}"
        # ), ephemeral=True)
        # await interaction.delete_original_message()
        # await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, guild))
        
        # await channel.send(embed = disnake.Embed(
        #     title = "Выдача наказания",
        #     description = f"{self.author.mention} выдал  голосовой мут - {self.target.mention} \nПричина: {reason}"
        #     #description = f"{self.target.mention} получил предупреждение по причине **{reason}**\n Выдал - {self.author.mention}"
        # ), view = None)

        # await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        
        self.stop()


    @disnake.ui.button(label="Text", style=ButtonStyle.gray)
    async def voice(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        types = "TextMute"
        Obed = disnake.Embed(
            title = f"Member interaction — {self.target}",
            description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
        )
        Obed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        Obed.set_thumbnail(
            url = self.target.avatar
        )
        
        embed = disnake.Embed(
            title = "Issue mute",
            description = "In the chat, write the reason why you want to issue a mut to the user"
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = MuteText(self.client, self.author, self.target, self.guild))
    @disnake.ui.button(label="Cancel", style=ButtonStyle.red)
    async def Backs(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        guild = self.client.get_guild(1148955538080677959)
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, guild))

class UnMuteButtons(disnake.ui.View):
    def __init__(self, client, author, target, guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def text(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        VoiceMute = disnake.utils.get(interaction.guild.roles, id = 1067827578972422185)
        modal = ReasonUnVoice(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        
        await interaction.response.send_modal(modal)
        await self.target.remove_roles(VoiceMute)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        
        self.stop()

    @disnake.ui.button(label="Text", style=ButtonStyle.gray)
    async def voice(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):

        VoiceMute = disnake.utils.get(interaction.guild.roles, id = 1149257769522823209)
        modal = ReasonUnText(interaction.user, self.guild, self.target)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        
        await interaction.response.send_modal(modal)
        await self.target.remove_roles(VoiceMute)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        
        self.stop()
    @disnake.ui.button(label="Cancel", style=ButtonStyle.red)
    async def Backs(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        guild = self.client.get_guild(1148955538080677959)
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, guild))
        
class GenderChange(disnake.ui.View):
    def __init__(self, client, author, target, guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def chmale(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        female = disnake.utils.get(interaction.guild.roles, id = 111)
        male = disnake.utils.get(interaction.guild.roles, id = 111)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await self.target.add_roles(male)
        await self.target.remove_roles(female)
        await interaction.response.defer()
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        await interaction.send(embed = disnake.Embed(
            description = f"Вы успешно сменили **гендер** на мужскую, пользователю - {self.target.mention}"
        ), ephemeral = True)
        
        self.stop()
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            db.commit()
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def chmfemale(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        female = disnake.utils.get(interaction.guild.roles, id = 111)
        male = disnake.utils.get(interaction.guild.roles, id = 111)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await self.target.add_roles(female)
        await self.target.remove_roles(male)
        await interaction.response.defer()
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        await interaction.send(embed = disnake.Embed(
            description = f"Вы успешно сменили **гендер** на женскую, пользователю - {self.target.mention}"
        ), ephemeral = True)
        
        self.stop()
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            db.commit()
        
class Verif(disnake.ui.View):
    def __init__(self, client, author, target, guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
    async def interaction_check(self, interaction):
        if interaction.user == self.author or interaction.user == self.author:
            return True
        else:
            return False
        
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def chmale(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        female = disnake.utils.get(interaction.guild.roles, id = 111)
        male = disnake.utils.get(interaction.guild.roles, id = 111)
        unverifi = disnake.utils.get(interaction.guild.roles, id =111)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await self.target.add_roles(male)
        await self.target.remove_roles(female)
        await self.target.remove_roles(unverifi)
        await interaction.response.defer()
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        await interaction.send(embed = disnake.Embed(
            description = f"Вы успешно верифицировали пользователя - {self.target.mention}, мужской **гендеркой**"
        ), ephemeral = True)
        
        self.stop()
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            cur.execute("UPDATE users SET verefy = verefy + 1 WHERE id = {}".format(self.author.id))
            db.commit()
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray)
    async def chfemale(self, button: disnake.ui.Button,  interaction: disnake.MessageInteraction):
        male = disnake.utils.get(interaction.guild.roles, id = 111)
        female = disnake.utils.get(interaction.guild.roles, id = 111)
        unverifi = disnake.utils.get(interaction.guild.roles, id = 111)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await self.target.add_roles(female)
        await self.target.remove_roles(male)
        await self.target.remove_roles(unverifi)
        await interaction.response.defer()
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        await interaction.send(embed = disnake.Embed(
            description = f"Вы успешно верифицировали пользователя - {self.target.mention}, женской **гендеркой**"
        ), ephemeral = True)
        
        self.stop()
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            cur.execute("UPDATE users SET verefy = verefy + 1 WHERE id = {}".format(self.author.id))
            db.commit()
    @disnake.ui.button(label="Cancel", style=ButtonStyle.red)
    async def Backs(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Member interaction — {self.target}",
                description = f"ID: `{self.target.id}`",
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        guild = self.client.get_guild(1067554815690952835)
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target, guild))
        
class ModerationButtons(disnake.ui.View):
    
    def __init__(self, client, author, target, guild):
        self.client = client
        self.author = author
        self.target = target
        self.guild = guild
        super().__init__(timeout=None)
    
    async def interaction_check(self, interaction):
        if interaction.user == self.author or interaction.user == self.author:
            return True
        else:
            return False

    
    @disnake.ui.button(label="Mute", style=ButtonStyle.gray, row = 2)
    async def Mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
            embed = disnake.Embed(
                title = "Choose which mute to give to the user",
            ).set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            ).set_thumbnail(
                url = self.target.avatar
            )
            await interaction.response.edit_message(embed = embed, view = MuteButtons(self.client, self.author, self.target, self.guild))
            # await self.target.add_roles(mute)
            # await interaction.send(embed=embed, ephemeral=True)
            self.stop()


    @disnake.ui.button(label="Unmute", style=ButtonStyle.gray, row = 2)
    async def Unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
            embed = disnake.Embed(
                title = "Choose which mute to remove the user",
            ).set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            ).set_thumbnail(
                url = self.target.avatar
            )
            await interaction.response.edit_message(embed = embed, view = UnMuteButtons(self.client, self.author, self.target, self.guild))
            # await self.target.add_roles(mute)
            # await interaction.send(embed=embed, ephemeral=True)
            self.stop()
    
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray, row = 2)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
    
            modal = ReasonBan(interaction.user, self.guild, self.target)
            Ban = disnake.utils.get(interaction.guild.roles, id = 1079732047205117993)
            Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
            Obed.set_author(
                    name = self.target,
                    url = f"https://discordapp.com/users/{self.target.id}/",
                    icon_url = self.target.avatar
                )
            Obed.set_thumbnail(
                    url = self.target.avatar
                )
            await interaction.response.send_modal(modal)
            await interaction.delete_original_message()
            await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
            await self.target.add_roles(Ban)
            

            # await interaction.response.edit_message(embed = embed, view = UnMuteButtons(self.client, self.author, self.target, self.guild))
            # await self.target.add_roles(mute)
            # await interaction.send(embed=embed, ephemeral=True)
            self.stop()
            
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.gray, row = 2)
    async def Unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
            modal = ReasonUnBan(interaction.user, self.guild, self.target)
            Ban = disnake.utils.get(interaction.guild.roles, id = 1079732047205117993)

            Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
            Obed.set_author(
                    name = self.target,
                    url = f"https://discordapp.com/users/{self.target.id}/",
                    icon_url = self.target.avatar
                )
            Obed.set_thumbnail(
                    url = self.target.avatar
                )
            
            await interaction.response.send_modal(modal)
            await self.target.remove_roles(Ban)
            
            await interaction.delete_original_message()
            await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
            # await interaction.response.edit_message(embed = embed, view = UnMuteButtons(self.client, self.author, self.target, self.guild))
            # await self.target.add_roles(mute)
            # await interaction.send(embed=embed, ephemeral=True)
            self.stop()
            
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.primary, row = 2)
    async def gender(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
            embed = disnake.Embed(
                title = f"Взаимодействие с участником - {self.target}",
                description =f"Определите **гендер** участника {self.target.mention}\n\n."
            ).set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            ).set_thumbnail(
                url = self.target.avatar
            )
            
            await interaction.response.edit_message(embed = embed, view = GenderChange(self.client, self.author, self.target, self.guild))
            # await self.target.add_roles(mute)
            # await interaction.send(embed=embed, ephemeral=True)
            self.stop()
            
    
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.grey, row = 4)
    async def veref(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
                title = f"Верификация участника - {self.target}",
                description =f"Верифицируйте {self.target.mention}\n\n."
            ).set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            ).set_thumbnail(
                url = self.target.avatar
            )
            
        await interaction.response.edit_message(embed = embed, view = Verif(self.client, self.author, self.target, self.guild))
    
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.grey, row = 4)
    async def nedo(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = ReasonVerifBan(interaction.user, self.guild, self.target)
        verifBan = disnake.utils.get(interaction.guild.roles, id = 111)
        Obed = disnake.Embed(
                title = f"Взаимодействие с участником — {self.target}",
                description = f"{interaction.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await interaction.response.send_modal(modal)
        await self.target.add_roles(verifBan)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            cur.execute("UPDATE users SET vetifBan = vetifBan + 1 WHERE id = {}".format(self.author.id))
            db.commit()
            
    @disnake.ui.button(label="ㅤ", style=ButtonStyle.grey, row = 4)
    async def unnedo(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        modal = ReasonUnVerifBan(interaction.user, self.guild, self.target)
        verifBan = disnake.utils.get(interaction.guild.roles, id = 111)
        Obed = disnake.Embed(
                title = f"Member interaction — {self.target}",
                description = f"{interaction.author.mention}, Choose an option to interact with {self.target.mention}"
            )
        Obed.set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            )
        Obed.set_thumbnail(
                url = self.target.avatar
            )
        await interaction.response.send_modal(modal)
        await self.target.remove_roles(verifBan)
        await interaction.delete_original_message()
        await interaction.send(embed=Obed, view = ModerationButtons(self.client, self.author, self.target, self.guild))
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            db.commit()
        
        
    @disnake.ui.button(label="Issue a warning", style=ButtonStyle.grey, row = 3)
    async def Warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        types = "warn"
        embed = disnake.Embed(
            title = "Issue a warning to the user",
            description = "In the chat, write the reason why you want to issue a warning to the user"
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = Back_two(self.client, self.author, self.target))

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.author.id, reason, types,datetime.today().replace(microsecond=0)])
        db.commit()
        await self.target.send(embed = disnake.Embed(
                    title = "You have been punished",
                    description = f"{interaction.author.mention}, gave you a warning\n Because of: **{reason}**\n date and time: **{datetime.today().replace(microsecond=0)}**",
                    ).set_thumbnail(
            url = self.target.avatar)
        )
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            cur.execute("UPDATE users SET warns = warns + 1 WHERE id = {}".format(self.author.id))
            cur.execute("INSERT INTO warn VALUES(?,?,?,?,?)",[self.target.id, self.author.id, reason, types,datetime.today().replace(microsecond=0)])
            db.commit()

        await interaction.edit_original_message(embed = disnake.Embed(
            description = f"{self.target.mention} received a warning for **{reason}**\n Gave out - {self.author.mention}"
        ), view = None)


    @disnake.ui.button(label="Remove warning", style=ButtonStyle.grey, row = 3)
    async def Unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]).fetchone() == None:
            return await interaction.response.send_message(embed = disnake.Embed(
                title = "Member has no warnings"
            ), ephemeral = True)
        view = disnake.ui.View()
        for x in cur.execute("SELECT id, adm, reason, _rowid_ FROM warn WHERE id = ?", [self.target.id]):
            view.add_item(Warns(label = x[2], author = self.author, target = self.target, con = x[3]))
        view.add_item(Back_one(self.client, self.author, self.target))
        await interaction.response.edit_message(embed = disnake.Embed(
            title = "Choose a warning"
        ), view = view)
        if cur.execute(f"SELECT id FROM users WHERE id = ?", [self.author.id]).fetchone() is None:
            cur.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [self.author.id, 0, 0, 0, 0, 0, 0, 0, 0])
            db.commit()
        else:
            
            cur.execute("UPDATE users SET points = points + 5 WHERE id = {}".format(self.author.id))
            db.commit()

    @disnake.ui.button(label="History of violations", style=ButtonStyle.gray, row = 4)
    async def Warn_History(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]).fetchone() == None:
            await interaction.response.send_message(embed = disnake.Embed(
                title = "participant has no warnings"
            ), ephemeral = True)
        else:
            emb = disnake.Embed(
                title = f"List of violations — {self.target}"
            )
            a = 0
            for x in cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]):
                a += 1
                emb.add_field(name = f"{a}) {x[2]}", value = f"**Type of punishment:** {x[3]}\n**date:** {x[4]}\n**Gave out:** <@{x[1]}>")
            await interaction.response.edit_message(embed = emb, view = Back(self.client, self.author, self.target))


            
    @disnake.ui.button(label="Cancel", style=ButtonStyle.red, row = 4)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.edit_original_message(embed = disnake.Embed(
            title = "Deleting a message..."
        ), view = None)
        await interaction.delete_original_message()

class Action(commands.Cog):

    def __init__(self, client):
        self.client = client
        print('Commands {} is loaded'.format(self.__class__.__name__))

    @commands.slash_command(name='action', description='Interaction menu')
    @commands.has_any_role(1148972401187627092,1148968585906094110,1148965052515356745,1148965329955995668,1149259036164894740)
    async def admin(self, inter, target: disnake.Member = commands.Param(name = "пользователь")):
        if target == None:
            target = await self.bot.fetch_user(target)
            print(target)
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
        if inter.author.top_role <= target.top_role:
            embed = disnake.Embed(
                title = "Member interaction",
                description = "You cannot interact with the member because your role is lower than or equal to the member's role"
            ).set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            ).set_thumbnail(
                url = target.avatar
            )
            await inter.send(embed = embed, ephemeral = True)
        else:
            embed = disnake.Embed(
                title = f"Member interaction — {target}",
                description = f"ID: `{target.id}`",
            )
            embed.set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            )
            embed.set_thumbnail(
                url = target.avatar
            )
            guild = self.client.get_guild(1148955538080677959)
            await inter.send(embed = embed, view = ModerationButtons(self.client, inter.author, target, guild))
            
    @admin.error
    async def on_command_error(self, inter, error):
        if (error, commands.MissingRole):
            print(error)
            embed = disnake.Embed(
                title="Not Enough Rights!",
                description=f"{inter.author.mention} you do not have permission to do this!"
            )
            await inter.send(embed=embed, ephemeral=True)


def setup(client):
    client.add_cog(Action(client))