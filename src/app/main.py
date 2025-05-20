from typing import Optional

from discord.ext import commands
from discord.ext.commands import MemberConverter, RoleConverter

from .bot_logging import getLogger
from .config import DISCORD_TOKEN, getIntents

logger = getLogger()
bot = commands.Bot(command_prefix='$', intents=getIntents())


@bot.event
async def on_ready():
    logger.info(f'{bot.user.name} has connected to Discord!')


@bot.command(name='roles')
async def list_roles(ctx):
    """List all groups (Roles) for the given guild."""
    logger.info('List roles')
    await ctx.send('Roles:')


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

def main():
    logger.info('Starting Discord bot...')
    bot.run(DISCORD_TOKEN)
    logger.info('Discord bot stopped.')


if __name__ == '__main__':
    main()
