#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A EncoderQueue Which Can Encode Videos.\nReduce Size of Videos (Depends on your Code)\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="github.com/1Danish-00/"),
                Button.url("DEVELOPER", url="t.me/SenpaiAF"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 A Quality EncoderQueue**\n\n+This Bot Encodes Videos With Negligible Quality Change.(Depends on your Code)\n+Generate Sample Encoded Video\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Encode.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Quality EncoderQueue**\n\n+This Bot Encodes Videos With Negligible Quality Change.\n+Generate Sample Encoded Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Encode.\nSo Be patience And Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A EncoderQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change (Depends on your Code)\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="github.com/1Danish-00/"),
                Button.url("DEVELOPER", url="t.me/SenpaiAF"),
            ],
        ],
    )
