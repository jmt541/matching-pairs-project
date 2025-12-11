import pygame
import random
from linkedList import LinkedList
from stack import Stack
from card import Card


pygame.init()
pygame.mixer.init()

# background music
# pygame.mixer.music.load("asset/music/pygame-music.mp3")
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(-1)

jumlahSalah = 0

def generateGrid(rows, cols, startX, startY, spacing, cardWidth, cardHeight):
        posisi = []

        for i in range (rows):
                for j in range(cols):
                        x = startX + j * (cardWidth + spacing)
                        y = startY + i * (cardHeight + spacing)
                        posisi.append((x,y))

        return posisi


# def pushKartuKeStack(card, stackKartu, push_object=True):
 
#     if push_object:
#         stackKartu.push(card)
#         print("push object:", card.value)
#     else:
#         stackKartu.push(card.value)
#         print("push value:", card.value)




def eventHandleClickHistoryStack(event, kartuFinal, stackKartu, historyStack):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

        for card in kartuFinal:
            if card.rect.collidepoint(mouse_pos) and not card.flipped and not card.matched:
                card.flipped = True

                stackKartu.push(card)

                historyStack.push(card.rect.topleft)

                print("history push posisi->", card.rect.topleft)
                break









# def eventHandleClick(event, kartuFinal, stackKartu):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()

#                 for card in kartuFinal:
#                         if card.rect.collidepoint(mouse_pos) and not card.flipped and not card.matched:
#                                  card.flipped = True
#                                  pushKartuKeStack(card, stackKartu)


def showHistoryNoMatchStackHistory(kartuFinal, historyStack, screen, background):

    while historyStack.size() > 0:
        pos = historyStack.pop()

    

        for card in kartuFinal:
            if card.rect.topleft == pos and not card.matched:
                card.flipped = True

                screen.blit(background, (0,0))
                for k in kartuFinal:
                    k.draw(screen)

                pygame.display.flip()
                pygame.time.delay(800)

                card.flipped = False
                break



# def showHistoryNoMatch(kartuFinal, history_kartu_nomatch, screen, background):
#         for i in range(history_kartu_nomatch.getSize()):
#                 value = history_kartu_nomatch.getValueAtIndex(i)



 

#                 for card in kartuFinal:
                        

#                         if card.value == value and not card.matched:
#                                 card.flipped = True

#                                 screen.blit(background, (0,0))

#                                 for k in kartuFinal:
#                                         k.draw(screen)

                                
#                                 pygame.display.flip()
#                                 pygame.time.delay(800)
#                                 card.flipped = False
#                                 break

                        




def compareKartuDiStack_History(stackKartu, historyStack):
    global jumlahSalah

    if stackKartu.size() == 2:
        card2 = stackKartu.pop()
        card1 = stackKartu.pop()

        if card1.value == card2.value:
            print("match!", card1.value)

            card1.matched = True
            card2.matched = True

            if card1.value == 1:
                showHistoryNoMatchStackHistory(kartuFinal, historyStack, screen, background_image)

        else:
            jumlahSalah += 1
            print("no match!")

            pygame.time.delay(500)

            card1.flipped = False
            card2.flipped = False






# def compareKartuDiStack(stackKartu, history_kartu_nomatch):
#         global jumlahSalah

#         if stackKartu.size() == 2:
#                 card2 = stackKartu.pop()
#                 card1 = stackKartu.pop()


#                 if card1.value == card2.value:
#                         print ("match!", card1.value)

#                         history_kartu_nomatch.remove(card1.value)

#                         card1.matched = True
#                         card2.matched = True


#                         if (card1.value == 1):
#                                 showHistoryNoMatch(kartuFinal, history_kartu_nomatch, screen, background_image)


                
                                
                        



                        
#                 else:


#                         jumlahSalah += 1
                      
#                         history_kartu_nomatch.append(card1.value, None)
#                         history_kartu_nomatch.append(card2.value, None)

#                         pygame.time.delay(600) 

#                         print ("no match!")
                        
#                         card1.flipped = False


#                         card2.flipped = False




                        





#load asset
background_image = pygame.image.load("asset/background.png")
Card.loadAssetKartuBelakang()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("test window")
clock = pygame.time.Clock()

#buat deck kartu 4x4
values = LinkedList()
for i in range(1, 9):
        kartuDepanGambar = f"asset/card/front/{i}.png"
        values.append(i, kartuDepanGambar)
        values.append(i, kartuDepanGambar) #di append ke LL dua kali karena deck harus semua ada pair





#linked list buat simpan history kartu tidak match
#history_kartu_nomatch = LinkedList()









posisi = generateGrid(

        rows = 4, cols = 4,
        startX = 420, startY = 110,
        spacing = 10,
        cardWidth = 87, cardHeight = 132

)



values.shuffle()

temp = values.head
kartuFinal = []

for (x, y) in posisi:
    card = Card(
        kartuDepanPath=temp.kartuDepanPath,
        value=temp.value,
        x=x,
        y=y
    )
    kartuFinal.append(card)
    temp = temp.next




#load stack
stackKartu = Stack()


#stack untuk history
historyStack = Stack()







running = True

while running:
        # membaca semua event
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False



                # method eventHandleclick melihat apakah player click mouse, dan jika click mouse, kartu yang di klik di push ke stack 
                #eventHandleClick(event, kartuFinal, stackKartu)


                #method eventHandleClick stack history
                eventHandleClickHistoryStack(event, kartuFinal, stackKartu, historyStack)











        screen.fill((30,30,30))
        screen.blit(background_image, (0,0))


        for card in kartuFinal:
                card.draw(screen)


        pygame.display.flip()

        #lalu di compare dengan method ini

        #compareKartuDiStack(stackKartu, history_kartu_nomatch)
        compareKartuDiStack_History(stackKartu, historyStack)

        if jumlahSalah == 100:
                running = False



pygame.quit()      






