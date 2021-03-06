import asyncio
import json
import utilities
from utilities import utilities

icons = {
    "01d": "š",
    "01n": "š",
    "02d": "āļø",
    "02n": "āļø",
    "03d": "āļø",
    "03n": "āļø",
    "04d": "āļø",
    "04n": "āļø",
    "09d": "š§",
    "09n": "š§",
    "10d": "š¦",
    "10n": "š¦",
    "11d": "š©",
    "11n": "š©",
    "13d": "šØ",
    "13n": "šØ",
    "50d": "š«",
    "50n": "š«",
}


async def run(message, matches, chat_id, step, crons=None):
    from_id = message.sender_id

    if step == 0:
        utilities.user_steps[from_id] = {"name": "weather", "step": 1, "data": []}
        text = "send country or town name."
        return [message.reply(text)]
    elif step == 1:
        del utilities.user_steps[from_id]
        payload = {
            "q": message.raw_text,
            "units": "metric",
            "appid": "973e8a21e358ee9d30b47528b43a8746",  # Your Open Weather Api Code
        }
        req = await utilities.get(
            "http://api.openweathermap.org/data/2.5/weather", params=payload
        )
        try:
            data = json.loads(req)
            cityName = "{}, {}".format(data["name"], data["sys"]["country"])
            tempInC = round(data["main"]["temp"], 2)
            tempInF = round((1.8 * tempInC) + 32, 2)
            icon = data["weather"][0]["icon"]
            desc = data["weather"][0]["description"]
            res = "{}\nš”{}C ({}F)\n{} {}".format(
                cityName, tempInC, tempInF, icons[icon], desc
            )
            return [message.reply(res)]
        except:
            return [message.reply("try again error happened.")]
    elif from_id in utilities.user_steps:
        return [
            message.reply(
                "there is a conversation available right now if you want to canceling it please press /cancel"
            )
        ]


plugin = {
    "name": "weather",
    "desc": "Show The Weather of a city\n\n" "*For Example :*\n`/weather London`",
    "usage": ["[!/#]weather \nIn another message put the <city_name>"],
    "run": run,
    "sudo": False,
    "patterns": ["^[!/#]weather$"],
}
