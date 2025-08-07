__version__ = (1, 1, 0)
#                                                                                                          
#                                                                                                       88  
#                                                    ,d                                          ,d     88  
#                                                    88                                          88     88  
#  ,adPPYba,  8b,dPPYba,  8b       d8  8b,dPPYba,  MM88MMM  ,adPPYba,  8b,     ,d8  ,adPPYba,  MM88MMM  88  
# a8"     ""  88P'   "Y8  `8b     d8'  88P'    "8a   88    a8P_____88   `Y8, ,8P'  a8"     ""    88     88  
# 8b          88           `8b   d8'   88       d8   88    8PP"""""""     )888(    8b            88     88  
#  "8a,   ,aa  88            `8b,d8'    88b,   ,a8"   88,   "8b,   ,aa   ,d8" "8b,  "8a,   ,aa    88,    88  
#  `"Ybbd8"'  88              Y88'     88`YbbdP"'    "Y888  `"Ybbd8"'  8P'     `Y8  `"Ybbd8"'    "Y888  88  
#                            d8'      88                                                                   
#                           d8'       88                                                                   
#              © Copyright 2024
#           https://t.me/cryptexctl
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# сланцы.py
# meta developer: @systemxplore
# scope: hikka_only
# scope: hikka_min 1.6.3
import os
import requests
from .. import loader, utils

class SlantsyMod(loader.Module):
    """АХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\n"""
    strings = {
        "name": "Сланцы",
    }

    def __init__(self):
        # Путь, куда будет загружена картинка
        self.image_path = "сланцы.jpeg"
        self.image_url = "https://0x0.st/Xd9E.jpeg"

    async def client_ready(self, client, db):
        self.client = client
        self.download_image()

    def download_image(self):
        """Скачивает изображение и сохраняет его на диск."""
        if not os.path.exists(self.image_path):  # Проверяем, есть ли файл
            response = requests.get(self.image_url)
            with open(self.image_path, 'wb') as file:
                file.write(response.content)
            print(f"✅ Картинка успешно загружена: {self.image_path}")
        else:
            print(f"🖼️ Картинка уже существует: {self.image_path}")

    @loader.command()
    async def этосланцычат(self, message):
        """АХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\nАХХХ ЭТО ГОРЯЩИЕ СЛАНЦЫ ЧААТ\n"""
        await self.client.send_file(message.chat_id, self.image_path)
        # Удаляем сообщение с командой
        await message.delete()
