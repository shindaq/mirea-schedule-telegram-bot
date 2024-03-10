from emoji import emojize
from models.lesson import Lesson

_days_of_the_week = [
    "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота",
    "Воскресенье"
]

_markdownv2_escapable_chars = {
    '`': '\`',
    #'*': '\*',
    '_': '\_',
    '{': '\{',
    '}': '\}',
    '[': '\[',
    ']': '\]',
    '<': '\<',
    '>': '\>',
    '(': '\(',
    ')': '\)',
    '#': '\#',
    '+': '\+',
    '-': '\-',
    '.': '\.',
    '!': '\!',
    '|': '\|'
}


def _markdownv2_escape(text: str) -> str:
    escaped_str = ""
    for symbol in text:
        if symbol in _markdownv2_escapable_chars:
            escaped_str += _markdownv2_escapable_chars[symbol]
        else:
            escaped_str += symbol
    return escaped_str


async def build_schedule_message(lessons: list[Lesson],
                                 day_of_the_week: int) -> str:
    if not lessons:
        return _markdownv2_escape(text=emojize(
            f"*{_days_of_the_week[day_of_the_week]}*\nПар нет!:clinking_beer_mugs:"
        ))
    message = f"*{_days_of_the_week[day_of_the_week]}*\n"
    for lesson in lessons:
        message += f"*Пара №{lesson.number}*\n"
        message += emojize(
            f":notebook_with_decorative_cover:: {lesson.name} — {lesson.type}\n"
        )
        message += emojize(f":alarm_clock:: {lesson.time}\n")
        message += emojize(f":man:: {lesson.tutor}\n")
        message += emojize(f":department_store:: {lesson.location}\n\n")
    return _markdownv2_escape(text=message)
