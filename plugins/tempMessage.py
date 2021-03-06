import asyncio
from utilities import utilities


async def run(message, matches, chat_id, step, crons=None):
    response = []
    if not (message.out):
        message = await message.reply(matches)
    duration = "šā¤ļøā¤ļøā¤ļøšššššš"

    while duration != "":
        response.append(message.edit(matches + "\nāāāāāāāāāāāāāāā\n" + duration))
        response.append(asyncio.sleep(1))
        duration = duration[:-1]
    response.append(message.delete())
    return response


plugin = {
    "name": "Temp Messages",
    "desc": "send msgs for a period of time.",
    "usage": ["[!/#]tm <text> to send message for a period of time."],
    "run": run,
    "sudo": True,
    "patterns": ["^[!/#]tm (.+)$"],
}

