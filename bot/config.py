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
    APP_ID = 7622984
    API_HASH = eb9af95b87e5d19acca3976d545ec748
    BOT_TOKEN = "5099097229:AAFC4WshHIqZcNceccJeNORoC92JX7jLOII"
    DEV = 1222651878
    OWNER = "1222651878 1562355479"
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset fast -c:v libx265 -crf 24 -s 1280x720 -tune psnr -b:v 2M -metadata title="Animax"  -metadata:s:v title="Animax Industry - 720p - HEVC"  -metadata:s:a title="Animax" -metadata:s:s title="Animax Subs" -map 0:v -c:a aac -b:a 256k -map 0:a -c:s copy -map 0:s? -max_muxing_queue_size 999999 "{}" -y'
    )
        THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/bc7f04c92fe8f2c0abcfe.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
