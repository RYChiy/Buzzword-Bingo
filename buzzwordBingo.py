
from fpdf import FPDF
from blessed import Terminal
from time import sleep
import random
from termcolor import colored



term = Terminal()

#Durch diese Methode wird eine für PDF geeignete Bingokarte erstellt       
def generate_card_multiplayer(laenge,breite,line):
        
        card = { 
            
            } 
        second_line=[]
        for num in line:
            
            second_line.append(num)
        for x in range(0,laenge):
            card[str(x+1)]=[random.choices(second_line,k=breite)]
           
            for o in card[str(x+1)][0]:  
                if str(o) in second_line:
                    second_line.remove(str(o))
        for letter in card:
            if letter=='2':
                if laenge==3 & breite==3:
                    card[letter][0][1] = "X" 
            elif letter =='3':
                if laenge==5 & breite==5:
                    card[letter][0][2] = "X"
            elif letter=='4':
                if laenge==7 & breite==7:
                    card[letter][0][3] = "X"
       
        return card

#Generierung einer Bingokarte
def generate_card(laenge,breite,line):
        
        
        card = { 
            
            } 
        second_line=[]
        for num in line:
            
            second_line.append(num)
        for x in range(0,laenge):
            card[str(x+1)]=[random.choices(second_line,k=breite)]
           
            for o in card[str(x+1)][0]:  
                if str(o) in second_line:
                    second_line.remove(str(o))
                
        #Einsetzen der Joker in die Karte
        for letter in card:
            if letter=='2':
                if laenge==3 & breite==3:
                    card[letter][0][1] =colored('         x          ','grey','on_white')
            elif letter =='3':
                if laenge==5 & breite==5:
                    card[letter][0][2] =colored('         x          ','grey','on_white')
            elif letter=='4':
                if laenge==7 & breite==7:
                    card[letter][0][3] =colored('         x          ','grey','on_white')
       
        return card

#Worte werden mit Leerzeichen verlängert, um eine saubere Darstellung zu garantieren
def card_order(card,laenge):
    for letter in card:
        for x in range(0,laenge):
            word=card[letter][0][x]
            length=len(word)
            if length<20:
                zahl=20-len(card[letter][0][x])
                
                wort=card[letter][0][x]
                card[letter][0][x]=wort+(zahl)*" "

#Methode zur Ausgabe der Karte im Terminal
def print_card(card):
    
    for letter in card:
        
        print('\t')
        print(letter,end=':\t')
        print('  '.join(card[letter][0]))

#Wörter werden aus Liste gezogen
def draw(line):

    word_drawn = random.choice(line) 
    line.remove(word_drawn)     
    return word_drawn  
    

#Methode, welche die Gewinne nachprüft
def check_win(card,laenge,breite):

    win = False
    #Zunächst werden die horizontalen Gewinnmöglichkeiten geprüft
    
    for letter in card:
        cnt=0
        
        for x in range(0,int(laenge)):

            if card[letter][0][x]==colored('         x          ','grey','on_white'):
                cnt+=1
            
        if cnt==int(laenge):
            win=True
            return win
            
    #jetzt werden die vertikalen Gewinnmöglichkeiten geprüft
    for x in range(0,int(laenge)):
        cnt=0

        for letter in card:
           if card[letter][0][x]==colored('         x          ','grey','on_white'):
               cnt+=1
        if cnt==int(laenge):
            win=True
            return win

    # jetzt werden die diagonalen Gewinnmöglichkeiten geprüft
    for x in range (0,int(laenge)):
        y=0
        cnt=0
        for letter in card:
            if card[letter][0][y]==colored('         x          ','grey','on_white'):
                cnt+=1
            y+=1
        if cnt==int(laenge):
            win=True
            return win

    for x in range (int(laenge),-1,-1):
        y=int(laenge)-1
        cnt=0
        for letter in card:
            if card[letter][0][y]==colored('         x          ','grey','on_white'):
                cnt+=1
            y-=1
        if cnt==int(laenge):
            win=True
        return win

#Methode zum Makieren/Durchstreichen der gezogenen Wörter
def durchstreichen(zahl_1,zahl_2,card):
    card[zahl_1][0][int(zahl_2)]=colored('         x          ','grey','on_white')


