# -*- coding: utf-8 -*-
import os
import discogs_client
os.system('clear')
d = discogs_client.Client('MyApp', user_token='fLXTTZLjyAmBngEXTESlYPBaeytveMGbbBYuFXOu')
group_in = raw_input('What Artist? ').upper()
title_in = raw_input('What Title? ').title()

res_out = d.search(group_in, type='master', artist=group_in, release_title=title_in)
res_out2 = d.search(title_in, artist=group_in, type='release')

print len(res_out)
for i in res_out:
    print i

def prin_trx(trx):
    ret_trx = []
    for i in trx:
        ret_trx.append(i)
    return ret_trx


if res_out.pages >=1:
    extract = res_out.page(1)[0]
    extr_01 = extract.main_release
    extr_02 = extract.tracklist
    print extr_01
    print prin_trx(extr_02)
    #print dir(extract)
else:
    print "No pages found"
    exit()

artist = res_out2[0].artists[0]
print len(res_out2[0].artists)
print artist.name


print title_in
