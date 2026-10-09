## Dimitri's Smart Hub

Dit is mijn Python-project voor Smart App. Tijdens de drie sprints heb ik verschillende applicaties gemaakt en deze uiteindelijk samengevoegd in één platform.

## Sprint 1 – Weerstation

In het weerstation kan de gebruiker voor maximaal 7 dagen de temperatuur, windsnelheid en luchtvochtigheid invoeren.

•Het programma berekent:

•De temperatuur in Fahrenheit

•De gevoelstemperatuur en een weerrapport

De gemiddelde temperatuur van de ingevoerde dagen

Met try/except wordt verkeerde invoer opgevangen, zodat de gebruiker opnieuw kan invoeren.

## Sprint 2 – Smart App Controller

De Smart App Controller leest gegevens uit een tekstbestand en berekent automatisch de instellingen voor de CV-ketel, ventilatie en bewatering.

De gebruiker kan:

•Het aantal dagen in het bestand bekijken
•Automatisch de actuatoren berekenen
•Een berekende waarde overschrijven

De resultaten worden opgeslagen in output.txt. Bij ongeldige invoer krijgt de gebruiker een foutmelding en kan deze opnieuw proberen.

## Sprint 3 – Platform

In Sprint 3 heb ik de eerdere applicaties samengevoegd in één hoofdmenu.

Daarnaast heb ik de Open-Meteo API toegevoegd, waarmee actuele weergegevens uit Utrecht worden opgehaald.

Het platform bestaat uit:

•Weerstation

•Smart App Controller

•Live weer Utrecht

•Stoppen

## Bestanden

•main.py – Hoofdmenu van het platform

•Weerstation.py – Sprint 1

•SmartApp_Controller.py – Sprint 2

•live_weer.py – Open-Meteo API

•smartapp_input.txt – Invoergegevens voor de controller

•output.txt – Berekende actuatorwaarden

•BRONNEN.md – Gebruikte bronnen en documentatie

## Programma starten

1.Open het project in PyCharm.

2.Zorg dat alle bestanden in dezelfde projectmap staan.

3.Start main.py.

4.Kies een optie uit het menu.

## Bronnen

De gebruikte bronnen staan in BRONNEN.md.