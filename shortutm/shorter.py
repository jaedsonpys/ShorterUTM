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


class ShorterUTM:
    @staticmethod
    def _save(utm_shorted: dict) -> str:
        while True:
            short_code = str(random.randint(100000, 999999))
            if ShortUTMDatabase.get(short_code) is None:
                break

        utm_shorted_query = urlencode(utm_shorted)
        ShortUTMDatabase.add(short_code, utm_shorted_query)

        return short_code

    @staticmethod
    def restore(short_code: str) -> dict:
        utm_shorted = dict()
        utm_shorted_query = ShortUTMDatabase.get(short_code)

        if utm_shorted_query is None:
            raise NotFoundShortedUTMError

        for param, value in parse_qs(utm_shorted_query).items():
            utm_shorted[param] = value[0]

        return utm_shorted

    @classmethod
    def short(cls, source: str = None, medium: str = None, campaign: str = None,
              term: Optional[str] = None, content: Optional[str] = None) -> str:
        utm_shorted = _filter_empty_utm({
            'utm_term': term,
            'utm_source': source,
            'utm_medium': medium,
            'utm_content': content,
            'utm_campaign': campaign
        })

        short_code = cls._save(utm_shorted)
        return short_code
