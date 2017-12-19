# Borrowed from: https://github.com/tborychowski/py-bin

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re


def get_quality(name):
    qual = '?'
    if re.search(r'blu\-?(ray)?', name, flags=re.I): qual = 'BluRay'
    elif re.search('dvd(rip)?', name, flags=re.I): qual = 'DVDr'
    elif re.search('brrip', name, flags=re.I): qual = 'BR'
    elif re.search('hdrip', name, flags=re.I): qual = 'HD'
    elif re.search('dvdscrn?', name, flags=re.I): qual = 'DVDScr'
    elif re.search('r5', name, flags=re.I): qual = 'R5'
    elif re.search(r'web\-?(dl|rip)', name, flags=re.I): qual = 'Web'
    elif re.search('r6', name, flags=re.I): qual = 'R6'
    elif re.search('ts(rip)?', name, flags=re.I): qual = 'TS'
    elif re.search('cam(rip)?', name, flags=re.I): qual = 'Cam'
    elif re.search('hdtv?', name, flags=re.I): qual = 'HDTV'
    return qual


def get_year(name):
    year = re.search(r'(19|20)(\d{2})', name)
    if year: return re.sub(r'.*(19|20)(\d{2}).*', r'\1\2', name)
    else: return '?'


def get_age(name):
    return re.sub(r'^(\d+)(.+)(d|h)(\w+s?)$', r'\1\3', name)


def clean_name(name):
    cln = [
        '\\w264', 'mp3', 'xvid', 'divx', 'aac', 'ac3', '~', '[\\s|-]rip', 'download', 'dubbed',
        'shift', 'h?dts', '\\sts', '\\smd', 'juggs', 'prisak', 'rajonboy', 'YIFY', 'tamil', 'hd',
        'team', 'mafiaking', 'hon3y', 'publichd', 'unrated', 'truefrench', 'rarbg', 'tomcat12',
        'maniacs', 'd3si', 'sample', 'torrent', 'art3mis', 'french', 'akatsuki', 'utt', 'ddhrg',
        '(\\d{3,4}p)', '(\\d+mb)', '([x|\\d]+cd)', '\\s\\d', 'brrip', 'dvd(scr(n)?)?(rip)?',
        'blu\\-?ray', 'bdrip', 'h3ll2p4y', 'italian', 't4p3', 'vision', 'venum', 'carpediem',
        '(e\\-)?subs', 'hellraz0r', 'jyk', 'mms', 'titan', 'k3ly', 'presents00', 'destroy', 'sap',
        'hc', 'rip', 'aqos', 'web', 'readnfo', 'subtitles', 'dus', 'BL4CKP34RL', 'ShAaNiG', 'tnt',
        'new( good)? source', 'v2', 'millenium', 'newsource', 'dd5', 'dl', 'english', 'svr',
        'web\\-?dl', '(br|hd)rip', 'hdcam(rip)?', 'r5', 'r6', 'cam', 'sumo', 'webrip', 'ntsc',
        'evo\\s', 'evo$', 'blitzcrieg', 'oo0oo', 'hdtv', 'hdrip', 'rip', 'afg'
    ]
    name = re.sub(r'\.', ' ', name)                           # dots to spaces
    name = re.sub(r'\(?(19|20)(\d{2})\)?', ' ', name)         # remove year
    for i in cln: name = re.sub(i, '', name, flags=re.I)      # remove words
    name = re.sub(r'\[.*\]', '', name)                        # brackets
    name = re.sub(r'\{.*\}', '', name)                        # curly braces
    name = re.sub(r'\(.*\)', '', name)                        # parents
    name = re.sub(r'\s?\-+\s?', ' ', name)                    # dashes
    name = re.sub(r'\s{2,}', ' ', name)                       # double spaces
    return name.strip()


