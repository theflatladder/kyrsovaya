#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import async_timeout

from itertools import chain, repeat

from aiohttp import web, ClientSession
from urllib.parse import quote, unquote, urljoin

from bs4 import BeautifulSoup

from yata import Yata



project_root = '.'
translate_ct = {'text/html', 'text/plain'}
yata = None

host, port = '127.1', 8080



def set_proxy(html, url, lang):
    soup = BeautifulSoup(html, 'html.parser')

    for elem, prop in chain(zip(soup.find_all(href=True), repeat('href')),
                            zip(soup.find_all(src=True),  repeat('src'))):
        elem[prop] = urljoin(url, elem[prop])


    for a in soup.find_all('a', href=True):
        a['href'] = f'/proxy?url={quote(a["href"])}&lang={lang}'

    return str(soup)


async def handle_translate(request):
    url = unquote(request.rel_url.query.get('url'))
    lang = request.rel_url.query.get('lang') or 'en'

    if not url:
        return web.Response(status=404)


    with async_timeout.timeout(10):
        async with ClientSession() as session, session.get(url) as response:
            if response.status != 200:
                return web.Response(status=response.status)

            content_type = response.content_type
            text = await response.text()

            if content_type in translate_ct:
                text = set_proxy(text, url, lang)

                translation = await yata.translate(text, lang, 'html')

                if translation.ok:
                    return web.Response(text=translation.text, content_type=content_type)
                else:
                    return web.Response(status=translation.code)
            else:
                return web.Response(text=text, content_type=content_type)

    return web.Response(status=503)


async def handle_index(request):
    return web.FileResponse('static/index.html')


if __name__ == '__main__':
    yata = Yata(sys.argv[1])

    app = web.Application()

    app.router.add_get('/proxy', handle_translate)
    app.router.add_get('/', handle_index)
    app.router.add_static('/', path='static/')

    web.run_app(app, host=host, port=port)
