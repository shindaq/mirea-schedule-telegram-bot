from dataclasses import dataclass
import json


@dataclass
class Lesson:
    number: int
    name: str
    type: str
    time: str
    tutor: str
    location: str


_lessons_times = [
    "09:00 - 10:30", "10:40 - 12:10", "12:40 - 14:10", "14:20 - 15:50",
    "16:20 - 17:50", "18:00 - 19:30", "19:40 - 21:10"
]


def lesson_init(lesson: json, lesson_number: int) -> Lesson:
    return Lesson(lesson_number + 1, lesson["name"], lesson["type"],
                  _lessons_times[lesson_number], lesson["tutor"],
                  lesson["place"])
