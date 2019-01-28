import math

#Prueft die Eingabedatei
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

    
#Berechnet den Richtungswinkel    
def riwi(x1, x2, y1, y2):
    return math.atan2(x1-x2, y1-y2)



#Wandelt rad in gon um
def rho(rad):
    return 63.6619772368*rad


#Ueberfuehren eines Winkels in den Geltungsbereich 0<=Winkel<400 gon
def keep0400(winkel_gon):
    return winkel_gon % 400


#Berechnet den Winkel in Gon im geforderten Geltungsbereich
def winkel_berechnen(x1, x2, y1, y2):
    winkel_rad = riwi(x1, x2, y1, y2)
    winkel_gon = rho(winkel_rad)
    
    return keep0400(winkel_gon)


#Winkel
def main():
    #Die Datei, aus der die Koordinaten gelesen werden sollen
    eingabedatei = "aera.in"
    
    #Die x und y Koordinaten werden jeweils in seperaten Listen gespeichert
    punkt_ids = []
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
        punkt_ids.append(int(zeile[0]))
        x_koordinaten.append(float(zeile[1]))
        y_koordinaten.append(float(zeile[2]))

    #Flaeche und Umfang berechnen
    flaeche = dreiecksformel(x_koordinaten, y_koordinaten)
    umfang = umfang_berechnen(x_koordinaten, y_koordinaten)

    
    #Öffnen der Output Datei
    output = open("aera.out", "w")

    #Winkel und Entfernung berechnen und in Output Datei schreiben
    n = len(x_koordinaten)
    i = 0
    while(i<n-1):
        output.write("Von:  Punkt {:d}".format(punkt_ids[i]) +
                     " mit Rechtswert {:6.3f}".format(x_koordinaten[i]) +
                     " und Hochwert {:7.3f}".format(y_koordinaten[i]) + "\n")
        output.write("Von:  Punkt {:d}".format(punkt_ids[i+1]) +
                     " mit Rechtswert {:6.3f}".format(x_koordinaten[i+1]) +
                     " und Hochwert {:7.3f}".format(y_koordinaten[i+1]) + "\n")

        #Winkel berechnen
        winkel = winkel_berechnen(x_koordinaten[i], x_koordinaten[i+1],
                          y_koordinaten[i], y_koordinaten[i+1])
        output.write("Richtungswinkel: {:f}".format(winkel) + " gon\n")
        
        #Entfernung berechnen
        entfernung = dist(x_koordinaten[i], y_koordinaten[i], x_koordinaten[i+1],
                          y_koordinaten[i+1])
        output.write("Entfernung: {:f}".format(entfernung) + " m\n\n")
        i += 1

    #Winkel & Entfernung zwischen letztem und erstem Punkt
    output.write("Von:  Punkt {:d}".format(punkt_ids[n-1]) +
                     " mit Rechtswert {:6.3f}".format(x_koordinaten[n-1]) +
                     " und Hochwert {:7.3f}".format(y_koordinaten[n-1]) + "\n")
    output.write("Von:  Punkt {:d}".format(punkt_ids[0]) +
                     " mit Rechtswert {:6.3f}".format(x_koordinaten[0]) +
                     " und Hochwert {:7.3f}".format(y_koordinaten[0]) + "\n")

    winkel = winkel_berechnen(x_koordinaten[n-1], x_koordinaten[0],
                          y_koordinaten[n-1], y_koordinaten[0])
    output.write("Richtungswinkel: {:f}".format(winkel) + " gon\n")
        
    entfernung = dist(x_koordinaten[n-1], y_koordinaten[n-1],
                      x_koordinaten[0], y_koordinaten[0])
    output.write("Entfernung: {:f}".format(entfernung) + " m\n\n")



    
    output.write("Fläche:        {:f}".format(flaeche) + " qm\n")
    output.write("Flächenumfang: {:f}".format(umfang) + " m\n")
    output.close()

    return True

    
    
    
print(main())

