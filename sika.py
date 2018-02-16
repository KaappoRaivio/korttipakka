#!/usr/bin/python3

import korttipakka
import time

pakka = korttipakka.Korttipakka()
pakka.shuffle()

pöytä = korttipakka.Pelipöytä(1, 1)

pelaajien_määrä = int(input('Montako pelaajaa? '))
if pelaajien_määrä < 1:
    raise Exception('Et voi pelata ilman pelaajia!')

pelaajat = [input('Pelaaja: ') for x in range(pelaajien_määrä)]

for i in range(len(pelaajat)):
    pelaajat[i] = korttipakka.Pelaaja(pelaajat[i])
    pelaajat[i].jaaKortit(korttipakka.pokerikäsi, pakka)

pelaajaindeksi = 0

aloituskortti = pakka.otaKorttiPakanPäältä()

aloituskortti.paljastettu = True

pöytä.lyöKorttiPakasta(0, 0, pakka, kortti=aloituskortti)

print(pöytä)

while True:
    pelaajaindeksi %= pelaajien_määrä

    vuoro = pelaajat[pelaajaindeksi]

    if vuoro.korttien_määrä is 0:
        print('Henkilö {} voitti!'.format(vuoro))
        break

    print('Henkilön {} vuoro'.format(vuoro))
    print(pelaajat[pelaajaindeksi].printKäsi())

    kortti_kädestä = int(input('Mikä kortti? '))

    if kortti_kädestä > len(vuoro.käsi) - 1:
        print('Indeksi ei kelpaa!')
        continue
    sopiva_kortti = pöytä.noudaKortti(0, 0)

    if pelaajat[pelaajaindeksi].käsi[kortti_kädestä].arvo == 7:
        sopiva_kortti = korttipakka.Kortti(maa=input('Mitä maata? '))
        kortti_kädestä = int(input('Mikä kortti? '))

    if pelaajat[pelaajaindeksi].käsi[kortti_kädestä].maa == pöytä.noudaKortti(0, 0).maa or pelaajat[pelaajaindeksi].käsi[kortti_kädestä].arvo == pöytä.noudaKortti(0, 0).arvo:
        pöytä.lyöKortti(0, 0, pelaajat[pelaajaindeksi].käsi[kortti_kädestä], pelaajat[pelaajaindeksi])
    else:
        print('Tuo kortti ei mene!')
        nostettu_kortti = vuoro.nostaKortti(pakka)
        print(nostettu_kortti)
        time.sleep(1)
        if nostettu_kortti.maa == pöytä.noudaKortti(0, 0).maa or nostettu_kortti.arvo == pöytä.noudaKortti(0, 0).arvo:
            pöytä.lyöKortti(0, 0, nostettu_kortti, pelaajat[pelaajaindeksi])
        else:
            print('Tuokaan kortti ei mene!')

    print(pöytä)
    pelaajaindeksi += 1
