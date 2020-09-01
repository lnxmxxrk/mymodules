#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from asyncio import sleep
import logging
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class EditMod(loader.Module):
    """Редактирует сообщение"""  # Translateable due to @loader.tds
    strings = {"name": "MsgEdit"}

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def editcmd(self, message):
        """Edits message"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, "Нет текста")
            return
        if len(args) == 1:
            await utils.answer(message, "Мало текста")
            return
        big = False if args == [] else True
        for _ in range(10):
           for c in args:
               await message.edit(c+("" if not big else "&NoBreak;"))
               await sleep(0.1)
