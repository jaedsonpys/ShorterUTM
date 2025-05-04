import random
from typing import Optional


def _filter_empty_utm(utm_shorted: dict) -> dict:
    filtered_utm_shorted = dict()

    for name, value in utm_shorted.items():
        if value is not None:
            filtered_utm_shorted[name] = value

    return filtered_utm_shorted


class Shorter:
    @staticmethod
    def short(source: str = None, medium: str = None, campaign: str = None,
              term: Optional[str] = None, content: Optional[str] = None) -> tuple:
        short_code = random.randint(10000, 99999)

        utm_shorted = _filter_empty_utm({
            'utm_term': term,
            'utm_source': source,
            'utm_medium': medium,
            'utm_content': content,
            'utm_campaign': campaign
        })

        return short_code, utm_shorted
