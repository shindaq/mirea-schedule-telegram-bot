import asyncio
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from dotenv import load_dotenv
from loguru import logger
from utils.build_schedule_message import build_schedule_message
from service.take_week import take_week
from utils.parse_schedule import parse_schedule

from utils.env import bot_secret_token

load_dotenv(override=True)

router = Router()

parsed_schedule = parse_schedule()


def get_keyboard():
    buttons = [[
        types.InlineKeyboardButton(text="ПН", callback_data="Monday"),
        types.InlineKeyboardButton(text="ВТ", callback_data="Tuesday"),
        types.InlineKeyboardButton(text="СР", callback_data="Wednesday"),
        types.InlineKeyboardButton(text="ЧТ", callback_data="Thursday"),
        types.InlineKeyboardButton(text="ПТ", callback_data="Friday"),
        types.InlineKeyboardButton(text="СБ", callback_data="Saturday")
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query()
async def callbacks_num(callback: types.CallbackQuery):
    with suppress(TelegramBadRequest):
        day_of_the_week = callback.data
        current_week = await take_week()
        if day_of_the_week == "Monday":
            schedule = parsed_schedule[current_week][0]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=0)
        elif day_of_the_week == "Tuesday":
            schedule = parsed_schedule[current_week][1]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=1)
        elif day_of_the_week == "Wednesday":
            schedule = parsed_schedule[current_week][2]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=2)
        elif day_of_the_week == "Thursday":
            schedule = parsed_schedule[current_week][3]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=3)
        elif day_of_the_week == "Friday":
            schedule = parsed_schedule[current_week][4]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=4)
        elif day_of_the_week == "Saturday":
            schedule = parsed_schedule[current_week][5]
            text = await build_schedule_message(lessons=schedule,
                                                day_of_the_week=5)
        await callback.message.edit_text(text,
                                         parse_mode='MarkdownV2',
                                         reply_markup=get_keyboard())
        await callback.answer()


@router.message(Command("schedule"))
async def schedule_handler(message: types.Message, bot: Bot) -> None:
    try:
        current_week = await take_week()
        current_day_of_week = datetime.now(tz=timezone(offset=timedelta(
            hours=3))).weekday()
        text = ""
        if current_day_of_week == 6:
            text = await build_schedule_message(
                lessons=None, day_of_the_week=current_day_of_week)
        else:
            schedule = parsed_schedule[current_week][current_day_of_week]
            text = await build_schedule_message(
                lessons=schedule, day_of_the_week=current_day_of_week)
        await message.answer(text,
                             parse_mode='MarkdownV2',
                             reply_markup=get_keyboard())
    except Exception as e:
        logger.error(e)


async def main() -> None:
    logger.info("Bot started!")
    dp = Dispatcher()
    dp.include_router(router=router)
    token = bot_secret_token()
    bot = Bot(token=token)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit, SystemError):
        logger.info("Bot stopped!")
