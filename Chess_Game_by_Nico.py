import pygame
import time
pygame.init()

case_B = (238, 192, 122)
interieur_color = (112, 153, 140)
ecrit_color = (23, 89, 155)
fond_color = (111, 74, 16)
place_case = ["TB1", "PB1", "V", "V", "V", "V", "PN1", "TN1", "CB1", "PB2", "V", "V", "V", "V", "PN2", "CN1", "FB1", "PB3", "V", "V", "V", "V", "PN3", "FN1", "RB", "PB4", "V", "V", "V", "V", "PN4", "RN", "ROIB", "PB5", "V", "V", "V", "V", "PN5", "ROIN", "FB2", "PB6", "V", "V", "V", "V", "PN6", "FN2", "CB2", "PB7", "V", "V", "V", "V", "PN7", "CN2", "TB2", "PB8", "V", "V", "V", "V", "PN8", "TN2"]
interd_CD = [6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63]
interd_CG = [0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57]
mortn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
NR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nbr_depl = []
coor_case = []
cas_depl = []
mortp = ""
mortf = 0
bloc_bout = 0
debut_P = 0
debut_R = 0
debut_TB1 = 0
debut_TB2 = 0
debut_TN1 = 0
debut_TN2 = 0
PMRB = 0
PMRN = 0
compteur_depl = 0
compteur_case_depl = 0
compteur_tour = 0
position = 64
XM = 0
YM = 0
TZB = 0
TZN = 0
MINB = 0
SB = 0
MSB = 0
MINN = 0
SN = 0
MSN = 0
blocTB = 0
blocTN = 0
blocM = 0


def plateau():
    compteur_pari = 0
    x = 200
    y = 30
    pygame.draw.rect(window, interieur_color, pygame.Rect(195, 25, 890, 890))
    pygame.draw.rect(window, (70, 44, 5), pygame.Rect(195, 25, 890, 890), 9)
    for i in range(0, 64):
        if i % 8 == 0 and i != 0:
            compteur_pari += 1
            x = 200
            y += 110
            coor_case.append(x)
            coor_case.append(y)
            if compteur_pari % 2 == 0:
                if i % 2 == 0:
                    pygame.draw.rect(window, fond_color, pygame.Rect(x, y, 110, 110))
                else:
                    pygame.draw.rect(window, case_B, pygame.Rect(x, y, 110, 110))
            else:
                if i % 2 == 0:
                    pygame.draw.rect(window, case_B, pygame.Rect(x, y, 110, 110))
                else:
                    pygame.draw.rect(window, fond_color, pygame.Rect(x, y, 110, 110))
            x += 110
        else:
            coor_case.append(x)
            coor_case.append(y)
            if compteur_pari % 2 == 0:
                if i % 2 == 0:
                    pygame.draw.rect(window, fond_color, pygame.Rect(x, y, 110, 110))
                else:
                    pygame.draw.rect(window, case_B, pygame.Rect(x, y, 110, 110))
            else:
                if i % 2 == 0:
                    pygame.draw.rect(window, case_B, pygame.Rect(x, y, 110, 110))
                else:
                    pygame.draw.rect(window, fond_color, pygame.Rect(x, y, 110, 110))
            x += 110


image = pygame.image.load("Chess_Icon.png")
pygame.display.set_icon(image)
pygame.display.set_caption("Chess Game by Nico")
window = pygame.display.set_mode((1280, 950))
window.fill(fond_color)
plateau()

for i in range(0, 8):
    image = pygame.image.load("Chess pieces Pion B.png")
    image.convert()
    if i == 0:
        BPB1 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 1:
        BPB2 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 2:
        BPB3 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 3:
        BPB4 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 4:
        BPB5 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 5:
        BPB6 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 6:
        BPB7 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
    if i == 7:
        BPB8 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
for i in range(0, 8):
    image = pygame.image.load("Chess pieces Pion N.png")
    image.convert()
    if i == 0:
        BPN1 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 1:
        BPN2 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 2:
        BPN3 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 3:
        BPN4 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 4:
        BPN5 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 5:
        BPN6 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 6:
        BPN7 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
    if i == 7:
        BPN8 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Tour B.png")
    image.convert()
    if i == 0:
        BTB1 = window.blit(image, [coor_case[112 * i] + 13, coor_case[1 + 112 * i] + 5])
    if i == 1:
        BTB2 = window.blit(image, [coor_case[112 * i] + 13, coor_case[1 + 112 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Tour N.png")
    image.convert()
    if i == 0:
        BTN1 = window.blit(image, [coor_case[14 + 112 * i] + 13, coor_case[15 + 112 * i] + 5])
    if i == 1:
        BTN2 = window.blit(image, [coor_case[14 + 112 * i] + 13, coor_case[15 + 112 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Cheval B.png")
    image.convert()
    if i == 0:
        BCB1 = window.blit(image, [coor_case[16 + 80 * i] + 5, coor_case[17 + 80 * i] + 5])
    if i == 1:
        BCB2 = window.blit(image, [coor_case[16 + 80 * i] + 5, coor_case[17 + 80 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Cheval N.png")
    image.convert()
    if i == 0:
        BCN1 = window.blit(image, [coor_case[30 + 80 * i] + 5, coor_case[31 + 80 * i] + 5])
    if i == 1:
        BCN2 = window.blit(image, [coor_case[30 + 80 * i] + 5, coor_case[31 + 80 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Fou B.png")
    image.convert()
    if i == 0:
        BFB1 = window.blit(image, [coor_case[32 + 48 * i] + 9, coor_case[33 + 48 * i] + 5])
    if i == 1:
        BFB2 = window.blit(image, [coor_case[32 + 48 * i] + 9, coor_case[33 + 48 * i] + 5])
for i in range(0, 2):
    image = pygame.image.load("Chess pieces Fou N.png")
    image.convert()
    if i == 0:
        BFN1 = window.blit(image, [coor_case[46 + 48 * i] + 9, coor_case[47 + 48 * i] + 5])
    if i == 1:
        BFN2 = window.blit(image, [coor_case[46 + 48 * i] + 9, coor_case[47 + 48 * i] + 5])
image = pygame.image.load("Chess pieces Reine B.png")
image.convert()
BRB = window.blit(image, [coor_case[48] + 5, coor_case[49] + 8])
image = pygame.image.load("Chess pieces Reine N.png")
image.convert()
BRN = window.blit(image, [coor_case[62] + 5, coor_case[63] + 8])
image = pygame.image.load("Chess pieces Roi B.png")
image.convert()
BROIB = window.blit(image, [coor_case[64] + 10, coor_case[65] + 5])
image = pygame.image.load("Chess pieces Roi N.png")
image.convert()
BROIN = window.blit(image, [coor_case[78] + 9, coor_case[79] + 5])

plateau()
font = pygame.font.SysFont("cambria", 50)
bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 215, 200, 70), 5)
text = font.render("30 MIN", False, ecrit_color)
window.blit(text, [280, 220])
bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 215, 200, 70), 5)
text = font.render("10 MIN", False, ecrit_color)
window.blit(text, [555, 220])
bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 215, 200, 70), 5)
text = font.render("5 MIN", False, ecrit_color)
window.blit(text, [850, 220])
bouton = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(515, 435, 250, 80), 5)
font = pygame.font.SysFont("cambria", 70)
text = font.render("Jouer", False, ecrit_color)
window.blit(text, [555, 425])
font = pygame.font.SysFont("cambria", 35)
text = font.render("Les Blancs", False, (255, 255, 255))
window.blit(text, [15, 210])
text = font.render("Les Noirs", False, (0, 0, 0))
window.blit(text, [1110, 210])
pygame.display.flip()
running = True


def debut():
    for i in range(0, 8):
        image = pygame.image.load("Chess pieces Pion B.png")
        image.convert()
        window.blit(image, [coor_case[2+16*i]+18, coor_case[3+16*i]+5])
    for i in range(0, 8):
        image = pygame.image.load("Chess pieces Pion N.png")
        image.convert()
        window.blit(image, [coor_case[12+16*i]+18, coor_case[13+16*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Tour B.png")
        image.convert()
        window.blit(image, [coor_case[112*i]+13, coor_case[1+112*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Tour N.png")
        image.convert()
        window.blit(image, [coor_case[14+112*i]+13, coor_case[15+112*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Cheval B.png")
        image.convert()
        window.blit(image, [coor_case[16+80*i]+5, coor_case[17+80*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Cheval N.png")
        image.convert()
        window.blit(image, [coor_case[30+80*i]+5, coor_case[31+80*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Fou B.png")
        image.convert()
        window.blit(image, [coor_case[32+48*i]+9, coor_case[33+48*i]+5])
    for i in range(0, 2):
        image = pygame.image.load("Chess pieces Fou N.png")
        image.convert()
        window.blit(image, [coor_case[46+48*i]+9, coor_case[47+48*i]+5])
    image = pygame.image.load("Chess pieces Reine B.png")
    image.convert()
    window.blit(image, [coor_case[48]+5, coor_case[49]+8])
    image = pygame.image.load("Chess pieces Reine N.png")
    image.convert()
    window.blit(image, [coor_case[62]+5, coor_case[63]+8])
    image = pygame.image.load("Chess pieces Roi B.png")
    image.convert()
    window.blit(image, [coor_case[64]+10, coor_case[65]+5])
    image = pygame.image.load("Chess pieces Roi N.png")
    image.convert()
    window.blit(image, [coor_case[78]+9, coor_case[79]+5])


def poss_depl_PB():
    if position != 7 and position != 15 and position != 23 and position != 31 and position != 39 and position != 47 and position != 55 and position != 63:
        if place_case[position+1] == "V":
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+1)*2]+54, coor_case[(position+1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position+1)*2])
            nbr_depl.append(coor_case[(position+1)*2+1])
            cas_depl.append(position+1)
            if debut_P == 1 and place_case[position+2] == "V":
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+2)*2]+54, coor_case[(position+2)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position+2)*2])
                nbr_depl.append(coor_case[(position+2)*2+1])
                cas_depl.append(position+2)
        if position > 7:
            verif_c = "B" in place_case[position-7]
            if place_case[position-7] != "V" and verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-7)*2]+54, coor_case[(position-7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position-7)*2])
                nbr_depl.append(coor_case[(position-7)*2+1])
                cas_depl.append(position-7)
        if position < 56:
            verif_c = "B" in place_case[position+9]
            if place_case[position+9] != "V" and verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+9)*2]+54, coor_case[(position+9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position+9)*2])
                nbr_depl.append(coor_case[(position+9)*2+1])
                cas_depl.append(position+9)


def poss_depl_PN():
    if position != 0 and position != 8 and position != 16 and position != 24 and position != 32 and position != 40 and position != 48 and position != 56:
        if place_case[position-1] == "V":
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-1)*2]+54, coor_case[(position-1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position-1)*2])
            nbr_depl.append(coor_case[(position-1)*2+1])
            cas_depl.append(position-1)
            if debut_P == 1 and place_case[position-2] == "V":
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-2)*2]+54, coor_case[(position-2)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position-2)*2])
                nbr_depl.append(coor_case[(position-2)*2+1])
                cas_depl.append(position-2)
        if position > 7:
            verif_c = "N" in place_case[position-9]
            if place_case[position-9] != "V" and verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-9)*2]+54, coor_case[(position-9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position-9)*2])
                nbr_depl.append(coor_case[(position-9)*2+1])
                cas_depl.append(position-9)
        if position < 56:
            verif_c = "N" in place_case[position+7]
            if place_case[position+7] != "V" and verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+7)*2]+54, coor_case[(position+7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position+7)*2])
                nbr_depl.append(coor_case[(position+7)*2+1])
                cas_depl.append(position+7)


