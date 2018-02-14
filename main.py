import random


class Kortti(object):
    def __init__(self, maa=None, arvo=None, paljastettu=False):
        self.maa = maa
        self.arvo = arvo
        self.paljastettu = paljastettu

    def __str__(self):
        if not self.paljastettu:
            return "hidden"
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

    def jaaKortit(self, template, jaettava_pakka):
        for i in range(len(template)):
            jaettava_kortti = jaettava_pakka.otaKorttiPakanPäältä()
            jaettava_kortti.paljastettu = template[i].paljastettu
            self.käsi.append(jaettava_kortti)

pokerikäsi = Template([Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False), Kortti(paljastettu=False)])

korttipakka = Korttipakka()
korttipakka.shuffle()

kaappo = Pelaaja('Kaappo')
kaappo.jaaKortit(pokerikäsi, korttipakka)

print(kaappo.käsi)
