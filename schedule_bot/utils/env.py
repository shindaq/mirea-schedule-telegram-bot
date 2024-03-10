import os


def bot_secret_token() -> str:
    secret = os.getenv("BOT_SECRET")
    if not secret:
        return ""
    return secret


def group_name() -> str:
    name = os.getenv("GROUP_NAME")
    if not name:
        return ""
    return name


def api_schedule_endpoint() -> str:
    endpoint = os.getenv("MIREA_GET_SCHEDULE_ENDPOINT")
    if not endpoint:
        return ""
    return endpoint


def api_week_endpoint() -> str:
    endpoint = os.getenv("GET_CURRENT_WEEK_ENDPOINT")
    if not endpoint:
        return ""
    return endpoint
