import random
from typing import Optional
from urllib.parse import urlencode, parse_qs

import melkdb

from shortutm.exceptions import NotFoundShortedUTMError

ShortUTMDatabase = melkdb.MelkDB('ShortUTMDatabase')


def _filter_empty_utm(utm_shorted: dict) -> dict:
    filtered_utm_shorted = dict()

    for name, value in utm_shorted.items():
        if value is not None:
            filtered_utm_shorted[name] = value

    return filtered_utm_shorted


class Shorter:
    @staticmethod
    def save(short_code: str, utm_shorted: dict) -> None:
        utm_shorted_query = urlencode(utm_shorted)
        ShortUTMDatabase.add(short_code, utm_shorted_query)

    @staticmethod
    def restore(short_code: str) -> dict:
        utm_shorted_query = ShortUTMDatabase.get(short_code)

        if utm_shorted_query is None:
            raise NotFoundShortedUTMError

        utm_shorted = parse_qs(utm_shorted_query)
        return utm_shorted

    @staticmethod
    def short(source: str = None, medium: str = None, campaign: str = None,
              term: Optional[str] = None, content: Optional[str] = None) -> tuple:
        short_code = str(random.randint(10000, 99999))

        utm_shorted = _filter_empty_utm({
            'utm_term': term,
            'utm_source': source,
            'utm_medium': medium,
            'utm_content': content,
            'utm_campaign': campaign
        })

        return short_code, utm_shorted
