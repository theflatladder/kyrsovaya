#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Yandex translate API"""


import aiohttp
import json

from .helpers import *


class Yata(object):
    """Yandex translate API wrapper."""

    _url = 'https://translate.yandex.net/api/v1.5/tr.json'

    def __init__(self, key):
        """:key - Yandex translate API key."""

        self.key = key
        self._session = aiohttp.ClientSession()

    def __del__(self):
        self._session.close()


    async def translate(self, text, lang, frmt='plain'):
        """Translates text to the specified language.

        :text - Text to translate.
        :lang - The translation direction.
            You can set it in either of the following ways:

            As a pair of language codes separated by a hyphen (“from”-“to”). For example, en-ru indicates translating from English to Russian.
            As the target language code (for example, ru). In this case, the service tries to detect the source language automatically.
        :frmt - Text format.
            Possible values:
            ``plain`` - Text without markup (default value).
            ``html``  - Text in HTML format."""

        pl = {
            'key': self.key,
            'text': text,
            'lang': lang,
            'format': frmt
        }

        response = await post(self._session, f'{self._url}/translate', data=pl)
        return translation(json.loads(await response.text()))


    async def detect(self, text, hint=None):
        """Detect language of text.
        :text - The text to detect the language for.
        :hint - A list of the most likely languages (they will be given preference when detecting the text language). Use the comma as a separator."""

        pl = {
            'key': self.key,
            'text': text
        }

        if hint:
            pl['hint'] = hint

        response = await post(self._session, f'{self._url}/detect', data=pl)
        return lang(json.loads(await response.text()))


    async def langs(self, ui='en'):
        """Get list of supported languages.
        :ui - In the response, supported languages are listed in the langs field with the definitions of the language codes.
              Language names are output in the language corresponding to the code in this parameter."""

        pl = {
            'key': self.key,
            'ui': ui
        }

        response = await post(self._session, f'{self._url}/getLangs', data=pl)
        return langs(json.loads(await response.text()))
