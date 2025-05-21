import discord
from discord.ext import commands

from .bot_logging import getLogger


class EmbedRolesFactory:
    __DEFAULT_EXEMPT_ROLES = ["@everyone", "Bot", "Admin", "Moderator"]

    def __init__(self, bot_name: str):
        self._logger = getLogger()
        self.__exempt_roles = self.__DEFAULT_EXEMPT_ROLES
        self.__exempt_roles.append(bot_name)

    @property
    def exempt_roles(self) -> list[str]:
        return self.__exempt_roles

    def create_embed(self, author: discord.User | discord.Member, guild: discord.Guild, roles: list[discord.Role]) -> discord.Embed:
        if not roles:
            self._logger.warning(f'No roles found in guild {guild} from {author}.')
            embed = discord.Embed(title="Server Roles", description="No roles found.", color=discord.Color.red())
            return embed

        desc = "\n".join(f"• {role.name}" for role in roles)
        title = f"{guild.name} Roles ({len(roles)})"
        embed = discord.Embed(title=title, description=desc, color=discord.Color.blue())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.set_footer(text=f"Requested by {author.name}", icon_url=author.avatar.url if author.avatar else None)
        embed.timestamp = discord.utils.utcnow()
        self._logger.info(f'Embed created for {author} in guild {guild} for roles {len(roles)}.')
        return embed


class RolesService:

    def __init__(self, embed_factory: EmbedRolesFactory):
        self._logger = getLogger()
        self._embed_factory = embed_factory

    def list_roles(self, ctx: commands.Context) -> discord.Embed:
        self._logger.info(f'List roles for guild: {ctx.guild.name} from {ctx.author}.')
        roles = [roles_found for roles_found in ctx.guild.roles if roles_found.name not in self._embed_factory.exempt_roles]
        return self._embed_factory.create_embed(author=ctx.author, guild=ctx.guild, roles=roles)
