def aantal_dagen(inputFile):
    bestand = open(inputFile, 'r')
    regels = bestand.readlines()
    bestand.close()

    return len(regels) - 1  # We willen de eerste regel skippen dus we doen - 1


def auto_bereken(inputFile, outputFile):
    bestand = open(inputFile, 'r')
    regels = bestand.readlines()
    bestand.close()

    uitvoer = open(outputFile, 'w')

    for regel in regels[1:]:
        delen = regel.split()

        datum = delen[0]
        aantal_mensen = int(delen[1])
        temp_setpoint = float(delen[2])
        temp_buiten = float(delen[3])
        neerslag = float(delen[4])

        verschil = temp_setpoint - temp_buiten

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = aantal_mensen + 1

        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(f'{datum};{cv};{ventilatie};{bewatering}\n')

    uitvoer.close()


def overwrite_settings(outputFile):
    datum = input('\nVoer een datum in (bijv. 05-10-2024): ')

    bestand = open(outputFile, 'r')
    regels = bestand.readlines()
    bestand.close()

    gevonden = False

    for regel in regels:
        delen = regel.strip().split(';')

        if delen[0] == datum:
            gevonden = True

    if gevonden == False:
        return -1
    print('\nKies een systeem:')
    print('1 = CV')
    print('2 = Ventilatie')
    print('3 = Bewatering')

    systeem = input('Maak een keuze: ')

    if systeem != '1' and systeem != '2' and systeem != '3':
        return -3

    nieuwe_waarde = input('Voer de nieuwe waarde in: ')

    if systeem == '1':
        try:
            nieuwe_waarde = int(nieuwe_waarde)
        except ValueError:
            return -3

        if nieuwe_waarde < 0 or nieuwe_waarde > 100:
            return -3

    elif systeem == '2':
        try:
            nieuwe_waarde = int(nieuwe_waarde)
        except ValueError:
            return -3

        if nieuwe_waarde < 0 or nieuwe_waarde > 4:
            return -3

    elif systeem == '3':
        if nieuwe_waarde != '0' and nieuwe_waarde != '1':
            return -3

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

    bestand = open(outputFile, 'w')
    bestand.writelines(regels)
    bestand.close()

    return 0


def smart_app_controller():
    inputFile = 'smartapp_input.txt'
    outputFile = 'output.txt'

    while True:
        print('\nSmart App Controller')
        print('1: Hoeveel dagen zijn er aanwezig?')
        print('2: Autobereken alle actuatoren')
        print('3: Overschrijf een berekende waarde')
        print('4: Stoppen')

        keuze = input('\nMaak een keuze: ')

        if keuze == '1':
            dagen = aantal_dagen(inputFile)
            print(f'\nEr zijn {dagen} dagen aanwezig')

        elif keuze == '2':
            auto_bereken(inputFile, outputFile)
            print('\nDe actuatoren zijn berekend en opgeslagen')

        elif keuze == '3':
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print('\nDe waarde is aangepast')
            elif resultaat == -1:
                print('\nDatum niet gevonden')
            elif resultaat == -3:
                print('\nOngeldig systeem of ongeldige waarde')

        elif keuze == '4':
            print('\nProgramma gestopt')
            break

        else:
            print('Ongeldige keuze')


smart_app_controller()