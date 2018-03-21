import korttipeli
from stack import Stack

korttipakka = korttipeli.DeckOfCards(52)
korttipakka.shuffle()

pelaajat = [korttipeli.Player(x, RFG_pile=True) for x in ['Kaappo{}'.format(i) for i in range(1, 4)]]

pelaaja_käsi = [korttipeli.Cell(korttipeli.Card(visible=False)) for i in range(3)]

pöytä_käsi = [[]]

pelipöytä = korttipeli.Table(1, 1, pelaajat, korttipakka)
pelipöytä.deal(pelaaja_käsi, pöytä_käsi)


vuoro = -1
kierros = 0
while True:
    kierros += 1
    print('\nKierros {}\n'.format(kierros))
    print(pelipöytä)

    vuoro = (vuoro + 1) % len(pelaajat)

    tarjoaja = pelaajat[vuoro]
    ottaja = pelaajat[(vuoro + 1) % len(pelaajat)]

    print('Pelaajan {} vuoro'.format(tarjoaja))
    # print(tarjoaja)

    tarjoajan_indeksi = int(input('Monesko kortti?')) - 1
    tarjottu_kortti = tarjoaja.drawCardFromHand(tarjoajan_indeksi)
    tarjoaja.addCardToHand(Stack(korttipakka.drawCard()))

    print(str(tarjoaja)  + 'asd\n')


    pelipöytä.putCardToTable(0, 0, tarjoaja, tarjoajan_indeksi)

    print(pelipöytä)
    print(ottaja)

    ottajan_indeksi = int(input('Monesko kortti?')) - 1
    ottava_kortti = ottaja.drawCardFromHand(ottajan_indeksi)
    ottaja.addCardToHand(Stack(korttipakka.drawCard()))


    pelipöytä.putCardToTable(0, 0, tarjoaja, ottajan_indeksi)

    print(pelipöytä)

    if ottava_kortti > tarjottu_kortti:
        ottaja.RFG_pile.append(pelipöytä.takeCardFromTable(0, 0))
        ottaja.RFG_pile.append(pelipöytä.takeCardFromTable(0, 0))
    else:
        tarjoaja.RFG_pile.append(pelipöytä.takeCardFromTable(0, 0))
        tarjoaja.RFG_pile.append(pelipöytä.takeCardFromTable(0, 0))

    print(pelipöytä)
