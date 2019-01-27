#Prueft die Eingabedatei aera.in
def file_pruefen(file):

    #Anzahl der Eintraege zaehlen
    anzahl_koordinaten=0
    for line in file:
        anzahl_koordinaten = anzahl_koordinaten+1

    #Wenn es weniger als 3 oder mehr als 1000 Eintraege gibt, ist die Datei
    #unguelitg
    if anzahl_koordinaten<3 or anzahl_koordinaten > 1000:
        return False
    return True


#Nimmt die Koordinaten und berechnet den Flaecheninhalt des Polygon
def dreiecksformel(x, y):
    flaeche = 0.0

    #n ist die Anzahl der Eintraege
    n = len(x)

    #Gausssche Dreiecksformel
    i = 0
    while i<n:
        flaeche += (y[i] + y[(i+1) % n]) * (x[i] - x[(i+1) % n])
        i = i+1

    flaeche = abs(flaeche/2.0)
    return flaeche



#Gibt den Abstand zwischen zwei Punkten (x1,y1) und (x2,y2) zurück
def dist(x1, y1, x2, y2):
    ergebnis = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5
    return ergebnis



#Berechnet aus den Koordinaten den Umfang des Polygon
def umfang_berechnen(x, y):
    umfang = 0.0
    i=0
    n = len(x)
    while i<n-1:
        umfang += dist(x[i], y[i], x[i+1], y[i+1])
        i = i+1
    umfang += dist(x[n-1], y[n-1], x[0], y[0])
    return umfang
    
    

def main():
    #Die Datei, aus der die Koordinaten gelesen werden sollen
    eingabedatei = "aera.in"
    
    #Die x und y Koordinaten werden jeweils in seperaten Listen gespeichert
    x_koordinaten = []
    y_koordinaten = []
    
    #Pruefen der Eingabedatei
    file = open(eingabedatei, "r")
    if (file_pruefen(file)==False):
      return "Es waren zu wenig oder zu viele Koordinaten in der Datei"


    #Einlesen der Eingabedatei und speichern der Daten in den Listen
    file = open(eingabedatei, "r")
    for line in file:
        zeile = line.split(" ")
        x_koordinaten.append(float(zeile[1]))
        y_koordinaten.append(float(zeile[2]))

    #Berechnungen der geforderten Werte
    flaeche = dreiecksformel(x_koordinaten, y_koordinaten)
    umfang = umfang_berechnen(x_koordinaten, y_koordinaten)


    #Schreiben der Ergebnisse in die Output-Datei
    output = open("aera.out", "w")
    output.write("Fläche: " + str(flaeche) + " qm\n")
    output.write("Flächenumfang: " + str(umfang) + " m\n")
    output.close()

    return True

    
    
    
print(main())

