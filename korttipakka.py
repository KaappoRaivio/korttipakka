import random


class Kortti(object):
    def __init__(self, maa=None, arvo=None, paljastettu=False):
        self.maa = maa
        self.arvo = arvo
        self.paljastettu = paljastettu

    def __str__(self):
        # if not self.paljastettu:
        #     return "piilotettu"
        return "{}-{}".format(self.maa, self.arvo)


class Korttipakka(object):
    def __init__(self, maat=['Ruutu', 'Risti', 'Hertta', 'Pata'], arvot=range(2, 15)):
        self.kortit = []
        self.maat = maat
        self.arvot = arvot
        for i in maat:
            for a in arvot:
                self.kortit.append(Kortti(i, a))

    def __str__(self):
        temp = ''
        for i in self.kortit:
            temp += str(i)
            temp += ', '
        temp = temp[:len(temp) - 2]  # Poistetaan viimeinen pilkku.
        return temp

    def shuffle(self):
        for i in range(len(self.kortit) - 1, 0, -1):
            random_indeksi = random.randint(0, i - 1)
            self.kortit[random_indeksi], self.kortit[i] = self.kortit[i], self.kortit[random_indeksi]

    def otaKorttiPakanPäältä(self):
        kortti = self.kortit[0]
        self.kortit = self.kortit[1:]
        return kortti

    def laitaKorttiPakkaan(self, kortti):
        if str(kortti) in str(self.kortit):
            raise Exception('Kortti on jo pakassa!')
        else:
            # self.kortit = self.kortit[:random_paikka], kortti, self.kortit[random_paikka + 1:]
            self.kortit.append(kortti)
            self.shuffle()


class Template(object):
    def __init__(self, lista):
        self.lista = lista

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, index):
        return self.lista[index]


class Pelaaja(object):
    def __init__(self, nimi):
        self.nimi = nimi
        self.käsi = []
        self.korttien_määrä = len(self.käsi)

    def jaaKortit(self, template, jaettava_pakka):
        for i in range(len(template)):
            jaettava_kortti = jaettava_pakka.otaKorttiPakanPäältä()
            jaettava_kortti.paljastettu = template[i].paljastettu
            self.käsi.append(jaettava_kortti)
            self.korttien_määrä = len(self.käsi)

    def paljastaKortti(self, indeksi):
        self.käsi[indeksi].paljastettu = True

    def __str__(self):
        return self.nimi

    def printKäsi(self):
        temp = ''
        for i in self.käsi:
            temp += str(i)
            temp += ', '

        temp = temp[:len(temp) - 2]  # viimeinen pillku pois.
        return temp


class Pelipöytä(object):
    korttien_esitystapa = {'Ruutu': '♢', 'Risti': '♧', 'Pata': '♤', 'Hertta': '♡'}

    def __init__(self, koko_x, koko_y):
        self.koko_x = koko_x
        self.koko_y = koko_y
        self.kortit = [['0'] * koko_x] * koko_y
        for x in range(koko_x):
            for y in range(koko_y):
                self.kortit[x][y] = Kortti(paljastettu=False)
        print(self.kortit)

    def __str__(self):
        temp = ''
        for x in range(self.koko_x):
            for y in range(self.koko_y):
                if self.noudaKortti(x, y).maa is None:
                    temp += '0'
                else:
                    temp += '{}{}'.format(Pelipöytä.korttien_esitystapa[self.noudaKortti(x, y).maa], str(self.noudaKortti(x, y).arvo))
            temp += '\n'
        return temp

    def noudaKortti(self, x, y):
        return self.kortit[x][y]

    def lyöKortti(self, x, y, kortti, pelaaja):
        for i in range(len(pelaaja.käsi)):
            pelaaja.käsi[i].paljastettu = True  # Väliaikainen

        if str(kortti) in pelaaja.printKäsi():
            self.kortit[x][y] = kortti
            pelaaja.käsi.remove(kortti)
            pelaaja.korttien_määrä = len(pelaaja.käsi)
        else:
            print('Pelaaja {} ei voi laittaa pöytään korttia {}'.format(pelaaja, kortti))

        for i in range(len(pelaaja.käsi)):
            pelaaja.käsi[i].paljastettu = False

    def lyöKorttiPakasta(self, x, y, pakka):
        self.kortit[x][y] = pakka.otaKorttiPakanPäältä()


pokerikäsi = Template([Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False)])
