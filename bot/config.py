#    This file is part of the Compressor distribution.
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

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset veryfast -c:v libx265 -s 860x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By @animecolony (https://t.me/AnimeColony )' -metadata:s:v:0 title="H20064" -metadata:s:a:0 title="@animecolony" -metadata:s:a:1 title="@animecolony" -metadata:s:s:0 title="@animecolony" -metadata:s:s:1 title="@animecolony" -metadata:s:s:2 title="@animecolony" -pix_fmt yuv420p -crf 31 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1 -vf "[in] drawtext=fontfile=arial.ttf: fontsize=17: fontcolor=white: x=(w-text_w)/23: y=h/28: text='@animecolony': enable='between (t,500,600)',
drawtext=fontfile=arial.ttf: fontsize=18: fontcolor=white: x=(w-text_w)/32: y=h/5: text='Brought to you by @animedualaudiozippercartoonist': enable='between (t,180,190)',drawtext=text=This Anime is Downloaded from @animecolony Telegram Channel t.me/AnimeColony  :fontfile=foo.ttf:y=h/34:x=w-(t-300)*w/5.5: fontcolor=white:fontsize=20:shadowx=2:shadowy=2 ,  drawtext=text=This Anime is Downloaded from @animecolony Telegram Channel t.me/AnimeColony  :fontfile=foo.ttf:y=h/34:x=w-(t-1000)*w/5.5: fontcolor=white:fontsize=20:shadowx=2:shadowy=2"
    THUMB = config("THUMBNAIL")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
