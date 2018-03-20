import korttipeli

korttipakka = korttipeli.DeckOfCards(52)
korttipakka.shuffle()

pelaajat = [korttipeli.Player('Kaappo1'), korttipeli.Player('Kaappo2'), korttipeli.Player('Kaappo3')]

pelaaja_käsi = [korttipeli.Cell(korttipeli.Card(visible=False)) for i in range(3)]

pöytä_käsi = [[]]

pelipöytä = korttipeli.Table(1, 1, pelaajat, korttipakka)
pelipöytä.deal(pelaaja_käsi, pöytä_käsi)

print(pelipöytä)

vuoro = 0
kierros = 1
while True:
    print('\nKierros {}\n'.format(kierros))

    vuoro = (vuoro + 1) % len(pelaajat)

    tarjoaja = pelaajat[vuoro]
    ottaja = pelaajat[(vuoro + 1) % len(pelaajat)]

    print('Pelaajan {} vuoro'.format(tarjoaja))
    # print(tarjoaja)

    tarjoajan_indeksi = int(input('Monesko kortti?')) - 1
    tarjottu_kortti = tarjoaja.drawCardFromHand(tarjoajan_indeksi)

    pelipöytä.putCardToTable(0, 0, tarjoaja, tarjoajan_indeksi)
    print(pelipöytä)

    print(ottaja)
    ottajan_indeksi = int(input('Monesko kortti?')) - 1

    ottava_kortti = ottaja.drawCardFromHand(ottajan_indeksi)
    pelipöytä.putCardToTable(0, 0, tarjoaja, ottajan_indeksi)

    if ottava_kortti.value > tarjottu_kortti:
        pass
    else:
        pass
