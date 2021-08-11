#!/usr/bin/env python3
"""
filter_datum returns the log message:
"""


from typing import List
import logging
import re


def filter_datum(
            fields: List[str],
            redaction: str,
            message: str,
            separator: str
            ) -> str:
    """
    a function that hides all the personal,
    sensitve informations.
    """
    for field in fields:
        message = re.sub("{}=([a-zA-Z0-9\\/]+){}".format(field, separator),
                         field + "=" + redaction + separator,  message)
    return message
