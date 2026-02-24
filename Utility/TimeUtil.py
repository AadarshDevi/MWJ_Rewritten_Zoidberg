from time import time, sleep
from datetime import datetime


def timeStamp(dateTime: datetime | None = None) -> str:
    """
    datetime:
        type: datetime or None
        default value: None
    """
    if dateTime is None:
        dateTime = datetime.now()

    return str(dateTime)
