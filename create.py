#!/usr/bin/python3
# coding: utf-8


from creator_oui import OUI_PASS
import time

import cgi
form = cgi.FieldStorage()


FROM = (form.getvalue("ville-depart").upper(), form.getvalue("depart").upper())
TO = (form.getvalue("ville-arrivee").upper(), form.getvalue("arrivee").upper())
DEPART = form.getvalue("date") + 'T' + form.getvalue("heure-depart") + '+02:00'
ARRIVEE = form.getvalue("date") + 'T' + form.getvalue("heure-arrivee") + '+02:00'
NOM = form.getvalue("nom").upper()
PRENOM = form.getvalue("prenom").upper()
NUM_TRAIN = form.getvalue("num_train")

FICHIER = 'OUI_PASS'+str(time.time())

oui_pass = OUI_PASS(FROM, TO, DEPART, ARRIVEE, NOM, PRENOM, NUM_TRAIN, FICHIER)

print("Content-type: text/html; charset=utf-8\n")

html = f"""<!DOCTYPE html>
<head>
<meta name = "viewport" content = "width = device-width">
    <title>Pass Creator</title>
    <link href="/styles/style.css" rel="stylesheet" type="text/css">
    <meta http-equiv="refresh" content="2; URL=/passes/{FICHIER}.pkpass" />
</head>
<body>
  <a href="/passes/{FICHIER}.pkpass" style="display: block;text-align: center;"><img src="/img/Add_to_Apple_Wallet_rgb_FR.svg"/></a>
</body>
</html>
"""
print(html)
