import pygame
import random
from linkedList import LinkedList
from card import Card


pygame.init()


def generateGrid(rows, cols, startX, startY, spacing, cardWidth, cardHeight):
        posisi = []

        for i in range (rows):
                for j in range(cols):
                        x = startX + j * (cardWidth + spacing)
                        y = startY + i * (cardHeight + spacing)
                        posisi.append((x,y))

        return posisi






#load asset
background_image = pygame.image.load("asset/background.png")
Card.loadAssetKartuBelakang()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("test window")


#buat deck kartu 4x4
values = LinkedList()
for i in range(1, 9):
        kartuDepanGambar = f"asset/card/front/{i}.png"
        values.append(i, kartuDepanGambar)
        values.append(i, kartuDepanGambar) #di append ke LL dua kali karena deck harus semua ada pair

# di ubah ke python list untuk bisa menggunakan library random buat di shuffle
valuePyList = values.convertList()
random.shuffle(valuePyList)


posisi = generateGrid(

        rows = 4, cols = 4,
        startX = 50, startY = 50,
        spacing = 10,
        cardWidth = 87, cardHeight = 132




)

kartuFinal = []

for ((value, img), (x, y)) in zip (valuePyList, posisi):
    card = Card(kartuDepanPath = img, value = value, x = x, y = y)


    kartuFinal.append(card)



















running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        screen.fill((30,30,30))

        screen.blit(background_image, (0,0))
        pygame.display.flip()


pygame.quit()      






