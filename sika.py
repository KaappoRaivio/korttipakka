import korttipakka

pakka = korttipakka.Korttipakka()
pakka.shuffle()

pöytä = korttipakka.Pelipöytä(1, 1)

pelaajien_määrä = int(input('Montako pelaajaa? '))
pelaajat = [input('Pelaaja: ') for x in range(pelaajien_määrä)]

for i in range(len(pelaajat)):
    pelaajat[i] = korttipakka.Pelaaja(pelaajat[i])
    pelaajat[i].jaaKortit(korttipakka.pokerikäsi, pakka)

pelaajaindeksi = 0

pöytä.lyöKorttiPakasta(0, 0, pakka)
print(pöytä)

while True:
    pelaajaindeksi %= pelaajien_määrä
    print(pelaajat[i])

    vuoro = pelaajat[pelaajaindeksi]

    if vuoro.korttien_määrä is 0:
        print('Henkilö {} voitti!'.format(vuoro))
        break

    print('Henkilön {} vuoro'.format(vuoro))
    print(pelaajat[pelaajaindeksi].printKäsi())

    kortti_kädestä = int(input('Mikä kortti? '))
    if pelaajat[pelaajaindeksi].käsi[kortti_kädestä].maa == pöytä.noudaKortti(0, 0).maa or pelaajat[pelaajaindeksi].käsi[kortti_kädestä].arvo == pöytä.noudaKortti(0, 0).arvo:
        pöytä.lyöKortti(0, 0, pelaajat[pelaajaindeksi].käsi[kortti_kädestä], pelaajat[pelaajaindeksi])
    else:
        print('Tuo kortti ei mene!')

    print(pöytä)
    pelaajaindeksi += 1