def poss_depl_T():
    compteur_pos = position
    while compteur_pos != 7 and compteur_pos != 15 and compteur_pos != 23 and compteur_pos != 31 and compteur_pos != 39 and compteur_pos != 47 and compteur_pos != 55 and compteur_pos != 63:
        if place_case[compteur_pos + 1] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos+1]
            else:
                verif_c = "N" in place_case[compteur_pos + 1]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+1)*2]+54, coor_case[(compteur_pos+1)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+1)*2])
                nbr_depl.append(coor_case[(compteur_pos+1)*2+1])
                cas_depl.append(compteur_pos+1)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+1)*2]+54, coor_case[(compteur_pos+1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos+1)*2])
            nbr_depl.append(coor_case[(compteur_pos+1)*2+1])
            cas_depl.append(compteur_pos+1)
        compteur_pos += 1
    compteur_pos = position
    while compteur_pos != 0 and compteur_pos != 8 and compteur_pos != 16 and compteur_pos != 24 and compteur_pos != 32 and compteur_pos != 40 and compteur_pos != 48 and compteur_pos != 56:
        if place_case[compteur_pos - 1] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos-1]
            else:
                verif_c = "N" in place_case[compteur_pos - 1]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos - 1) * 2] + 54, coor_case[(compteur_pos - 1) * 2 + 1] + 54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-1)*2])
                nbr_depl.append(coor_case[(compteur_pos-1)*2+1])
                cas_depl.append(compteur_pos-1)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-1)*2]+54, coor_case[(compteur_pos-1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos-1)*2])
            nbr_depl.append(coor_case[(compteur_pos-1)*2+1])
            cas_depl.append(compteur_pos-1)
        compteur_pos -= 1
    compteur_pos = position
    while compteur_pos > 7:
        if place_case[compteur_pos - 8] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos-8]
            else:
                verif_c = "N" in place_case[compteur_pos - 8]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos - 8) * 2] + 54, coor_case[(compteur_pos - 8) * 2 + 1] + 54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-8)*2])
                nbr_depl.append(coor_case[(compteur_pos-8)*2+1])
                cas_depl.append(compteur_pos-8)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-8)*2]+54, coor_case[(compteur_pos-8)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos-8)*2])
            nbr_depl.append(coor_case[(compteur_pos-8)*2+1])
            cas_depl.append(compteur_pos-8)
        compteur_pos -= 8
    compteur_pos = position
    while compteur_pos < 56:
        if place_case[compteur_pos + 8] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos+8]
            else:
                verif_c = "N" in place_case[compteur_pos + 8]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+8)*2]+54, coor_case[(compteur_pos+8)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+8)*2])
                nbr_depl.append(coor_case[(compteur_pos+8)*2+1])
                cas_depl.append(compteur_pos+8)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+8)*2]+54, coor_case[(compteur_pos+8)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos+8)*2])
            nbr_depl.append(coor_case[(compteur_pos+8)*2+1])
            cas_depl.append(compteur_pos+8)
        compteur_pos += 8


def poss_depl_C():
    compteur_pos = position
    possible = compteur_pos in interd_CD
    if possible == False:
        if compteur_pos > 7:
            if place_case[compteur_pos - 6] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos-6]
                else:
                    verif_c = "N" in place_case[compteur_pos-6]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-6)*2]+54, coor_case[(compteur_pos-6)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos-6)*2])
                    nbr_depl.append(coor_case[(compteur_pos-6)*2+1])
                    cas_depl.append(compteur_pos-6)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-6)*2]+54, coor_case[(compteur_pos-6)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-6)*2])
                nbr_depl.append(coor_case[(compteur_pos-6)*2+1])
                cas_depl.append(compteur_pos-6)
        if compteur_pos < 56:
            if place_case[compteur_pos + 10] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos+10]
                else:
                    verif_c = "N" in place_case[compteur_pos+10]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+10)*2]+54, coor_case[(compteur_pos+10)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos+10)*2])
                    nbr_depl.append(coor_case[(compteur_pos+10)*2+1])
                    cas_depl.append(compteur_pos+10)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+10)*2]+54, coor_case[(compteur_pos+10)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+10)*2])
                nbr_depl.append(coor_case[(compteur_pos+10)*2+1])
                cas_depl.append(compteur_pos+10)
    possible = compteur_pos in interd_CG
    if possible == False:
        if compteur_pos > 7:
            if place_case[compteur_pos - 10] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos-10]
                else:
                    verif_c = "N" in place_case[compteur_pos-10]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-10)*2]+54, coor_case[(compteur_pos-10)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos-10)*2])
                    nbr_depl.append(coor_case[(compteur_pos-10)*2+1])
                    cas_depl.append(compteur_pos-10)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-10)*2]+54, coor_case[(compteur_pos-10)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-10)*2])
                nbr_depl.append(coor_case[(compteur_pos-10)*2+1])
                cas_depl.append(compteur_pos-10)
        if compteur_pos < 56:
            if place_case[compteur_pos + 6] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos+6]
                else:
                    verif_c = "N" in place_case[compteur_pos+6]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+6)*2]+54, coor_case[(compteur_pos+6)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos+6)*2])
                    nbr_depl.append(coor_case[(compteur_pos+6)*2+1])
                    cas_depl.append(compteur_pos+6)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+6)*2]+54, coor_case[(compteur_pos+6)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+6)*2])
                nbr_depl.append(coor_case[(compteur_pos+6)*2+1])
                cas_depl.append(compteur_pos+6)
    if compteur_pos > 15:
        if compteur_pos != 23 and compteur_pos != 31 and compteur_pos != 39 and compteur_pos != 47 and compteur_pos != 55 and compteur_pos != 63:
            if place_case[compteur_pos - 15] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos-15]
                else:
                    verif_c = "N" in place_case[compteur_pos-15]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-15)*2]+54, coor_case[(compteur_pos-15)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos-15)*2])
                    nbr_depl.append(coor_case[(compteur_pos-15)*2+1])
                    cas_depl.append(compteur_pos-15)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-15)*2]+54, coor_case[(compteur_pos-15)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-15)*2])
                nbr_depl.append(coor_case[(compteur_pos-15)*2+1])
                cas_depl.append(compteur_pos-15)
        if compteur_pos != 16 and compteur_pos != 24 and compteur_pos != 32 and compteur_pos != 40 and compteur_pos != 48 and compteur_pos != 56:
            if place_case[compteur_pos - 17] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos-17]
                else:
                    verif_c = "N" in place_case[compteur_pos-17]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-17)*2]+54, coor_case[(compteur_pos-17)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos-17)*2])
                    nbr_depl.append(coor_case[(compteur_pos-17)*2+1])
                    cas_depl.append(compteur_pos-17)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-17)*2]+54, coor_case[(compteur_pos-17)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-17)*2])
                nbr_depl.append(coor_case[(compteur_pos-17)*2+1])
                cas_depl.append(compteur_pos-17)
    if compteur_pos < 48:
        if compteur_pos != 23 and compteur_pos != 31 and compteur_pos != 39 and compteur_pos != 47 and compteur_pos != 7 and compteur_pos != 15:
            if place_case[compteur_pos + 17] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos+17]
                else:
                    verif_c = "N" in place_case[compteur_pos+17]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+17)*2]+54, coor_case[(compteur_pos+17)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos+17)*2])
                    nbr_depl.append(coor_case[(compteur_pos+17)*2+1])
                    cas_depl.append(compteur_pos+17)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+17)*2]+54, coor_case[(compteur_pos+17)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+17)*2])
                nbr_depl.append(coor_case[(compteur_pos+17)*2+1])
                cas_depl.append(compteur_pos+17)
        if compteur_pos != 16 and compteur_pos != 24 and compteur_pos != 32 and compteur_pos != 40 and compteur_pos != 0 and compteur_pos != 8:
            if place_case[compteur_pos + 15] != "V":
                verif_cp = "B" in place_case[position]
                if verif_cp == True:
                    verif_c = "B" in place_case[compteur_pos+15]
                else:
                    verif_c = "N" in place_case[compteur_pos+15]
                if verif_c == False:
                    pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+15)*2]+54, coor_case[(compteur_pos+15)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(compteur_pos+15)*2])
                    nbr_depl.append(coor_case[(compteur_pos+15)*2+1])
                    cas_depl.append(compteur_pos+15)
            else:
                pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+15)*2]+54, coor_case[(compteur_pos+15)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+15)*2])
                nbr_depl.append(coor_case[(compteur_pos+15)*2+1])
                cas_depl.append(compteur_pos+15)


