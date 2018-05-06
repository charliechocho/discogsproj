# -*- coding: utf-8 -*-
import os
import discogs_client
os.system('clear')
d = discogs_client.Client('MyApp', user_token='fLXTTZLjyAmBngEXTESlYPBaeytveMGbbBYuFXOu')
#group_in = raw_input('What Artist? ').upper()
#title_in = raw_input('What Title? ').title()

#res_out = d.search(group_in, type='master', artist=group_in, release_title=title_in)
#rel_out = d.search(group_in, artist=group_in, type='artist')[0].releases[1]
artist = d.artist('abba')
print artist
