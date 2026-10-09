import json
import urllib.request
import urllib.error


#Deze functie haalt weergegevens op via Open Meteo
def live_weer():

    #De coordinaten van Utrecht en de gegevens die we willen
    url = (
        'https://api.open-meteo.com/v1/forecast'
        '?latitude=52.09&longitude=5.12'
        '&current=temperature_2m,relative_humidity_2m,wind_speed_10m'
        '&wind_speed_unit=ms'
        '&timezone=Europe%2FAmsterdam'
    )

    try:
        #We maken verbinding en lezen het antwoord van de api
        with urllib.request.urlopen(url, timeout=10) as antwoord:
            gegevens = json.load(antwoord)

        #We halen de waarden uit het JSON antwoord
        huidig = gegevens['current']

        temperatuur = huidig['temperature_2m']
        vochtigheid = huidig['relative_humidity_2m']
        wind = huidig['wind_speed_10m']

        # We tonen de resultaten aan de gebruiker
        print('\n================================')
        print('       LIVE WEER UTRECHT')
        print('================================')
        print(f'Temperatuur: {temperatuur} C')
        print(f'Luchtvochtigheid: {vochtigheid}%')
        print(f'Windsnelheid: {wind} m/s')
        print('================================')

    except (urllib.error.URLError, TimeoutError, OSError):
        #Bijvoorbeeld als er geen internetverbinding is
        print('\nKan het weer niet ophalen. Controleer je internetverbinding.')

    except (KeyError, ValueError, TypeError):
        #Als de api ongeldige of ontbrekende gegevens terugstuurt
        print('\nDe weergegevens konden niet verwerkt worden.')


#Alleen direct starten als we dit bestand zelf uitvoeren
if __name__ == '__main__':
    live_weer()
