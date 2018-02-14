import korttipakka

pakka = korttipakka.Korttipakka()
pakka.shuffle()

pöytä = korttipakka.Pelipöytä(1, 1)


# while True:
pelaajaindeksi = 0

pelaajien_määrä = int(input('Montako pelaajaa? '))
pelaajat = [input('Pelaaja: ') for x in range(pelaajien_määrä)]

for i in range(len(pelaajat)):
    pelaajat[i] = korttipakka.Pelaaja(pelaajat[i])
    pelaajat[i].jaaKortit(korttipakka.pokerikäsi, pakka)

    print(pelaajat[i])

vuoro = pelaajat[pelaajaindeksi]

print('Henkilön {} vuoro'.format(vuoro))
print(pelaajat[pelaajaindeksi].printKäsi())
pöytä.lyöKortti(0, 0, pelaajat[pelaajaindeksi].käsi[int(input('Mikä kortti? '))], pelaajat[pelaajaindeksi])
# print(pöytä)
