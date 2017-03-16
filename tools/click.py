from macro.bot import bot

x, y = bot.get_position()
bot.left_click(x, y, n=20, pre_dl=3)