from models.lesson import Lesson, lesson_init
from service.take_schedule import take_schedule


def parse_schedule() -> list[list[list[Lesson]]]:
    unparsed_weeks_schedule = take_schedule()[0]["schedule"]
    parsed_schedule = []
    for week_number in range(1, 17):
        week_schedule = []
        for day in unparsed_weeks_schedule:
            lessons_list = []
            if not week_number % 2:
                for lesson_number, lesson in enumerate(day["even"]):
                    if lesson:
                        if lesson[0]["weeks"]:
                            for special_lesson_week_number in lesson[0][
                                    "weeks"]:
                                if special_lesson_week_number == week_number:
                                    lessons_list.append(
                                        lesson_init(
                                            lesson=lesson[0],
                                            lesson_number=lesson_number))
                        else:
                            lessons_list.append(
                                lesson_init(lesson=lesson[0],
                                            lesson_number=lesson_number))
            else:
                for lesson_number, lesson in enumerate(day["odd"]):
                    if lesson:
                        if lesson[0]["weeks"]:
                            for special_lesson_week_number in lesson[0][
                                    "weeks"]:
                                if special_lesson_week_number == week_number:
                                    lessons_list.append(
                                        lesson_init(
                                            lesson=lesson[0],
                                            lesson_number=lesson_number))
                        else:
                            lessons_list.append(
                                lesson_init(lesson=lesson[0],
                                            lesson_number=lesson_number))
            week_schedule.append(lessons_list)
        parsed_schedule.append(week_schedule)
    return parsed_schedule
