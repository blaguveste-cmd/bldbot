import asyncio
import os
from pathlib import Path
from telethon import TelegramClient

from config import API_ID, API_HASH

SESSION = "accounts/relayer.session"
PID_FILE = Path(".stars_listener.pid")


def is_listener_running() -> bool:
    if not PID_FILE.exists():
        return False
    try:
        pid = int(PID_FILE.read_text().strip())
        return pid > 0 and os.path.exists(f"/proc/{pid}")
    except Exception:
        return False


async def main():
    if is_listener_running():
        print("⚠️ Stars listener запущен. Проверка сессии через этот скрипт невозможна — listener уже использует сессию.")
        return

    print(f"Проверяю: {SESSION}")
    client = TelegramClient(SESSION, API_ID, API_HASH)

    try:
        await client.connect()
        if await client.is_user_authorized():
            me = await client.get_me()
            print("✅ Сессия ЖИВАЯ")
            print(f"   ID: {me.id}")
            print(f"   Имя: {me.first_name}")
            print(f"   Username: @{me.username}" if me.username else "   Username: нет")
        else:
            print("❌ Сессия МЁРТВАЯ — нужно создавать заново")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("   Сессия скорее всего битая или аккаунт забанен")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())