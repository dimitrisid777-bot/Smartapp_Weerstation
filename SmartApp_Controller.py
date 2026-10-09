
def aantal_dagen(inputFile):
    try:
        bestand = open(inputFile, 'r')
        regels = bestand.readlines()
        bestand.close()

        #Eerste regel met kolomnamen niet meetellen
        return max(0, len(regels) - 1)

    except FileNotFoundError:
        print('Fout: Het invoerbestand bestaat niet!')
        return None

    except OSError:
        print('Fout: Het invoerbestand kan niet gelezen worden!')
        return None


def auto_bereken(inputFile, outputFile):
    try:
        bestand = open(inputFile, 'r')
        regels = bestand.readlines()
        bestand.close()

    except FileNotFoundError:
        print('Fout: Het invoerbestand bestaat niet!')
        return False

    except OSError:
        print('Fout: Het invoerbestand kan niet gelezen worden!')
        return False

    uitvoer_regels = []

    #Eerste regel overslaan
    for regel in regels[1:]:
        delen = regel.split()

        try:
            datum = delen[0]
            aantal_mensen = int(delen[1])
            temp_setpoint = float(delen[2])
            temp_buiten = float(delen[3])
            neerslag = float(delen[4])

        except (ValueError, IndexError):
            print('Fout: Het invoerbestand bevat ongeldige gegevens!')
            return False

        #CV berekenen
        verschil = temp_setpoint - temp_buiten

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        #Ventilatie maximaal op stand 4
        ventilatie = aantal_mensen + 1

        if ventilatie > 4:
            ventilatie = 4

        #Bewatering bij minder dan 3 mm neerslag
        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer_regels.append(
            f'{datum};{cv};{ventilatie};{bewatering}\n'
        )

    try:
        with open(outputFile, 'w') as uitvoer:
            uitvoer.writelines(uitvoer_regels)

    except OSError:
        print('Fout: Het uitvoerbestand kan niet opgeslagen worden!')
        return False

    return True


def overwrite_settings(outputFile):
    try:
        with open(outputFile, 'r') as bestand:
            regels = bestand.readlines()

    except FileNotFoundError:
        print('Fout: Bereken eerst de actuatoren met optie 2!')
        return -2

    except OSError:
        print('Fout: Het uitvoerbestand kan niet gelezen worden!')
        return -2

    #Datum zoeken
    while True:
        datum = input('\nVoer een datum in (bijv. 05-10-2024): ')

        if datum == '':
            print('Bewerking geannuleerd.')
            return -4

        gevonden = False

        for regel in regels:
            delen = regel.strip().split(';')

            if delen[0] == datum:
                gevonden = True
                break

        if gevonden:
            break

        print('Datum niet gevonden! Probeer opnieuw.')

    #Systeem kiezen
    while True:
        print('\nKies een systeem:')
        print('1 = CV')
        print('2 = Ventilatie')
        print('3 = Bewatering')

        systeem = input('Maak een keuze: ')

        if systeem in ('1', '2', '3'):
            break

        if systeem == '':
            print('Bewerking geannuleerd.')
            return -4

        print('Ongeldig systeem! Kies 1, 2 of 3.')

    #Nieuwe waarde controleren
    while True:
        nieuwe_waarde = input('Voer de nieuwe waarde in: ')

        if nieuwe_waarde == '':
            print('Bewerking geannuleerd.')
            return -4

        if systeem == '1' or systeem == '2':
            try:
                nieuwe_waarde = int(nieuwe_waarde)

            except ValueError:
                print('Ongeldige invoer! Voer een geheel getal in.')
                continue

            if systeem == '1' and not (0 <= nieuwe_waarde <= 100):
                print('CV moet tussen 0 en 100 liggen!')
                continue

            if systeem == '2' and not (0 <= nieuwe_waarde <= 4):
                print('Ventilatie moet tussen 0 en 4 liggen!')
                continue

        elif systeem == '3':
            if nieuwe_waarde not in ('0', '1'):
                print('Bewatering moet 0 of 1 zijn!')
                continue

        break

    #De juiste regel aanpassen
    for i in range(len(regels)):
        delen = regels[i].strip().split(';')

        if delen[0] == datum:

            if systeem == '1':
                delen[1] = str(nieuwe_waarde)

            elif systeem == '2':
                delen[2] = str(nieuwe_waarde)

            elif systeem == '3':
                if nieuwe_waarde == '1':
                    delen[3] = 'True'
                else:
                    delen[3] = 'False'

            regels[i] = ';'.join(delen) + '\n'

    try:
        with open(outputFile, 'w') as bestand:
            bestand.writelines(regels)

    except OSError:
        print('Fout: Het uitvoerbestand kan niet aangepast worden!')
        return -2

    return 0


def smart_app_controller():
    inputFile = 'smartapp_input.txt'
    outputFile = 'output.txt'

    #Menu blijft terugkomen tot optie 4
    while True:
        print('\n=================================')
        print('       SMART APP CONTROLLER')
        print('=================================')
        print('1: Hoeveel dagen zijn er aanwezig?')
        print('2: Autobereken alle actuatoren')
        print('3: Overschrijf een berekende waarde')
        print('4: Stoppen')
        print('=================================')

        keuze = input('\nMaak een keuze: ')

        if keuze == '1':
            dagen = aantal_dagen(inputFile)

            if dagen is not None:
                print(f'\nEr zijn {dagen} dagen aanwezig')

        elif keuze == '2':
            gelukt = auto_bereken(inputFile, outputFile)

            if gelukt:
                print('\nDe actuatoren zijn berekend en opgeslagen')

        elif keuze == '3':
            resultaat = overwrite_settings(outputFile)

            # Resultaat van het overschrijven
            if resultaat == 0:
                print('\nDe waarde is aangepast')
            elif resultaat == -1:
                print('\nDatum niet gevonden')
            elif resultaat == -2:
                print('\nDe bewerking kon niet worden uitgevoerd')
            elif resultaat == -3:
                print('\nOngeldig systeem of ongeldige waarde')
            elif resultaat == -4:
                print('\nTerug naar het menu.')

        elif keuze == '4':
            print('\nProgramma gestopt')
            break

        else:
            print('\nOngeldige keuze! Probeer opnieuw.')


if __name__ == '__main__':
    smart_app_controller()
