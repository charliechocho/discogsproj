# -*- coding: utf-8 -*-

import discogs_client
d = discogs_client.Client('MyApp', user_token='fLXTTZLjyAmBngEXTESlYPBaeytveMGbbBYuFXOu')

# res_out = d.search('Abba', artist='Abba', release_title='arrival')
res_out = d.search('Abba', type='master', artist='Abba', release_title='Waterloo')
print res_out.pages

print res_out.page(1)
# print '\n\n'
clean_tx = res_out[0]
clean_tx = str(clean_tx)
clean_tx = clean_tx[8:].split()
m_rec = clean_tx[0]
rel_info = d.master(m_rec)
print rel_info.title
# print rel_info.artists
print '\n\n'
print rel_info.tracklist
print '\n\n'
for trck in rel_info.tracklist:
    print trck

print '\n\n'
trck = rel_info.tracklist[5]
print '\n\n'
trck = str(trck)
trk_li = trck.split('\'')
print trk_li