def poss_depl_F():
    compteur_pos = position
    while compteur_pos > 7 and compteur_pos != 15 and compteur_pos != 23 and compteur_pos != 31 and compteur_pos != 39 and compteur_pos != 47 and compteur_pos != 55 and compteur_pos != 63:
        if place_case[compteur_pos-7] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos-7]
            else:
                verif_c = "N" in place_case[compteur_pos-7]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-7)*2]+54, coor_case[(compteur_pos-7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-7)*2])
                nbr_depl.append(coor_case[(compteur_pos-7)*2+1])
                cas_depl.append(compteur_pos-7)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-7)*2]+54, coor_case[(compteur_pos-7)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos-7)*2])
            nbr_depl.append(coor_case[(compteur_pos-7)*2+1])
            cas_depl.append(compteur_pos-7)
        compteur_pos -= 7
    compteur_pos = position
    while compteur_pos > 7 and compteur_pos != 8 and compteur_pos != 16 and compteur_pos != 24 and compteur_pos != 32 and compteur_pos != 40 and compteur_pos != 48 and compteur_pos != 56:
        if place_case[compteur_pos-9] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos-9]
            else:
                verif_c = "N" in place_case[compteur_pos-9]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos-9)*2]+54, coor_case[(compteur_pos-9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos-9)*2])
                nbr_depl.append(coor_case[(compteur_pos-9)*2+1])
                cas_depl.append(compteur_pos-9)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos-9)*2]+54, coor_case[(compteur_pos-9)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos-9)*2])
            nbr_depl.append(coor_case[(compteur_pos-9)*2+1])
            cas_depl.append(compteur_pos-9)
        compteur_pos -= 9
    compteur_pos = position
    while compteur_pos < 56 and compteur_pos != 15 and compteur_pos != 23 and compteur_pos != 31 and compteur_pos != 39 and compteur_pos != 47 and compteur_pos != 55 and compteur_pos != 7:
        if place_case[compteur_pos+9] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos+9]
            else:
                verif_c = "N" in place_case[compteur_pos+9]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+9)*2]+54, coor_case[(compteur_pos+9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+9)*2])
                nbr_depl.append(coor_case[(compteur_pos+9)*2+1])
                cas_depl.append(compteur_pos+9)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+9)*2]+54, coor_case[(compteur_pos+9)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos+9)*2])
            nbr_depl.append(coor_case[(compteur_pos+9)*2+1])
            cas_depl.append(compteur_pos+9)
        compteur_pos += 9
    compteur_pos = position
    while compteur_pos < 56 and compteur_pos != 8 and compteur_pos != 16 and compteur_pos != 24 and compteur_pos != 32 and compteur_pos != 40 and compteur_pos != 48 and compteur_pos != 0:
        if place_case[compteur_pos+7] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[compteur_pos+7]
            else:
                verif_c = "N" in place_case[compteur_pos+7]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(compteur_pos+7)*2]+54, coor_case[(compteur_pos+7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(compteur_pos+7)*2])
                nbr_depl.append(coor_case[(compteur_pos+7)*2+1])
                cas_depl.append(compteur_pos+7)
            break
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(compteur_pos+7)*2]+54, coor_case[(compteur_pos+7)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(compteur_pos+7)*2])
            nbr_depl.append(coor_case[(compteur_pos+7)*2+1])
            cas_depl.append(compteur_pos+7)
        compteur_pos += 7


def poss_depl_R():
    if position != 15 and position != 23 and position != 31 and position != 39 and position != 47 and position != 55 and position != 7 and position != 63:
        if place_case[position + 1] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position + 1]
            else:
                verif_c = "N" in place_case[position + 1]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+1)*2]+54, coor_case[(position+1)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position + 1) * 2])
                nbr_depl.append(coor_case[(position + 1) * 2 + 1])
                cas_depl.append(position + 1)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+1)*2]+54, coor_case[(position+1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position+1)*2])
            nbr_depl.append(coor_case[(position+1)*2+1])
            cas_depl.append(position+1)
    if position != 8 and position != 16 and position != 24 and position != 32 and position != 40 and position != 48 and position != 0 and position != 56:
        if place_case[position - 1] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position - 1]
            else:
                verif_c = "N" in place_case[position - 1]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-1)*2]+54, coor_case[(position-1)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position - 1) * 2])
                nbr_depl.append(coor_case[(position - 1) * 2 + 1])
                cas_depl.append(position - 1)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-1)*2]+54, coor_case[(position-1)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position-1)*2])
            nbr_depl.append(coor_case[(position-1)*2+1])
            cas_depl.append(position-1)
    if position > 7:
        if place_case[position - 8] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position - 8]
            else:
                verif_c = "N" in place_case[position - 8]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-8)*2]+54, coor_case[(position-8)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position - 8) * 2])
                nbr_depl.append(coor_case[(position - 8) * 2 + 1])
                cas_depl.append(position - 8)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-8)*2]+54, coor_case[(position-8)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position-8)*2])
            nbr_depl.append(coor_case[(position-8)*2+1])
            cas_depl.append(position-8)
            if debut_R == 1 and place_case[position - 16] == "V" and place_case[position - 24] == "V":
                if place_case[position] == "ROIB" and debut_TB1 == 0:
                    pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-16)*2]+54, coor_case[(position-16)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(position-16)*2])
                    nbr_depl.append(coor_case[(position-16)*2+1])
                    cas_depl.append(position-16)
                if place_case[position] == "ROIN" and debut_TN1 == 0:
                    pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-16)*2]+54, coor_case[(position-16)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(position-16)*2])
                    nbr_depl.append(coor_case[(position-16)*2+1])
                    cas_depl.append(position-16)

    if position < 56:
        if place_case[position + 8] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position + 8]
            else:
                verif_c = "N" in place_case[position + 8]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+8)*2]+54, coor_case[(position+8)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position + 8) * 2])
                nbr_depl.append(coor_case[(position + 8) * 2 + 1])
                cas_depl.append(position + 8)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+8)*2]+54, coor_case[(position+8)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position+8)*2])
            nbr_depl.append(coor_case[(position+8)*2+1])
            cas_depl.append(position+8)
            if debut_R == 1 and place_case[position + 16] == "V":
                if place_case[position] == "ROIB" and debut_TB2 == 0:
                    pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+16)*2]+54, coor_case[(position+16)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(position+16)*2])
                    nbr_depl.append(coor_case[(position+16)*2+1])
                    cas_depl.append(position+16)
                if place_case[position] == "ROIN" and debut_TN2 == 0:
                    pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+16)*2]+54, coor_case[(position+16)*2+1]+54], 20, 5)
                    nbr_depl.append(coor_case[(position+16)*2])
                    nbr_depl.append(coor_case[(position+16)*2+1])
                    cas_depl.append(position+16)
    if position > 7 and position != 15 and position != 23 and position != 31 and position != 39 and position != 47 and position != 55 and position != 63:
        if place_case[position - 7] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position - 7]
            else:
                verif_c = "N" in place_case[position - 7]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-7)*2]+54, coor_case[(position-7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position - 7) * 2])
                nbr_depl.append(coor_case[(position - 7) * 2 + 1])
                cas_depl.append(position - 7)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-7)*2]+54, coor_case[(position-7)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position-7)*2])
            nbr_depl.append(coor_case[(position-7)*2+1])
            cas_depl.append(position-7)
    if position < 56 and position != 15 and position != 23 and position != 31 and position != 39 and position != 47 and position != 55 and position != 7:
        if place_case[position + 9] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position + 9]
            else:
                verif_c = "N" in place_case[position + 9]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+9)*2]+54, coor_case[(position+9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position + 9) * 2])
                nbr_depl.append(coor_case[(position + 9) * 2 + 1])
                cas_depl.append(position + 9)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+9)*2]+54, coor_case[(position+9)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position+9)*2])
            nbr_depl.append(coor_case[(position+9)*2+1])
            cas_depl.append(position+9)
    if position < 56 and position != 8 and position != 16 and position != 24 and position != 32 and position != 40 and position != 48 and position != 0:
        if place_case[position + 7] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position + 7]
            else:
                verif_c = "N" in place_case[position + 7]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position+7)*2]+54, coor_case[(position+7)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position + 7) * 2])
                nbr_depl.append(coor_case[(position + 7) * 2 + 1])
                cas_depl.append(position + 7)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position+7)*2]+54, coor_case[(position+7)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position+7)*2])
            nbr_depl.append(coor_case[(position+7)*2+1])
            cas_depl.append(position+7)
    if position > 7 and position != 8 and position != 16 and position != 24 and position != 32 and position != 40 and position != 48 and position != 56:
        if place_case[position - 9] != "V":
            verif_cp = "B" in place_case[position]
            if verif_cp == True:
                verif_c = "B" in place_case[position - 9]
            else:
                verif_c = "N" in place_case[position - 9]
            if verif_c == False:
                pygame.draw.circle(window, (255, 0, 0), [coor_case[(position-9)*2]+54, coor_case[(position-9)*2+1]+54], 20, 5)
                nbr_depl.append(coor_case[(position-9)*2])
                nbr_depl.append(coor_case[(position-9)*2+1])
                cas_depl.append(position-9)
        else:
            pygame.draw.circle(window, (121, 212, 12), [coor_case[(position-9)*2]+54, coor_case[(position-9)*2+1]+54], 20, 5)
            nbr_depl.append(coor_case[(position-9)*2])
            nbr_depl.append(coor_case[(position-9)*2+1])
            cas_depl.append(position-9)


