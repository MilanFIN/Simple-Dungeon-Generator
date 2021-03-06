import random



class mapCreator:
    def __init__(self):
        self.xAlku = 0
        self.yAlku = 0
        self.xSijainti = 0
        self.ySijainti = 0
        self.xKoko = 0
        self.yKoko = 0
        self.mapSizeX = 0
        self.mapSizeY = 0
    def mapMaker(self, xsize, ysize, RoomMin, RoomMax):
        #asetetaan kartan koko
        self.mapSizeX = xsize
        self.mapSizeY = ysize
        #luodaan 2d taulukko, joka täynnä # merkkejä
        self.kartta= [["#" for x in range(xsize)] for y in range(ysize)]
        #arvotaan ensimmäisen huoneen koko
        self.xKoko = random.randint(RoomMin, RoomMax)
        self.yKoko = random.randint(RoomMin, RoomMax)
        #1. huoneen vasemman yläkulman sijainti, siten ettei oikea alakulma ylitä kartan reunoja!
        self.xSijainti = random.randint(0, xsize -self.xKoko)
        self.ySijainti = random.randint(0, ysize -self.yKoko)
        #seuraava kutsuu huoneenluojafunktion!
        self.makeRoom(self.xSijainti, self.ySijainti, self.xKoko, self.yKoko)
        #seuraava luo 1. numeron ekaan huoneeseen
        for y in range(1 ):
            for x in range(1):
                self.kartta[self.ySijainti][self.xSijainti] = "1"
        kaikkiSuunnat = ["up", "down", "left", "right"] #luo lista suunnista
        while True:#tekee toisen ja kolmannen jne huoneen
            uusiKokoX = random.randint(4, 8)
            uusiKokoY = random.randint(4, 8)

            if not kaikkiSuunnat : #lopetetaan ohjelma, jos on yritetty tehdä käytävä
                for y in range(1 ):
                    for x in range(1):
                        self.kartta[self.ySijainti][self.xSijainti] = "2" #tee merkki vikaan huoneeseen
                break
            #suunta = "down"
            suunta = random.choice(kaikkiSuunnat)
            if suunta == "up":
                uusiSijaintiX = self.xSijainti +  random.randint(-1, 1) #uuden huoneen x ja y koordinaatit, vanhat säästetään ja muutetaan kun keritään
                uusiSijaintiY = self.ySijainti - uusiKokoY - 1
                oviX = self.xSijainti + 2 #oven sijainti
                oviY = self.ySijainti - 1
            elif suunta == "down": #yrittää luoda huoneen alapuolelle
                uusiSijaintiX = self.xSijainti +  random.randint(-1, 1) #uuden huoneen x ja y koordinaatit, vanhat säästetään ja muutetaan kun keritään
                uusiSijaintiY = self.ySijainti + self.yKoko + 1
                oviX = self.xSijainti + 2 #oven sijainti
                oviY = uusiSijaintiY -1
            elif suunta == "left":
                uusiSijaintiX = self.xSijainti - uusiKokoX - 1 #uuden huoneen x ja y koordinaatit, vanhat säästetään ja muutetaan kun keritään
                uusiSijaintiY = self.ySijainti + random.randint(-1, 1)
                oviX = self.xSijainti - 1 #oven sijainti
                oviY = self.ySijainti  + 2
            elif suunta == "right":
                uusiSijaintiX = self.xSijainti + self.xKoko + 1  #uuden huoneen x ja y koordinaatit, vanhat säästetään ja muutetaan kun keritään
                uusiSijaintiY = self.ySijainti + random.randint(-1, 1)
                oviX = uusiSijaintiX - 1  #oven sijainti
                oviY = uusiSijaintiY  +2

            if (self.enoughRoom(uusiSijaintiX, uusiSijaintiY, uusiKokoX, uusiKokoY, xsize, ysize)) == True: #testaa voidaanko piirtää huone
                self.makeRoom(uusiSijaintiX, uusiSijaintiY, uusiKokoX, uusiKokoY) #luo huone
                self.makeRoom(oviX, oviY, 1, 1) #luo oven
                self.xSijainti = uusiSijaintiX
                self.ySijainti = uusiSijaintiY
                self.xKoko = uusiKokoX
                self.yKoko = uusiKokoY
                kaikkiSuunnat = ["up", "down", "left", "right"]
            else:
                kaikkiSuunnat.remove(suunta)
        return self.kartta

    def enoughRoom(self, xlocation, ylocation, xlength, ylength, xsize, ysize): #tämä tarkistaa, onko seuraavalle huoneelle tilaa kartalla, palauttaa true/false vastauksen
        palautettava = True
        if xlocation + xlength + 1 <= xsize and ylocation + ylength + 1 <= ysize and xlocation - 1 >= 0 and ylocation - 1 >= 0: #testaa, meneekö huone kartan yli!
            for y in range (ylength + 2):
                for x in range (xlength + 2):
                    if self.kartta[ylocation + y - 1][xlocation + x - 1] == "#":#testaa onko kyseinen ruutu seinää
                        pass
                    else:
                        palautettava = False
        else:
            palautettava = False
        return palautettava

    def makeRoom(self, xlocation, ylocation, xlength, ylength): #tämä luo uuden huoneen, ei välitä onko koordinaatit oikein, joten enoughRoom() pitää ajaa ensin!
        for y in range(ylength ):
            for x in range(xlength ):
                self.kartta[ylocation + y][xlocation + x] = "."

    def printMap(self):
        for y in range(50):
            for x in range(70):
                #print (y)
                print (self.kartta[y][x], end="")
            print ("")
    def getMap(self):
        return self.kartta
    def save(self, polku = "map.txt"):
        text_file = open(polku, "w")
        kirjoitettava = ""
        for y in range(self.mapSizeY ):
            for x in range(self.mapSizeX ):
                kirjoitettava += self.kartta[y][x]
            kirjoitettava += "\n"
        text_file.write(kirjoitettava)
        text_file.close()

#creating example map with parameters: (map width, map height, min. roomsize, max roomsize.)
#mapcreator = mapCreator()
#mapcreator.mapMaker(70, 50, 4, 8)
#mapcreator.printMap()
#mapcreator.save()




