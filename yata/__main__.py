#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import argparse
import requests

from yata import Yata


def create_parser():
    parser = argparse.ArgumentParser(
        prog='Yata',
        epilog='(c) Anton Matveev 2017. All right reserved.')

    parser.add_argument('-k', '--api-key',
                        required='True',
                        type=str,
                        help='Yandex translate API key.')

    group = parser.add_mutually_exclusive_group()


    group.add_argument('-t', '--text',
                        type=str,
                        help='Text to translate.')

    group.add_argument('-u', '--url',
                        type=str,
                        help='Translate web page.')

    parser.add_argument('-l', '--lang',
                        type=str,
                        help='Translation direction.')

    parser.add_argument('-f', '--format',
                        default='plain',
                        type=str,
                        help='Text format.')

    return parser



if __name__ == "__main__":
    if sys.version_info < (3, 6):
        sys.exit('Python 3.6 or later is required.\n')

    parser = create_parser()
    params = parser.parse_args(sys.argv[1:])

    key, text, url, lang, frmt = params.api_key, params.text, params.url, params.lang, params.format


    yata = Yata(key)

    if url:
        page = requests.get(url)

        if page.ok:
            response = yata.translate(page.content.decode(), lang, 'html')
    else:
        response = yata.translate(text, lang, frmt)

    if response.ok:
        print(response.text)
    else:
        print(response.response)
