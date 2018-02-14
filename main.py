import korttipakka

pakka = korttipakka.Korttipakka()
pakka.shuffle()

pöytä = korttipakka.Pelipöytä(10, 10)


while True:
    komento = input('Mitä haluat tehdä? ')
    print(komento.lower())
    if komento.lower() == 'uusi peli':
        pelaajien_määrä = int(input('Montako pelaajaa? '))
        pelaajat = [input('Pelaaja: ') for x in range(pelaajien_määrä)]
        for i in range(len(pelaajat)):
            pelaajat[i] = korttipakka.Pelaaja(i)
            pelaajat[i].jaaKortit(korttipakka.pokerikäsi, pakka)
            print(pelaajat[i])
