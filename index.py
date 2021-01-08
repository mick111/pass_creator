#!/usr/bin/python3
# coding: utf-8

import cgi
from datetime import datetime, timedelta

now = datetime.now()
before = now - timedelta(hours=2)

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

html = f"""<!DOCTYPE html>
<head>
    <meta name = "viewport" content = "width = device-width">
    <title>Pass Creator</title>
    <link href="/styles/style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <form action="/create.py" method="post">
    <table>
    <tbody>
        <tr>
            <td><label for="prenom">Prénom</label></td><td><input required type="text" id="prenom" name="prenom"></td>
        </tr>
        <tr>
            <td><label for="nom">Nom</label></td><td><input required type="text" id="nom" name="nom"></td>
        </tr>
        <tr>
            <td><label for="date">Date de voyage</label></td><td><input required type="date" id="date" name="date" value={before.strftime("%Y-%m-%d")}></td>
        </tr>
        <tr>
            <td><label for="ville-depart">Ville de départ</label></td><td><input required type="text" id="ville-depart" name="ville-depart" value="Le Havre"></td>
        </tr>
        <tr>
            <td><label for="depart">Gare de départ</label></td><td><input required type="text" id="depart" name="depart" value="Le Havre"></td>
        </tr>
        <tr>
            <td><label for="heure-depart">Heure de départ</label></td><td><input required type="time" id="heure-depart" name="heure-depart" value={before.strftime("%H:%M")}></td>
        </tr>
        <tr>
            <td><label for="ville-arrivee">Ville d'arrivée</label></td><td><input required type="text" id="ville-arrivee" name="ville-arrivee" value="Paris"></td>
        </tr>
        <tr>
            <td><label for="arrivee">Gare d'arrivée</label></td><td><input required type="text" id="arrivee" name="arrivee" value="Gare Saint-Lazare (Paris)"></td>
        </tr>
        <tr>
            <td><label for="heure-arrivee">Heure d'arrivée</label></td><td><input required type="time" id="heure-arrivee" name="heure-arrivee" value={now.strftime("%H:%M")}></td>
        </tr>
        <tr>
            <td><label for="num_train">Numéro de train</label></td><td><input required type="text" id="num_train" name="num_train" value=3109></td>
        </tr>
        <tr><td colspan="2" style="text-align:center;"><input style="margin-top: 5px !important;" style="margin:auto;" type="image" src="/img/Add_to_Apple_Wallet_rgb_FR.svg" alt="Submit Form"></td></tr>
    </tbody>
    </form>
    </table>
</body>
</html>
"""

print(html)