print(term.home + term.clear + term.move_y(term.height // 2))

#Textdatei mit den für das Bingo benötigten Buzzwords
datei = open('bingowoerter.txt','r')
line=[]
line = datei.read().split('•')


#Einleitung in das Spiel
print(term.clear+term.center('''
    LADIES UND GENTLEMEN!!!!
    HERZLICH WILLKOMMEN ZUM BINGO-SPIELEABEND!!

    Zunächst erfassen wir die von ihnen gewünschten Seitenmaße
    für ihre Bingokarten!

    Bitte geben Sie zunächst die Höhe der Bingokarte ein!'''))

with term.cbreak():
    laenge = term.inkey()


print(term.clear+term.center('Bitte geben Sie die Breite der Bingokarte ein.'))
#Eingabe wird direkt eingelesen
with term.cbreak():
    breite = term.inkey()


print(term.clear+term.center('''
    Was möchten Sie heute spielen?
    Geben Sie bitte eine der folgenden Ziffern ein, um einen der beiden Modi zu spielen!!
    

    1: Einzelspieler
    2: Mehrspieler'''))

with term.cbreak():
    modus=term.inkey()

bingo_karten=[]

win=False
#Einzelspielermodus
if modus=='1':
    
    einzelspieler=generate_card(int(laenge),int(breite),line)
    bingo_karten.append(einzelspieler)
    
    card_order(bingo_karten[0],int(laenge))
    anzahl_spieler=1
    for x in range(0,anzahl_spieler):
        print_card(bingo_karten[x]) 


    print('''
    NUN BEGINNT DAS SPIEL!!
    Es werden aus einer Liste, Wörter entnommen und wenn diese
    in ihrer Bingokarte vorkommen, markieren sie diese!!!

    WIR WÜNSCHEN IHNEN VIEL SPAß UND NOCH VIEL ERFOLG ;-)

    ''')

    win=False


    for x in range(0,int(anzahl_spieler)):
        print("\nDrücke Enter um ein neues Wort zu ziehen.\nZum Beenden, schribe bitte quit.\n")
        user_input = term.inkey()
        win=check_win(bingo_karten[x],int(laenge),int(breite))
        words_till_win = 0
        
        
        #Hauptsächliche While-Schleife des Einzelspielermodus
        while win == False and user_input != "quit":
            word_drawn = draw(line)
            words_till_win += 1
            #gezogenes Wort wird aus der Liste gestrichen
            
            
            
            print(term.clear+"\nGezogenes Wort:"+colored(f'{word_drawn}.','grey','on_white'))
            print(f"Anzahl an gezogenen Wörtern: {words_till_win}.\n")
            print('Um ein Wort durchzustreichen, so geben Sie bitte x ein')
            print_card(bingo_karten[x])

            #In jedem Durchlauf wird geprüft, ob der Spieler gewonnen hat
            win=check_win(bingo_karten[x],int(laenge),int(breite))

            if win==True:
                print(term.clear+term.center(''))
                print(term.home + term.on_blue + term.clear)
                print(term.center(f"Herzlichen Glückwunsch!\n"))
                
                print(term.center(("Sie haben gewonnen!\n\n")))
                
                print(term.center((f"So viele Wörter wurden bis zum Sieg gezogen: {words_till_win}")))
         
            
            user_input=input()
            

            if user_input =='x':
                    zahl_oder_keine_zahl=False
                    #Es wird nachgeprüft, ob es sich um gültige ZIffern handelt, oder nicht
                    while zahl_oder_keine_zahl!=True:
                        zahl_1=input('1. Koordinate: ')

                        zahl_2=input('2. Koordinate: ')
                    
                    
                        if zahl_1.isnumeric() and zahl_2.isnumeric():
                            durchstreichen(zahl_1,(int(zahl_2)-1),einzelspieler)
                            zahl_oder_keine_zahl=True

                        else:
                            print('Bitte geben Sie zwei gültige Ziffern ein!')
                        

            elif user_input=="quit":
                print(term.clear+term.center('Vielen Dank fürs Mitspielen!'))
                quit()


#Programm für den Mehrspielermodus
if modus=='2': 
    
    print(term.clear+term.center('Bitte geben Sie an, wie viele Personen am Bingospiel teilnehmen möchten!'))
    
    anzahl_spieler=input()
    
    #Bingokarten werden für alle Spieler erstellt
    for x in range(0,int(anzahl_spieler)):
        
        bingo_karten.append(generate_card_multiplayer(int(laenge),int(breite),line))
        card_order(bingo_karten[x],int(laenge))

    #for-Schleife, zum Übertragen der Bingokarten in PDF-Dateien
    for x in range(0,int(anzahl_spieler)):
        pdf =FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)

        card=bingo_karten[x]
        card_order(card,int(laenge))
        for letter in card:


                pdf.cell(200,10,txt=letter,ln=1,align='C')
                pdf.cell(200,10,txt='| '.join(card[letter][0]),ln=0,align='C')
                
        pdf.output('Karte'+str(x+1)+'.pdf','F')
        
        
    timer=input(term.clear+'Bitte Zeitabstand zwischen die Wörtern angeben: \n')

    print(f'''
    NUN BEGINNT DAS SPIEL!!!
    Aus einer Liste werden nun alle {timer} Sekunden ein Wort gezogen, und wenn dieses
    in Ihrer Bingokarte vorkommt, so streichen Sie es durch oder Markieren Sie es.

    WIR WÜNSCHEN IHNEN VIEL SPAß UND ERFOLG AUF DEN SIEG ;-)

    ''')
    

    win=False
    for x in range(0,int(anzahl_spieler)):
        user_input = input()
        words_till_win = 0

        #Hauptsächlische While-Schleife des Multiplayers
        while win == False:
            word_drawn = draw(line)
            words_till_win += 1
            #gezogenes Wort wird aus der Liste gestrichen
            
            
            
            print(term.clear+colored(f"\nGezogenes Wort: {word_drawn}.",'grey','on_white'))
            print(f"Anzahl an gezogenen Wörtern: {words_till_win}.\n\n\n")
           
            sleep(int(timer))

            
            
            