def supp_pos():
    compteur_supp_depl = 0
    compteur_supp_depl_2 = 0

    def supp_pion():
        dedant_n = place_case[cas_depl[compteur_supp_depl_2]]
        dedant = "PB" in place_case[cas_depl[compteur_supp_depl_2]]
        if dedant == True:
            if dedant_n == "PB1" and NR[0] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB2" and NR[1] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB3" and NR[2] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB4" and NR[3] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB5" and NR[4] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB6" and NR[5] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB7" and NR[6] == 1:
                dedant_n = "RB"
            elif dedant_n == "PB8" and NR[7] == 1:
                dedant_n = "RB"
            else:
                image = pygame.image.load("Chess pieces Pion B.png")
                image.convert()
                window.blit(image, [nbr_depl[compteur_supp_depl] + 18, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "PN" in place_case[cas_depl[compteur_supp_depl_2]]
        if dedant == True:
            if dedant_n == "PN1" and NR[8] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN2" and NR[9] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN3" and NR[10] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN4" and NR[11] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN5" and NR[12] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN6" and NR[13] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN7" and NR[14] == 1:
                dedant_n = "RN"
            elif dedant_n == "PN8" and NR[15] == 1:
                dedant_n = "RN"
            else:
                image = pygame.image.load("Chess pieces Pion N.png")
                image.convert()
                window.blit(image, [nbr_depl[compteur_supp_depl] + 18, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "TB" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Tour B.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 13, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "TN" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Tour N.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 13, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "CB" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Cheval B.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 5, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "CN" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Cheval N.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 5, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "FB" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Fou B.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 9, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "FN" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Fou N.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 9, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "RB" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Reine B.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 5, nbr_depl[compteur_supp_depl+1] + 8])
        dedant = "RN" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Reine N.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 5, nbr_depl[compteur_supp_depl+1] + 8])
        dedant = "ROIB" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Roi B.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 10, nbr_depl[compteur_supp_depl+1] + 5])
        dedant = "ROIN" in dedant_n
        if dedant == True:
            image = pygame.image.load("Chess pieces Roi N.png")
            image.convert()
            window.blit(image, [nbr_depl[compteur_supp_depl] + 9, nbr_depl[compteur_supp_depl+1] + 5])

    while len(nbr_depl) > compteur_supp_depl:
        compteur_pari = 0
        for i in range(0, 64):
            if i % 8 == 0 and i != 0:
                compteur_pari += 1
                if i == cas_depl[compteur_supp_depl_2]:
                    if compteur_pari % 2 == 0:
                        if cas_depl[compteur_supp_depl_2] % 2 == 0:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, fond_color, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, fond_color, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                        else:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, case_B, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, case_B, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                    else:
                        if cas_depl[compteur_supp_depl_2] % 2 == 0:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, case_B, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, case_B, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                        else:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, fond_color, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, fond_color, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
            else:
                if i == cas_depl[compteur_supp_depl_2]:
                    if compteur_pari % 2 == 0:
                        if cas_depl[compteur_supp_depl_2] % 2 == 0:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, fond_color, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, fond_color, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                        else:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, case_B, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, case_B, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                    else:
                        if cas_depl[compteur_supp_depl_2] % 2 == 0:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, case_B, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, case_B, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
                        else:
                            if place_case[cas_depl[compteur_supp_depl_2]] != "V":
                                pygame.draw.rect(window, fond_color, pygame.Rect(nbr_depl[compteur_supp_depl], nbr_depl[compteur_supp_depl+1], 110, 110))
                                if XM != nbr_depl[compteur_supp_depl] or YM != nbr_depl[compteur_supp_depl+1]:
                                    supp_pion()
                            else:
                                pygame.draw.circle(window, fond_color, [nbr_depl[compteur_supp_depl] + 54, nbr_depl[compteur_supp_depl+1] + 54], 20, 5)
        compteur_supp_depl += 2
        compteur_supp_depl_2 += 1


def depl():
    compteur_pari = 0
    for i in range(0, 64):
        if i % 8 == 0 and i != 0:
            compteur_pari += 1
            if i == position:
                if compteur_pari % 2 == 0:
                    if position % 2 == 0:
                        pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                    else:
                        pygame.draw.rect(window, case_B, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                else:
                    if position % 2 == 0:
                        pygame.draw.rect(window, case_B, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                    else:
                        pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
        else:
            if i == position:
                if compteur_pari % 2 == 0:
                    if position % 2 == 0:
                        pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                    else:
                        pygame.draw.rect(window, case_B, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                else:
                    if position % 2 == 0:
                        pygame.draw.rect(window, case_B, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))
                    else:
                        pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[position*2], coor_case[position*2+1], 110, 110))


