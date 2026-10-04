import asyncio
import io
import os
from typing import Any

import botpy
from botpy import logging
from botpy.message import GroupMessage

import command_processor
import config
import user_database

_log = logging.get_logger()


# qbot client
class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message: GroupMessage):
        userID: str = message.author.member_openid
        groupID: str = str(message.group_openid)
        msg_content: str = message.content

        # log message
        _log.info(f"from user[{userID}] in group[{groupID}]: {msg_content}")

        # register user
        if user_database.is_user_registered(uid=userID) == False:
            user_database.register_user(uid=userID)

        # process command
        reply: str = command_processor.process_command(
            uid=userID, full_command=msg_content
        )

        # reply
        if reply != "":
            await message.reply(content=reply)


intents = botpy.Intents(public_messages=True)

asyncio.set_event_loop(asyncio.new_event_loop())
client = MyClient(intents=intents)
client.run(appid=config.json_apikey["appid"], secret=config.json_apikey["secret"])
