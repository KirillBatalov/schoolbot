import asyncio
from aiogram import Dispatcher, Bot

from handlers import router
from settings import config


async def main():
    dispatcher = Dispatcher()
    bot = Bot(token=config.bot_token.get_secret_value())

    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())