def mort():
    global mortp
    font = pygame.font.SysFont("cambria", 40)
    mortd = "PB" in mortp
    if mortd == True:
        if mortp == "PB1" and NR[0] == 1:
            mortp = "RB"
        elif mortp == "PB2" and NR[1] == 1:
            mortp = "RB"
        elif mortp == "PB3" and NR[2] == 1:
            mortp = "RB"
        elif mortp == "PB4" and NR[3] == 1:
            mortp = "RB"
        elif mortp == "PB5" and NR[4] == 1:
            mortp = "RB"
        elif mortp == "PB6" and NR[5] == 1:
            mortp = "RB"
        elif mortp == "PB7" and NR[6] == 1:
            mortp = "RB"
        elif mortp == "PB8" and NR[7] == 1:
            mortp = "RB"
        else:
            mortn[0] += 1
            image = pygame.image.load("Chess pieces Pion BP.png")
            image.convert()
            window.blit(image, [1119, 280])
            pygame.draw.rect(window, fond_color, pygame.Rect(1180, 280, 50, 50))
            text = font.render("X " + str(mortn[0]), False, (0, 0, 0))
            window.blit(text, [1170, 280])
    mortd = "PN" in mortp
    if mortd == True:
        if mortp == "PN1" and NR[8] == 1:
            mortp = "RN"
        elif mortp == "PN2" and NR[9] == 1:
            mortp = "RN"
        elif mortp == "PN3" and NR[10] == 1:
            mortp = "RN"
        elif mortp == "PN4" and NR[11] == 1:
            mortp = "RN"
        elif mortp == "PN5" and NR[12] == 1:
            mortp = "RN"
        elif mortp == "PN6" and NR[13] == 1:
            mortp = "RN"
        elif mortp == "PN7" and NR[14] == 1:
            mortp = "RN"
        elif mortp == "PN8" and NR[15] == 1:
            mortp = "RN"
        else:
            mortn[1] += 1
            image = pygame.image.load("Chess pieces Pion NP.png")
            image.convert()
            window.blit(image, [129, 280])
            pygame.draw.rect(window, fond_color, pygame.Rect(55, 280, 50, 50))
            text = font.render(str(mortn[1]) + " X", False, (255, 255, 255))
            window.blit(text, [55, 280])
    mortd = "CB" in mortp
    if mortd == True:
        mortn[2] += 1
        image = pygame.image.load("Chess pieces Cheval BP.png")
        image.convert()
        window.blit(image, [1112, 390])
        pygame.draw.rect(window, fond_color, pygame.Rect(1180, 390, 50, 50))
        text = font.render("X " + str(mortn[2]), False, (0, 0, 0))
        window.blit(text, [1170, 390])
    mortd = "CN" in mortp
    if mortd == True:
        mortn[3] += 1
        image = pygame.image.load("Chess pieces Cheval NP.png")
        image.convert()
        window.blit(image, [122, 390])
        pygame.draw.rect(window, fond_color, pygame.Rect(55, 390, 50, 50))
        text = font.render(str(mortn[3]) + " X", False, (255, 255, 255))
        window.blit(text, [55, 390])
    mortd = "FB" in mortp
    if mortd == True:
        mortn[4] += 1
        image = pygame.image.load("Chess pieces Fou BP.png")
        image.convert()
        window.blit(image, [1114, 500])
        pygame.draw.rect(window, fond_color, pygame.Rect(1180, 500, 50, 50))
        text = font.render("X " + str(mortn[4]), False, (0, 0, 0))
        window.blit(text, [1170, 500])
    mortd = "FN" in mortp
    if mortd == True:
        mortn[5] += 1
        image = pygame.image.load("Chess pieces Fou NP.png")
        image.convert()
        window.blit(image, [124, 500])
        pygame.draw.rect(window, fond_color, pygame.Rect(55, 500, 50, 50))
        text = font.render(str(mortn[5]) + " X", False, (255, 255, 255))
        window.blit(text, [55, 500])
    mortd = "TB" in mortp
    if mortd == True:
        mortn[6] += 1
        image = pygame.image.load("Chess pieces Tour BP.png")
        image.convert()
        window.blit(image, [1116, 610])
        pygame.draw.rect(window, fond_color, pygame.Rect(1180, 610, 50, 50))
        text = font.render("X " + str(mortn[6]), False, (0, 0, 0))
        window.blit(text, [1170, 610])
    mortd = "TN" in mortp
    if mortd == True:
        mortn[7] += 1
        image = pygame.image.load("Chess pieces Tour NP.png")
        image.convert()
        window.blit(image, [126, 610])
        pygame.draw.rect(window, fond_color, pygame.Rect(55, 610, 50, 50))
        text = font.render(str(mortn[7]) + " X", False, (255, 255, 255))
        window.blit(text, [55, 610])
    mortd = "RB" in mortp
    if mortd == True:
        mortn[8] += 1
        image = pygame.image.load("Chess pieces Reine BP.png")
        image.convert()
        window.blit(image, [1112, 720])
        pygame.draw.rect(window, fond_color, pygame.Rect(1180, 720, 50, 50))
        text = font.render("X " + str(mortn[8]), False, (0, 0, 0))
        window.blit(text, [1170, 720])
    mortd = "RN" in mortp
    if mortd == True:
        mortn[9] += 1
        image = pygame.image.load("Chess pieces Reine NP.png")
        image.convert()
        window.blit(image, [122, 720])
        pygame.draw.rect(window, fond_color, pygame.Rect(55, 720, 50, 50))
        text = font.render(str(mortn[9]) + " X", False, (255, 255, 255))
        window.blit(text, [55, 720])


