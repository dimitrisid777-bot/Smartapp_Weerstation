#We importeren onze drie applicaties
from Weerstation import weerstation
from SmartApp_Controller import smart_app_controller
from live_weer import live_weer


#Dit is het hoofdmenu van mijn Smart Hub
def hoofdmenu():

    #De while loop zorgt dat het menu blijft terugkomen
    while True:
        print('\n====================================')
        print("         DIMITRI'S SMART HUB")
        print('====================================')
        print('1: Weerstation')
        print('2: Smart App Controller')
        print('3: Live weer Utrecht')
        print('4: Stoppen')
        print('====================================')

        #De gebruiker kiest een applicatie
        keuze = input('\nMaak een keuze: ')

        if keuze == '1':
            #Sprint 1 starten
            weerstation()

        elif keuze == '2':
            #Sprint 2 starten
            smart_app_controller()

        elif keuze == '3':
            #weergegevens ophalen via Open Meteo
            live_weer()

        elif keuze == '4':
            #Het hele platform afsluiten
            print('\nBedankt voor het gebruiken van Smart Hub!')
            break

        else:
            #Ongeldige menukeuze netjes afhandelen
            print('\nOngeldige keuze! Probeer opnieuw.')


#Het programma starten
if __name__ == '__main__':
    hoofdmenu()
