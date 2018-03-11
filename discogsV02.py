# -*- coding: utf-8 -*-
import os
import discogs_client
os.system('clear')
d = discogs_client.Client('MyApp', user_token='fLXTTZLjyAmBngEXTESlYPBaeytveMGbbBYuFXOu')
group_in = raw_input('What Artist? ').upper()
title_in = raw_input('What Title? ').title()

res_out = d.search(group_in, type='master', artist=group_in, release_title=title_in)

def make_str(x):
    x = str(x).split('-')
    return x[0], x[1]

def get_id(x):
    y = x.split(' ')
    return y[1]

def cln_lst(lin):
    lst_cln = []
    for i in lin:
        trm = i[2].strip()
        if trm == title_in:
            lst_cln.append(i)
    return lst_cln

def cln_trk(trks):
    lst_cln = []
    for i in trks:
        srch = i
        srch =str(srch).replace('\"', '\'')
        srch = srch.split('\'')
        lst_cln.append(srch[3])

    return lst_cln


lst = []
for i in res_out.page(1):
    srch = i
    srch = str(srch).replace('\"', '\'')
    srch2 = srch.split('\'')
    grp_art, grp_tit = make_str(srch2[1])
    grp_mas = get_id(srch2[0])
    lst_snd = grp_mas, grp_art, grp_tit
    lst.append(lst_snd)


lst = cln_lst(lst)

for i in lst:
    rel_info = d.master(i[0])
    if len(rel_info.tracklist) > 5:
        print rel_info.tracklist
        pur_trk = cln_trk(rel_info.tracklist)
        break

print '\n\n'

for i in pur_trk:
    print i

print '\n\n'
