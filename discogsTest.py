# -*- coding: utf-8 -*-
import os
import discogs_client
os.system('clear')
d = discogs_client.Client('MyApp', user_token='fLXTTZLjyAmBngEXTESlYPBaeytveMGbbBYuFXOu')
group_in = raw_input('What Artist? ').upper()
title_in = raw_input('What Title? ').title()

res_out = d.search(group_in, type='master', artist=group_in, release_title=title_in)
res_out2 = d.search(title_in, artist=group_in, type='release')

print len(res_out2)

print res_out.pages
extract = res_out.page(1)[0].title
print extract

artist = res_out2[0].artists[0]
print artist.name
print artist.id

print title_in

for i in res_out.page(1):
    row = i.title.split('-')
    if row[1].strip() == title_in:
        print row[1].strip()

print len(extract)
