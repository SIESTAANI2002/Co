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
    APP_ID = config("APP_ID", default=15681388, cast=int)
    API_HASH = config("API_HASH", default="446b56944f74f6b7688175d48cdfa881")
    BOT_TOKEN = "5419649199:AAH3qRlGtk3kEHFeYPm8WdUPfDgSK73w7So"
    DEV = 5074446156
    OWNER = config("OWNER", default="5074446156")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -c:v libx265  -profile:v main10 -pix_fmt yuv420p10le -vf scale=1280:720 -preset medium  -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -x265-params frame-threads=4:log-level=2:input-csp=1:input-res=1280x720:high-tier=1:ref=6:min-keyint=23:keyint=250:bframes=6:b-adapt=2:rc-lookahead=80:lookahead-slices=6:scenecut=40:ctu=64:min-cu-size=8:max-tu-size=32:tu-inter-depth=4:tu-intra-depth=4:limit-tu=1:rdoq-level=2:max-merge=4:limit-refs=3:me=3:subme=4:merange=48:deblock=1,1:rd=4:psy-rd=0.80:psy-rdoq=1.25:ipratio=1.40:pbratio=1.30:aq-mode=3:aq-strength=0.75:cbqpoffs=-1:crqpoffs=-1:qcomp=0.60:qpstep=4:qg-size=32:qpmax=69:qpmin=0:sar=1:videoformat=5:range=0:colorprim=2:transfer=2:colormatrix=2:chromaloc=1:slices=1:no-info=1:limit-sao=1 -crf 22.2 -map 0:v -map 0:a -map 0:s -c:a aac -b:a 112k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Anime Sakura" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="AnimeSakura.Co" -metadata:s:s:0 title="Anime Sakura" -metadata:s:s:1 title="@Ani_Animesh" -metadata:s:s:2 title="AnimeSakura.co" "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
