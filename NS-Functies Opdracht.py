def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0
    if afstandKM <= 50:
        prijs = afstandKM * 0.80
    else:
        prijs = 15 + afstandKM * 0.60

    return (prijs)


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit and (leeftijd >= 12 and leeftijd < 65):
        prijs = prijs * 0.60
    elif weekendrit:
        prijs = prijs * 0.65
    elif leeftijd < 12 or leeftijd >= 65:
        prijs = prijs * 0.70

    return (prijs)

print(standaardprijs(25))
print(ritprijs(19,True,25))














