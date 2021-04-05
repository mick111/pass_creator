#!/usr/bin/python3
# coding: utf-8


from creator_transavia import TRANSAVIA_PASS
from creator_oui import OUI_PASS
import time

import cgi
form = cgi.FieldStorage()

PASS_TYPE = form.getvalue("pass_type")

if PASS_TYPE == "OUI":
    FROM = (form.getvalue("ville-depart").upper(), form.getvalue("depart").upper())
    TO = (form.getvalue("ville-arrivee").upper(), form.getvalue("arrivee").upper())
    DEPART = form.getvalue("date") + 'T' + form.getvalue("heure-depart") + '+01:00'
    ARRIVEE = form.getvalue("date") + 'T' + form.getvalue("heure-arrivee") + '+01:00'
    NOM = form.getvalue("nom").upper()
    PRENOM = form.getvalue("prenom").upper()
    NUM_TRAIN = form.getvalue("num_train")

    FICHIER = 'OUI_PASS'+str(time.time())
    OUI_PASS(FROM, TO, DEPART, ARRIVEE, NOM, PRENOM, NUM_TRAIN, FICHIER)

elif PASS_TYPE == "TRANSAVIA":
    FROM = (form.getvalue("depart_code").upper(), form.getvalue("depart"))
    TO = (form.getvalue("arrivee_code").upper(), form.getvalue("arrivee"))
    EMBARQUEMENT = form.getvalue("date") + 'T' + form.getvalue("heure_embarquement") + '+01:00'
    NOM_PRENOM = form.getvalue("nom") + ' ' + form.getvalue("prenom").upper()
    TERMINAL = form.getvalue("terminal")
    FLIGHT = form.getvalue("num_vol")
    SEAT = form.getvalue("num_siege")
    ZONE = form.getvalue("zone")

    FICHIER = 'TRANSAVIA_PASS'+str(time.time())
    TRANSAVIA_PASS(FICHIER, FROM, TO, EMBARQUEMENT, NOM_PRENOM, TERMINAL, FLIGHT, SEAT, ZONE)

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