while running:
    mouse_xy = pygame.mouse.get_pos()
    clic_5 = bouton5M.collidepoint(mouse_xy)
    clic_10 = bouton10M.collidepoint(mouse_xy)
    clic_30 = bouton30M.collidepoint(mouse_xy)
    clic_f = bouton.collidepoint(mouse_xy)
    clic_PB1 = BPB1.collidepoint(mouse_xy)
    clic_PB2 = BPB2.collidepoint(mouse_xy)
    clic_PB3 = BPB3.collidepoint(mouse_xy)
    clic_PB4 = BPB4.collidepoint(mouse_xy)
    clic_PB5 = BPB5.collidepoint(mouse_xy)
    clic_PB6 = BPB6.collidepoint(mouse_xy)
    clic_PB7 = BPB7.collidepoint(mouse_xy)
    clic_PB8 = BPB8.collidepoint(mouse_xy)
    clic_PN1 = BPN1.collidepoint(mouse_xy)
    clic_PN2 = BPN2.collidepoint(mouse_xy)
    clic_PN3 = BPN3.collidepoint(mouse_xy)
    clic_PN4 = BPN4.collidepoint(mouse_xy)
    clic_PN5 = BPN5.collidepoint(mouse_xy)
    clic_PN6 = BPN6.collidepoint(mouse_xy)
    clic_PN7 = BPN7.collidepoint(mouse_xy)
    clic_PN8 = BPN8.collidepoint(mouse_xy)
    clic_TB1 = BTB1.collidepoint(mouse_xy)
    clic_TB2 = BTB2.collidepoint(mouse_xy)
    clic_TN1 = BTN1.collidepoint(mouse_xy)
    clic_TN2 = BTN2.collidepoint(mouse_xy)
    clic_CB1 = BCB1.collidepoint(mouse_xy)
    clic_CB2 = BCB2.collidepoint(mouse_xy)
    clic_CN1 = BCN1.collidepoint(mouse_xy)
    clic_CN2 = BCN2.collidepoint(mouse_xy)
    clic_FB1 = BFB1.collidepoint(mouse_xy)
    clic_FB2 = BFB2.collidepoint(mouse_xy)
    clic_FN1 = BFN1.collidepoint(mouse_xy)
    clic_FN2 = BFN2.collidepoint(mouse_xy)
    clic_RB = BRB.collidepoint(mouse_xy)
    clic_RN = BRN.collidepoint(mouse_xy)
    clic_ROIB = BROIB.collidepoint(mouse_xy)
    clic_ROIN = BROIN.collidepoint(mouse_xy)
    for event in pygame.event.get():
        if len(nbr_depl) > 0:
            compteur_depl = 0
            compteur_case_depl = 0
            while compteur_depl < len(nbr_depl):
                s = pygame.Surface((110, 110))
                s.set_alpha(0)
                s.fill((255, 255, 255))
                bouton_depl = window.blit(s, (nbr_depl[compteur_depl], nbr_depl[compteur_depl+1]))
                clic_depl = bouton_depl.collidepoint(mouse_xy)
                if event.type == pygame.MOUSEBUTTONDOWN and clic_depl and bloc_bout == 1:
                    XM = nbr_depl[compteur_depl]
                    YM = nbr_depl[compteur_depl + 1]
                    supp_pos()
                    depl()
                    XM = 0
                    YM = 0
                    if place_case[position] == "PB1":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[0] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB1 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[0] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB1 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB1"
                    if place_case[position] == "PB2":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[1] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB2 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[1] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB2 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB2"
                    if place_case[position] == "PB3":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[2] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB3 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[2] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB3 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB3"
                    if place_case[position] == "PB4":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[3] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB4 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[3] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB4 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB4"
                    if place_case[position] == "PB5":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[4] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB5 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[4] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB5 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB5"
                    if place_case[position] == "PB6":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[5] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB6 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[5] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB6 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB6"
                    if place_case[position] == "PB7":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[6] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB7 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[6] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB7 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB7"
                    if place_case[position] == "PB8":
                        if position+1 == 7 or position+1 == 15 or position+1 == 23 or position+1 == 31 or position+1 == 39 or position+1 == 47 or position+1 == 55 or position+1 == 63 or NR[7] == 1:
                            image = pygame.image.load("Chess pieces Reine B.png")
                            image.convert()
                            BPB8 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[7] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion B.png")
                            image.convert()
                            BPB8 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PB8"
                    if place_case[position] == "PN1":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[8] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN1 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[8] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN1 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN1"
                    if place_case[position] == "PN2":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[9] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN2 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[9] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN2 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN2"
                    if place_case[position] == "PN3":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[10] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN3 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[10] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN3 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN3"
                    if place_case[position] == "PN4":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[11] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN4 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[11] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN4 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN4"
                    if place_case[position] == "PN5":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[12] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN5 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[12] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN5 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN5"
                    if place_case[position] == "PN6":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[13] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN6 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[13] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN6 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN6"
                    if place_case[position] == "PN7":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[14] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN7 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[14] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN7 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN7"
                    if place_case[position] == "PN8":
                        if position-1 == 0 or position-1 == 8 or position-1 == 16 or position-1 == 24 or position+1 == 32 or position-1 == 40 or position-1 == 48 or position-1 == 56 or NR[15] == 1:
                            image = pygame.image.load("Chess pieces Reine N.png")
                            image.convert()
                            BPN8 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                            NR[15] = 1
                        else:
                            image = pygame.image.load("Chess pieces Pion N.png")
                            image.convert()
                            BPN8 = window.blit(image, [nbr_depl[compteur_depl] + 18, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "PN8"
                    if place_case[position] == "TB1":
                        debut_TB1 = 1
                        image = pygame.image.load("Chess pieces Tour B.png")
                        image.convert()
                        BTB1 = window.blit(image, [nbr_depl[compteur_depl] + 13, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "TB1"
                    if place_case[position] == "TB2":
                        debut_TB2 = 1
                        image = pygame.image.load("Chess pieces Tour B.png")
                        image.convert()
                        BTB2 = window.blit(image, [nbr_depl[compteur_depl] + 13, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "TB2"
                    if place_case[position] == "TN1":
                        debut_TN1 = 1
                        image = pygame.image.load("Chess pieces Tour N.png")
                        image.convert()
                        BTN1 = window.blit(image, [nbr_depl[compteur_depl] + 13, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "TN1"
                    if place_case[position] == "TN2":
                        debut_TN2 = 1
                        image = pygame.image.load("Chess pieces Tour N.png")
                        image.convert()
                        BTN2 = window.blit(image, [nbr_depl[compteur_depl] + 13, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "TN2"
                    if place_case[position] == "CB1":
                        image = pygame.image.load("Chess pieces Cheval B.png")
                        image.convert()
                        BCB1 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "CB1"
                    if place_case[position] == "CB2":
                        image = pygame.image.load("Chess pieces Cheval B.png")
                        image.convert()
                        BCB2 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "CB2"
                    if place_case[position] == "CN1":
                        image = pygame.image.load("Chess pieces Cheval N.png")
                        image.convert()
                        BCN1 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "CN1"
                    if place_case[position] == "CN2":
                        image = pygame.image.load("Chess pieces Cheval N.png")
                        image.convert()
                        BCN2 = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "CN2"
                    if place_case[position] == "FB1":
                        image = pygame.image.load("Chess pieces Fou B.png")
                        image.convert()
                        BFB1 = window.blit(image, [nbr_depl[compteur_depl] + 9, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "FB1"
                    if place_case[position] == "FB2":
                        image = pygame.image.load("Chess pieces Fou B.png")
                        image.convert()
                        BFB2 = window.blit(image, [nbr_depl[compteur_depl] + 9, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "FB2"
                    if place_case[position] == "FN1":
                        image = pygame.image.load("Chess pieces Fou N.png")
                        image.convert()
                        BFN1 = window.blit(image, [nbr_depl[compteur_depl] + 9, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "FN1"
                    if place_case[position] == "FN2":
                        image = pygame.image.load("Chess pieces Fou N.png")
                        image.convert()
                        BFN2 = window.blit(image, [nbr_depl[compteur_depl] + 9, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "FN2"
                    if place_case[position] == "RB":
                        image = pygame.image.load("Chess pieces Reine B.png")
                        image.convert()
                        BRB = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "RB"
                    if place_case[position] == "RN":
                        image = pygame.image.load("Chess pieces Reine N.png")
                        image.convert()
                        BRN = window.blit(image, [nbr_depl[compteur_depl] + 5, nbr_depl[compteur_depl + 1] + 8])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "RN"
                    if place_case[position] == "ROIB":
                        if PMRB == 0 and coor_case[16*2] == nbr_depl[compteur_depl] and coor_case[16*2+1] == nbr_depl[compteur_depl+1]:
                            pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[0], coor_case[1], 110, 110))
                            image = pygame.image.load("Chess pieces Tour B.png")
                            image.convert()
                            BTB1 = window.blit(image, [coor_case[24*2] + 13, coor_case[24*2+1] + 5])
                            place_case[0] = "V"
                            place_case[24] = "TB1"
                        if PMRB == 0 and coor_case[48*2] == nbr_depl[compteur_depl] and coor_case[48*2+1] == nbr_depl[compteur_depl+1]:
                            pygame.draw.rect(window, case_B, pygame.Rect(coor_case[56*2], coor_case[56*2+1], 110, 110))
                            image = pygame.image.load("Chess pieces Tour B.png")
                            image.convert()
                            BTB2 = window.blit(image, [coor_case[40*2] + 13, coor_case[40*2+1] + 5])
                            place_case[56] = "V"
                            place_case[40] = "TB2"
                        PMRB = 1
                        image = pygame.image.load("Chess pieces Roi B.png")
                        image.convert()
                        BROIB = window.blit(image, [nbr_depl[compteur_depl] + 10, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "ROIB"
                    if place_case[position] == "ROIN":
                        if PMRN == 0 and coor_case[23*2] == nbr_depl[compteur_depl] and coor_case[23*2+1] == nbr_depl[compteur_depl+1]:
                            pygame.draw.rect(window, case_B, pygame.Rect(coor_case[7*2], coor_case[7*2+1], 110, 110))
                            image = pygame.image.load("Chess pieces Tour N.png")
                            image.convert()
                            BTN1 = window.blit(image, [coor_case[31*2] + 13, coor_case[31*2+1] + 5])
                            place_case[7] = "V"
                            place_case[31] = "TN1"
                        if PMRN == 0 and coor_case[55*2] == nbr_depl[compteur_depl] and coor_case[55*2+1] == nbr_depl[compteur_depl+1]:
                            pygame.draw.rect(window, fond_color, pygame.Rect(coor_case[63*2], coor_case[63*2+1], 110, 110))
                            image = pygame.image.load("Chess pieces Tour N.png")
                            image.convert()
                            BTN2 = window.blit(image, [coor_case[47*2] + 13, coor_case[47*2+1] + 5])
                            place_case[63] = "V"
                            place_case[47] = "TN2"
                        PMRN = 1
                        image = pygame.image.load("Chess pieces Roi N.png")
                        image.convert()
                        BROIN = window.blit(image, [nbr_depl[compteur_depl] + 9, nbr_depl[compteur_depl + 1] + 5])
                        place_case[position] = "V"
                        if place_case[cas_depl[compteur_case_depl]] != "V":
                            mortp = place_case[cas_depl[compteur_case_depl]]
                            mort()
                        place_case[cas_depl[compteur_case_depl]] = "ROIN"
                    nbr_depl = []
                    cas_depl = []
                    compteur_tour += 1
                    if compteur_tour == 2:
                        compteur_tour = 0
                    if compteur_tour == 0:
                        pygame.draw.rect(window, fond_color, pygame.Rect(1105, 70, 170, 120))
                        font = pygame.font.SysFont("cambria", 50)
                        text = font.render("A votre", False, (255, 255, 255))
                        window.blit(text, [15, 70])
                        text = font.render("tour", False, (255, 255, 255))
                        window.blit(text, [50, 120])
                        blocTB = 1
                        blocTN = 0
                        TZB = time.time()
                    elif compteur_tour == 1:
                        pygame.draw.rect(window, fond_color, pygame.Rect(15, 70, 170, 120))
                        font = pygame.font.SysFont("cambria", 50)
                        text = font.render("A votre", False, (0, 0, 0))
                        window.blit(text, [1105, 70])
                        text = font.render("tour", False, (0, 0, 0))
                        window.blit(text, [1140, 120])
                        blocTB = 0
                        blocTN = 1
                        TZN = time.time()
                    break
                compteur_depl += 2
                compteur_case_depl += 1
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_30 and bloc_bout == 0:
            if mortf == 1:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(265, 655, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 660])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 660])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 660])
            else:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(265, 215, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 220])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 215, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 220])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 215, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 220])
            MINB = 30
            MINN = 30
            blocM = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_10 and bloc_bout == 0:
            if mortf == 1:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 660])
                bouton10M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(540, 655, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 660])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 660])
            else:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 215, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 220])
                bouton10M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(540, 215, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 220])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 215, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 220])
            MINB = 10
            MINN = 10
            blocM = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_5 and bloc_bout == 0:
            if mortf == 1:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 660])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 660])
                bouton5M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(815, 655, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 660])
            else:
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 215, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 220])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 215, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 220])
                bouton5M = pygame.draw.rect(window, (0, 255, 0), pygame.Rect(815, 215, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 220])
            MINB = 5
            MINN = 5
            blocM = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_f and bloc_bout == 0 and blocM == 1:
            blocM = 0
            bloc_bout = 1
            if mortf == 1:
                place_case = ["TB1", "PB1", "V", "V", "V", "V", "PN1", "TN1", "CB1", "PB2", "V", "V", "V", "V", "PN2","CN1", "FB1", "PB3", "V", "V", "V", "V", "PN3", "FN1", "RB", "PB4", "V", "V", "V", "V", "PN4", "RN", "ROIB", "PB5", "V", "V", "V", "V", "PN5", "ROIN", "FB2", "PB6", "V", "V", "V", "V", "PN6", "FN2", "CB2", "PB7", "V", "V", "V", "V", "PN7", "CN2", "TB2", "PB8", "V", "V", "V", "V", "PN8", "TN2"]
                mortn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                nbr_depl = []
                coor_case = []
                cas_depl = []
                compteur_tour = 0
                position = 64
                XM = 0
                YM = 0
                SB = 0
                MSB = 0
                SN = 0
                MSN = 0
                blocTN = 0
                pygame.draw.rect(window, fond_color, pygame.Rect(1105, 70, 170, 120))
                font = pygame.font.SysFont("cambria", 50)
                text = font.render("A votre", False, (255, 255, 255))
                window.blit(text, [15, 70])
                text = font.render("tour", False, (255, 255, 255))
                window.blit(text, [50, 120])
                pygame.draw.rect(window, fond_color, pygame.Rect(1110, 280, 200, 830))
                pygame.draw.rect(window, fond_color, pygame.Rect(50, 280, 200, 830))
            plateau()
            if mortf == 0:
                debut()
            else:
                for i in range(0, 8):
                    image = pygame.image.load("Chess pieces Pion B.png")
                    image.convert()
                    if i == 0:
                        BPB1 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 1:
                        BPB2 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 2:
                        BPB3 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 3:
                        BPB4 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 4:
                        BPB5 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 5:
                        BPB6 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 6:
                        BPB7 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                    if i == 7:
                        BPB8 = window.blit(image, [coor_case[2 + 16 * i] + 18, coor_case[3 + 16 * i] + 5])
                for i in range(0, 8):
                    image = pygame.image.load("Chess pieces Pion N.png")
                    image.convert()
                    if i == 0:
                        BPN1 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 1:
                        BPN2 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 2:
                        BPN3 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 3:
                        BPN4 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 4:
                        BPN5 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 5:
                        BPN6 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 6:
                        BPN7 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                    if i == 7:
                        BPN8 = window.blit(image, [coor_case[12 + 16 * i] + 18, coor_case[13 + 16 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Tour B.png")
                    image.convert()
                    if i == 0:
                        BTB1 = window.blit(image, [coor_case[112 * i] + 13, coor_case[1 + 112 * i] + 5])
                    if i == 1:
                        BTB2 = window.blit(image, [coor_case[112 * i] + 13, coor_case[1 + 112 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Tour N.png")
                    image.convert()
                    if i == 0:
                        BTN1 = window.blit(image, [coor_case[14 + 112 * i] + 13, coor_case[15 + 112 * i] + 5])
                    if i == 1:
                        BTN2 = window.blit(image, [coor_case[14 + 112 * i] + 13, coor_case[15 + 112 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Cheval B.png")
                    image.convert()
                    if i == 0:
                        BCB1 = window.blit(image, [coor_case[16 + 80 * i] + 5, coor_case[17 + 80 * i] + 5])
                    if i == 1:
                        BCB2 = window.blit(image, [coor_case[16 + 80 * i] + 5, coor_case[17 + 80 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Cheval N.png")
                    image.convert()
                    if i == 0:
                        BCN1 = window.blit(image, [coor_case[30 + 80 * i] + 5, coor_case[31 + 80 * i] + 5])
                    if i == 1:
                        BCN2 = window.blit(image, [coor_case[30 + 80 * i] + 5, coor_case[31 + 80 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Fou B.png")
                    image.convert()
                    if i == 0:
                        BFB1 = window.blit(image, [coor_case[32 + 48 * i] + 9, coor_case[33 + 48 * i] + 5])
                    if i == 1:
                        BFB2 = window.blit(image, [coor_case[32 + 48 * i] + 9, coor_case[33 + 48 * i] + 5])
                for i in range(0, 2):
                    image = pygame.image.load("Chess pieces Fou N.png")
                    image.convert()
                    if i == 0:
                        BFN1 = window.blit(image, [coor_case[46 + 48 * i] + 9, coor_case[47 + 48 * i] + 5])
                    if i == 1:
                        BFN2 = window.blit(image, [coor_case[46 + 48 * i] + 9, coor_case[47 + 48 * i] + 5])
                image = pygame.image.load("Chess pieces Reine B.png")
                image.convert()
                BRB = window.blit(image, [coor_case[48] + 5, coor_case[49] + 8])
                image = pygame.image.load("Chess pieces Reine N.png")
                image.convert()
                BRN = window.blit(image, [coor_case[62] + 5, coor_case[63] + 8])
                image = pygame.image.load("Chess pieces Roi B.png")
                image.convert()
                BROIB = window.blit(image, [coor_case[64] + 10, coor_case[65] + 5])
                image = pygame.image.load("Chess pieces Roi N.png")
                image.convert()
                BROIN = window.blit(image, [coor_case[78] + 9, coor_case[79] + 5])
                mortf = 0
            font = pygame.font.SysFont("cambria", 50)
            text = font.render("A votre", False, (255, 255, 255))
            window.blit(text, [15, 70])
            text = font.render("tour", False, (255, 255, 255))
            window.blit(text, [50, 120])
            blocTB = 1
            TZB = time.time()
            font = pygame.font.SysFont("cambria", 50)
            pygame.draw.rect(window, fond_color, pygame.Rect(1100, 820, 170, 120))
            pygame.draw.rect(window, fond_color, pygame.Rect(10, 820, 170, 120))
            if MINB == 5:
                text = font.render("0" + str(MINB) + " : " + str(SB) + "0", False, (255, 255, 255))
            else:
                text = font.render(str(MINB) + " : " + str(SB) + "0", False, (255, 255, 255))
            window.blit(text, [10, 820])
            font = pygame.font.SysFont("cambria", 50)
            if MINN == 5:
                text = font.render("0" + str(MINN) + " : " + str(SN) + "0", False, (0, 0, 0))
            else:
                text = font.render(str(MINN) + " : " + str(SN) + "0", False, (0, 0, 0))
            window.blit(text, [1100, 820])
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB1 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB1"):
                    position = place_case.index("PB1")
                    if position == 1:
                        debut_P = 1
                    if NR[0] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB2 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB2"):
                    position = place_case.index("PB2")
                    if position == 9:
                        debut_P = 1
                    if NR[1] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB3 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB3" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB3"):
                    position = place_case.index("PB3")
                    if position == 17:
                        debut_P = 1
                    if NR[2] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB3 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB4 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB4" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB4"):
                    position = place_case.index("PB4")
                    if position == 25:
                        debut_P = 1
                    if NR[3] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB4 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB5 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB5" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB5"):
                    position = place_case.index("PB5")
                    if position == 33:
                        debut_P = 1
                    if NR[4] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB5 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB6 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB6" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB6"):
                    position = place_case.index("PB6")
                    if position == 41:
                        debut_P = 1
                    if NR[5] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB6 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB7 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB7" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB7"):
                    position = place_case.index("PB7")
                    if position == 49:
                        debut_P = 1
                    if NR[6] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB7 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PB8 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "PB8" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PB8"):
                    position = place_case.index("PB8")
                    if position == 57:
                        debut_P = 1
                    if NR[7] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PB()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPB8 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN1 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN1"):
                    position = place_case.index("PN1")
                    if position == 6:
                        debut_P = 1
                    if NR[8] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN2 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN2"):
                    position = place_case.index("PN2")
                    if position == 14:
                        debut_P = 1
                    if NR[9] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN3 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN3" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN3"):
                    position = place_case.index("PN3")
                    if position == 22:
                        debut_P = 1
                    if NR[10] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN3 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN4 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN4" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN4"):
                    position = place_case.index("PN4")
                    if position == 30:
                        debut_P = 1
                    if NR[11] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN4 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN5 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN5" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN5"):
                    position = place_case.index("PN5")
                    if position == 38:
                        debut_P = 1
                    if NR[12] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN5 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN6 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN6" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN6"):
                    position = place_case.index("PN6")
                    if position == 46:
                        debut_P = 1
                    if NR[13] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN6 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN7 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN7" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN7"):
                    position = place_case.index("PN7")
                    if position == 54:
                        debut_P = 1
                    if NR[14] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN7 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_PN8 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "PN8" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("PN8"):
                    position = place_case.index("PN8")
                    if position == 62:
                        debut_P = 1
                    if NR[15] == 1:
                        poss_depl_T()
                        poss_depl_F()
                    else:
                        poss_depl_PN()
                    debut_P = 0
                else:
                    position = 64
            else:
                BPN8 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_TB1 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "TB1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("TB1"):
                    position = place_case.index("TB1")
                    poss_depl_T()
                else:
                    position = 64
            else:
                BTB1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_TB2 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "TB2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("TB2"):
                    position = place_case.index("TB2")
                    poss_depl_T()
                else:
                    position = 64
            else:
                BTB2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_TN1 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "TN1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("TN1"):
                    position = place_case.index("TN1")
                    poss_depl_T()
                else:
                    position = 64
            else:
                BTN1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_TN2 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "TN2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("TN2"):
                    position = place_case.index("TN2")
                    poss_depl_T()
                else:
                    position = 64
            else:
                BTN2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_CB1 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "CB1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("CB1"):
                    position = place_case.index("CB1")
                    poss_depl_C()
                else:
                    position = 64
            else:
                BCB1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_CB2 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "CB2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("CB2"):
                    position = place_case.index("CB2")
                    poss_depl_C()
                else:
                    position = 64
            else:
                BCB2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_CN1 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "CN1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("CN1"):
                    position = place_case.index("CN1")
                    poss_depl_C()
                else:
                    position = 64
            else:
                BCN1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_CN2 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "CN2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("CN2"):
                    position = place_case.index("CN2")
                    poss_depl_C()
                else:
                    position = 64
            else:
                BCN2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_FB1 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "FB1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("FB1"):
                    position = place_case.index("FB1")
                    poss_depl_F()
                else:
                    position = 64
            else:
                BFB1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_FB2 and bloc_bout == 1 and compteur_tour == 0:
            mortd = "FB2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("FB2"):
                    position = place_case.index("FB2")
                    poss_depl_F()
                else:
                    position = 64
            else:
                BFB2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_FN1 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "FN1" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("FN1"):
                    position = place_case.index("FN1")
                    poss_depl_F()
                else:
                    position = 64
            else:
                BFN1 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_FN2 and bloc_bout == 1 and compteur_tour == 1:
            mortd = "FN2" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("FN2"):
                    position = place_case.index("FN2")
                    poss_depl_F()
                else:
                    position = 64
            else:
                BFN2 = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_RB and bloc_bout == 1 and compteur_tour == 0:
            mortd = "RB" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("RB"):
                    position = place_case.index("RB")
                    poss_depl_T()
                    poss_depl_F()
                else:
                    position = 64
            else:
                BRB = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_RN and bloc_bout == 1 and compteur_tour == 1:
            mortd = "RN" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("RN"):
                    position = place_case.index("RN")
                    poss_depl_T()
                    poss_depl_F()
                else:
                    position = 64
            else:
                BRN = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_ROIB and bloc_bout == 1 and compteur_tour == 0:
            mortd = "ROIB" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("ROIB"):
                    position = place_case.index("ROIB")
                    if position == 32 and PMRB == 0:
                        debut_R = 1
                    poss_depl_R()
                    debut_R = 0
                else:
                    position = 64
            else:
                BROIB = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
                bouton = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(505, 435, 270, 80), 5)
                font = pygame.font.SysFont("cambria", 70)
                text = font.render("Rejouer", False, ecrit_color)
                window.blit(text, [515, 425])
                text = font.render("Victoire ", False, ecrit_color)
                window.blit(text, [330, 210])
                text = font.render("des Noirs", False, (0, 0, 0))
                window.blit(text, [620, 210])
                text = font.render("!", False, ecrit_color)
                window.blit(text, [930, 210])
                bloc_bout = 0
                mortf = 1
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 660])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 660])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 660])
        elif event.type == pygame.MOUSEBUTTONDOWN and clic_ROIN and bloc_bout == 1 and compteur_tour == 1:
            mortd = "ROIN" in place_case
            if mortd == True:
                supp_pos()
                nbr_depl = []
                cas_depl = []
                if position != place_case.index("ROIN"):
                    position = place_case.index("ROIN")
                    if position == 39 and PMRN == 0:
                        debut_R = 1
                    poss_depl_R()
                    debut_R = 0
                else:
                    position = 64
            else:
                BROIN = pygame.draw.rect(window, fond_color, pygame.Rect(0, 0, 0, 0))
                bouton = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(505, 435, 270, 80), 5)
                font = pygame.font.SysFont("cambria", 70)
                text = font.render("Rejouer", False, ecrit_color)
                window.blit(text, [515, 425])
                text = font.render("Victoire ", False, ecrit_color)
                window.blit(text, [330, 210])
                text = font.render("des Blancs", False, (255, 255, 255))
                window.blit(text, [600, 210])
                text = font.render("!", False, ecrit_color)
                window.blit(text, [945, 210])
                bloc_bout = 0
                mortf = 1
                font = pygame.font.SysFont("cambria", 50)
                bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                text = font.render("30 MIN", False, ecrit_color)
                window.blit(text, [280, 660])
                bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                text = font.render("10 MIN", False, ecrit_color)
                window.blit(text, [555, 660])
                bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                text = font.render("5 MIN", False, ecrit_color)
                window.blit(text, [850, 660])

    if blocTB == 1 and mortf == 0:
        TB = time.time() - TZB
        font = pygame.font.SysFont("cambria", 50)
        if TB >= 1:
            if MINB > 0 or SB >= 20:
                change = int(TB)
                while change >= 1:
                    if SB == 0:
                        MINB -= 1
                        SB = 59
                    else:
                        if MINB == 0:
                            if SB != 20:
                                SB -= 1
                        else:
                            SB -= 1
                    change -= 1
                pygame.draw.rect(window, fond_color, pygame.Rect(10, 820, 170, 120))
                if len(str(SB)) == 1:
                    if len(str(MINB)) == 1:
                        text = font.render("0" + str(MINB) + " : " + "0" + str(SB), False, (255, 255, 255))
                    else:
                        text = font.render(str(MINB) + " : " + "0" + str(SB), False, (255, 255, 255))
                else:
                    if len(str(MINB)) == 1:
                        text = font.render("0" + str(MINB) + " : " + str(SB), False, (255, 255, 255))
                    else:
                        text = font.render(str(MINB) + " : " + str(SB), False, (255, 255, 255))
                window.blit(text, [10, 820])
                TZB = time.time()
        TB = time.time() - TZB
        if TB > 0.1 and MINB == 0 and SB <= 20:
            if SB > 0:
                change = round(TB, 1)
                while change >= 0.1:
                    if MSB == 0:
                        if SB != 0:
                            SB -= 1
                            MSB = 9
                    else:
                        MSB -= 1
                    change -= 0.1
                pygame.draw.rect(window, fond_color, pygame.Rect(10, 820, 170, 120))
                if SB == 0:
                    text = font.render(str(MINB) + "0" + " : " + "0" + str(SB), False, (255, 0, 0))
                    bouton = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(505, 435, 270, 80), 5)
                    font = pygame.font.SysFont("cambria", 70)
                    text = font.render("Rejouer", False, ecrit_color)
                    window.blit(text, [515, 425])
                    text = font.render("Victoire ", False, ecrit_color)
                    window.blit(text, [330, 210])
                    text = font.render("des Noirs", False, (0, 0, 0))
                    window.blit(text, [620, 210])
                    text = font.render("!", False, ecrit_color)
                    window.blit(text, [930, 210])
                    bloc_bout = 0
                    mortf = 1
                    font = pygame.font.SysFont("cambria", 50)
                    bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                    text = font.render("30 MIN", False, ecrit_color)
                    window.blit(text, [280, 660])
                    bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                    text = font.render("10 MIN", False, ecrit_color)
                    window.blit(text, [555, 660])
                    bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                    text = font.render("5 MIN", False, ecrit_color)
                    window.blit(text, [850, 660])
                elif SB < 10:
                    text = font.render(str(MINB) + " : " + "0" + str(SB) + "." + str(MSB), False, (255, 0, 0))
                    window.blit(text, [10, 820])
                else:
                    text = font.render(str(MINB) + " : " + str(SB) + "." + str(MSB), False, (255, 0, 0))
                    window.blit(text, [10, 820])
            TZB = time.time()
    if blocTN == 1 and mortf == 0:
        TN = time.time() - TZN
        font = pygame.font.SysFont("cambria", 50)
        if TN >= 1:
            if MINN > 0 or SN >= 20:
                change = int(TN)
                while change >= 1:
                    if SN == 0:
                        MINN -= 1
                        SN = 59
                    else:
                        if MINN == 0:
                            if SN != 20:
                                SN -= 1
                        else:
                            SN -= 1
                    change -= 1
                pygame.draw.rect(window, fond_color, pygame.Rect(1100, 820, 170, 120))
                if len(str(SN)) == 1:
                    if len(str(MINN)) == 1:
                        text = font.render("0" + str(MINN) + " : " + "0" + str(SN), False, (0, 0, 0))
                    else:
                        text = font.render(str(MINN) + " : " + "0" + str(SN), False, (0, 0, 0))
                else:
                    if len(str(MINN)) == 1:
                        text = font.render("0" + str(MINN) + " : " + str(SN), False, (0, 0, 0))
                    else:
                        text = font.render(str(MINN) + " : " + str(SN), False, (0, 0, 0))
                window.blit(text, [1100, 820])
                TZN = time.time()
        TN = time.time() - TZN
        if TN > 0.1 and MINN == 0 and SN <= 20:
            if SN > 0:
                change = round(TN, 1)
                while change >= 0.1:
                    if MSN == 0:
                        if SN != 0:
                            SN -= 1
                            MSN = 9
                    else:
                        MSN -= 1
                    change -= 0.1
                pygame.draw.rect(window, fond_color, pygame.Rect(1100, 820, 170, 120))
                if SN == 0:
                    text = font.render(str(MINN) + "0" + " : " + "0" + str(SN), False, (255, 0, 0))
                    bouton = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(505, 435, 270, 80), 5)
                    font = pygame.font.SysFont("cambria", 70)
                    text = font.render("Rejouer", False, ecrit_color)
                    window.blit(text, [515, 425])
                    text = font.render("Victoire ", False, ecrit_color)
                    window.blit(text, [330, 210])
                    text = font.render("des Blancs", False, (255, 255, 255))
                    window.blit(text, [600, 210])
                    text = font.render("!", False, ecrit_color)
                    window.blit(text, [945, 210])
                    bloc_bout = 0
                    mortf = 1
                    font = pygame.font.SysFont("cambria", 50)
                    bouton30M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(265, 655, 200, 70), 5)
                    text = font.render("30 MIN", False, ecrit_color)
                    window.blit(text, [280, 660])
                    bouton10M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(540, 655, 200, 70), 5)
                    text = font.render("10 MIN", False, ecrit_color)
                    window.blit(text, [555, 660])
                    bouton5M = pygame.draw.rect(window, (141, 21, 137), pygame.Rect(815, 655, 200, 70), 5)
                    text = font.render("5 MIN", False, ecrit_color)
                    window.blit(text, [850, 660])
                elif SN < 10:
                    text = font.render(str(MINN) + " : " + "0" + str(SN) + "." + str(MSN), False, (255, 0, 0))
                    window.blit(text, [1100, 820])
                else:
                    text = font.render(str(MINN) + " : " + str(SN) + "." + str(MSN), False, (255, 0, 0))
                    window.blit(text, [1100, 820])
            TZN = time.time()
    pygame.display.flip()
