# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:45:33 2018
p146
@author: ACANTAMA
"""

def make_album(artist_name, album_title, tracks=''):
    """Returns a dictionary that includes artist name, album title and track number (optional)"""
    music = {'artist': artist_name.title(), 'album': album_title.title()}
    if tracks:
        music['tracks'] = tracks
    return music
    
music_inquiry = make_album('pink floyd', 'the dark side of the moon', tracks=10)
print(music_inquiry)

music_inquiry = make_album('the beatles', 'abbey road')
print(music_inquiry)

music_inquiry = make_album('led zeppelin', 'houses of the holy', tracks=12)
print(music_inquiry)

music_inquiry = make_album('the beatles', 'revolver')
print(music_inquiry)

