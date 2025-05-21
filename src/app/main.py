from typing import Optional

from discord.ext import commands
from discord.ext.commands import MemberConverter, RoleConverter

from app.service import RolesService, EmbedRolesFactory
from .bot_logging import getLogger
from .config import DISCORD_TOKEN, getIntents, BOT_NAME

logger = getLogger()
bot = commands.Bot(command_prefix='$', intents=getIntents())
rolesService = RolesService(EmbedRolesFactory(bot_name=BOT_NAME))


@bot.event
async def on_ready():
    logger.info(f'{bot.user.name} has connected to Discord!')


@bot.command(name='roles')
async def list_roles(ctx: commands.Context):
    """List all groups (Roles) for the given guild."""
    response = rolesService.list_roles(ctx)
    await ctx.send(embed=response, silent=True)


@bot.command(name='role_members')
async def list_members_with_role(ctx, guild_role: RoleConverter):
    """List all members of the given role for the given guild."""
    logger.info('List members with role')
    await ctx.send('Members of the role:')


@bot.command(name='member_roles')
async def list_roles_member_is_part_of(ctx, guild_member: MemberConverter):
    """List all roles for the given member in the given guild."""
    logger.info('List roles member is part of')
    await ctx.send('Roles of the member:')


@bot.command(name='subscribe_role')
async def subscribe_role(ctx, guild_role: RoleConverter):
    """Subscribe to the given role."""
    logger.info('Subscribe to role')
    await ctx.send('Subscribed to role.')


@bot.command(name='reminder')
async def reminder(ctx, role: RoleConverter, date_time: str, reminder_name: str, reminder_description: Optional[str] = ""):
    """Set a reminder for the given role at the given date and time."""
    logger.info('Set reminder')
    await ctx.send('Reminder set.')


@bot.command(name='reminders')
async def list_reminders(ctx, role: RoleConverter):
    """List all reminders for the given role."""
    logger.info('List reminders')
    await ctx.send('Reminders for the role:')


@bot.command(name='subscribe_reminder')
async def subscribe_reminder(ctx, reminder_id: int):
    """Subscribe to the given reminder."""
    logger.info('Subscribe to reminder')
    await ctx.send('Subscribed to reminder.')


def main():
    logger.info('Starting Discord bot...')
    bot.run(DISCORD_TOKEN)
    logger.info('Discord bot stopped.')


if __name__ == '__main__':
    main()
