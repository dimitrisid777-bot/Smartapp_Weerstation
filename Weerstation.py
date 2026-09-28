#sprint1
def fahrenheit(temp_celcius):
    return 32 + (temp_celcius * 1.8)

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    if gevoel < 0 and windsnelheid > 10:
        return 'Het is heel koud en het stormt! Verwarming helemaal aan!'
    elif gevoel < 0 and windsnelheid <= 10:
        return 'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!'
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return 'Het is best koud en het waait; verwarming aan en roosters dicht!'
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return 'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!'
    elif 10 <= gevoel < 22:
        return 'Heerlijk weer, niet te koud of te warm.'
    else:
        return 'Warm! Airco aan!'

def weerstation():
    totaal = 0
    for dag in range(1, 8):
        temp = input(f'Wat is op dag {dag} de temperatuur[C]: ')
        if temp == '':
            print('bye')
            return
        temp = float(temp)

        wind = input(f'Wat is op dag {dag} de windsnelheid[m/s]: ')
        if wind == '':
            print('bye')
            return
        wind = float(wind)

        vocht = input(f'Wat is op dag {dag} de vochtigheid[%]: ')
        if vocht == '':
            print('bye')
            return
        vocht = int(vocht)

        totaal = totaal + temp
        gemiddelde = totaal / dag

        print(f"Het is {temp:.1f}C {fahrenheit(temp):.1f}F")
        print(weerrapport(temp, wind, vocht))
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("=" * 38)

weerstation()

#sprint2

