import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

bot = Bot(token='6961322764:AAHxKwWGeEtIoUhCTSz1O3tSKlHp__RHk4M')
dp = Dispatcher()


async def main():
    bot = Bot(token='6961322764:AAHxKwWGeEtIoUhCTSz1O3tSKlHp__RHk4M')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")