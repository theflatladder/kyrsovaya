#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import ClientSession


class lang(object):
    """Language code."""

    def __init__(self, response):
        self.ok = response['code'] == 200

        if self.ok:
            self.lang = response['lang']
        else:
            self.msg = response['message']


class langs(object):
    """List of supported languages."""

    def __init__(self, response):
        self.response = response

        self.code = response.get('code', 200)
        self.ok = self.code == 200

        if self.ok:
            self.langs = response['langs']
        else:
            self.msg = response['message']


class translation(object):
    """Translation."""

    def __init__(self, response):
        self.response = response
        self.code = response['code']
        self.ok = self.code == 200

        if self.ok:
            self.text = response['text'][0]
            self.lang = response['lang']
        else:
            self.msg = response['message']


async def post(session, url, data):
    async with session.post(url, data=data) as response:
        return response
