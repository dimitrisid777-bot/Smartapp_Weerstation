def aantal_dagen(inputFile):
    bestand = open(inputFile, 'r')
    regels = bestand.readlines()
    bestand.close()

    return len(regels) - 1  # We willen de eerste regel skippen dus we doen - 1

print(aantal_dagen('smartapp_input.txt')) #print het aantal dagen (aantal regels in txtfiel)



def auto_bereken(inputFile, outputFile):
    bestand = open(inputFile, 'r')
    regels = bestand.readlines()
    bestand.close()

    for regel in regels[1:]:
        delen = regel.split()
        print(delen)

auto_bereken('smartapp_input.txt', 'output.txt')




