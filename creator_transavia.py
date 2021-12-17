#!/usr/bin/env python3

from passbook.models import (
    Pass,
    Barcode,
    BoardingPass,
    DateField,
    BarcodeFormat,
    Field,
    DateStyle,
    NumberField,
    TransitType,
    Alignment,
)
from os.path import expanduser
import datetime

def TRANSAVIA_PASS(dest, FROM, TO, EMBARQUEMENT, NOM_PRENOM, TERMINAL, FLIGHT, SEAT, ZONE):
    cardInfo = BoardingPass(transitType=TransitType.AIR)
    field = Field("date", EMBARQUEMENT.strftime("%d %b"), "Date")
    field.textAlignment = Alignment.NATURAL
    cardInfo.headerFields.append(field)

    field = Field("fli", FLIGHT, "Flight")
    field.textAlignment = Alignment.CENTER
    cardInfo.headerFields.append(field)

    cardInfo.primaryFields.append(Field("src", FROM[0], FROM[1]))
    field = Field("dst", TO[0], TO[1])
    field.textAlignment = Alignment.NATURAL
    cardInfo.primaryFields.append(field)

    cardInfo.auxiliaryFields.append(
        Field("nam", NOM_PRENOM, "Passager")
    )

    field = Field("ter", TERMINAL, "Terminal")
    field.textAlignment = Alignment.CENTER
    cardInfo.auxiliaryFields.append(field)

    field = Field("sea", SEAT, "Siège")
    field.textAlignment = Alignment.CENTER
    cardInfo.auxiliaryFields.append(field)

    field = Field("zon", ZONE, "Zone")
    field.textAlignment = Alignment.RIGHT
    cardInfo.auxiliaryFields.append(field)

    field = DateField(
        "boa",
        EMBARQUEMENT.isoformat(),
        "Boarding",
        dateStyle=DateStyle.NONE,
        timeStyle=DateStyle.SHORT,
    )
    cardInfo.secondaryFields.append(field)

    field = Field(
        "dur",
        "1:00",
        "Durée de vol",
    )
    field.textAlignment = Alignment.RIGHT
    cardInfo.secondaryFields.append(field)

    cardInfo.backFields.append(
        Field(
            "acs",
            """Le terminal de l'aérodrome The Game se situe au <a href="https://maps.apple.com/?address=6%20Rue%20de%20la%20Harpe,%2075005%20Paris,%20France&auid=14148564957634573501&ll=48.852927,2.344476&lsp=9902&q=The%20Game&_ext=CisKBAgEEHoKBAgFEAMKBQgGEN8BCgQIChAACgQIUhACCgQIVRAOCgQIWRABEiYpd44S9plsSEAx0ZAjdJmzAkA59WM4UsBtSEBBo+RINY/PAkBQBA%3D%3D&t=r">6 rue de la Harpe 75005 Paris</a>""",
            "Accès au terminal"
        )
    )

    cardInfo.backFields.append(
        Field(
            "svc",
            """TheGame Airlines vous propose toute une gamme de rafraîchissements dès votre arrivée dans notre terminal d'embarquement. Jus d'orange, thé glacé et café... à volonté pour votre plus grand confort. Retrouvez également notre Magazine pour faire passer le temps durant votre vol...""", 
            "Nos services à bord",
        )
    )
    cardInfo.backFields.append(
        Field("mor", """Nous avons mis en place une <a href="http://9ogu.mjt.lu/lnk/CAAAAmTDWgQAAAAAAAAAAR4qWN8AALQJix0AAAAAAAwbTwBhvFGqf8uNRHzDQLe3vSX6eKsIYwAMJnY/2/qpmowiQheKKUSDKKZU5IHA/aHR0cHM6Ly93d3cudGhlZ2FtZS1mcmFuY2UuY29tL2ZyL2NvdmlkLTE5Lmh0bQ">série de mesures</a> que nous jugeons essentielles, ce qui ne vous empêchera pas de vivre un moment fun et convivial !
Et sous nos masques gardons le sourire !""", "Covid 19 - Mesures Sanitaires")
    )
    cardInfo.backFields.append(
        Field("pas", """En plus de ces mesures, la présentation du Pass Sanitaire est obligatoire pour les joueurs de 12 ans et plus. Nous vous invitons à privilégier ce pass sous format numérique via l'application Tous Anti Covid afin d'éviter tout problème à la lecture du QR code. Retrouvez toutes nos informations sur ce pass en suivant <a href="http://9ogu.mjt.lu/lnk/CAAAAmTDWgQAAAAAAAAAAR4qWN8AALQJix0AAAAAAAwbTwBhvFGqf8uNRHzDQLe3vSX6eKsIYwAMJnY/3/zcOSDpgl2hZ2FQRqCtiyFQ/aHR0cHM6Ly93d3cudGhlZ2FtZS1mcmFuY2UuY29tL2ZyL2NvdmlkLTE5Lmh0bQ">""", "Covid 19 - Mesures Sanitaires")
    )
    organizationName = "The Game"
    passTypeIdentifier = "pass.com.sear.app"
    teamIdentifier = "836469M6XW"

    passfile = Pass(
        cardInfo,
        passTypeIdentifier=passTypeIdentifier,
        organizationName=organizationName,
        teamIdentifier=teamIdentifier,
    )
    passfile.serialNumber = "AZERTYUIPT"
    passfile.barcode = Barcode(
        message=f"M1{NOM_PRENOM.replace(' ','/').upper()}       U7EDGF {FROM[0]}{TO[0]}{FLIGHT} 093Y009D0080 147>1181WW1092BTO 0000000000000299790000000000 0                          ",
        format=BarcodeFormat.QR,
        altText="seq. nr. " + FLIGHT + ":80"
    )

    passfile.labelColor = "rgb(37, 150, 190)"
    passfile.foregroundColor = "rgb(96, 96, 96)"
    passfile.backgroundColor = "rgb(255, 255, 255)"

    passfile.description = "The Game boardingpass"

    passfile.relevantDate = EMBARQUEMENT.isoformat()

    # Including the icon and logo is necessary for the passbook to be valid.
    passfile.addFile("icon.png", open("images/vh2tz.png", "rb"))
    passfile.addFile("logo@2x.png", open("images/vh2tz.png", "rb"))
    passfile.addFile("logo.png", open("images/vh2tz.png", "rb"))

    # Create and output the Passbook file (.pkpass)
    password = open(expanduser("~") + "/pass_creator/passcreatorpwd.txt").read()
    return passfile.create(
        "certs/certificate.pem",
        expanduser("~") + "/pass_creator/private.key",
        "certs/wwdr.pem",
        password,
        "passes/" + dest + ".pkpass",
    )


if __name__ == "__main__":
    TO = ("ORY", "Paris-Orly")
    FROM = ("ACE", "Arrecife (Lanzarote)")
    EMBARQUEMENT = datetime.datetime.fromisoformat("2021-10-10T22:51+02:00")
    NOM_PRENOM = "Arnaud Maillet"
    TERMINAL = "1"
    SEAT = "9D"
    ZONE = "2"
    FLIGHT = "TO3151"
    FICHIER = "toto"
    print(EMBARQUEMENT.isoformat())
    TRANSAVIA_PASS(FICHIER, FROM, TO, EMBARQUEMENT, NOM_PRENOM, TERMINAL, FLIGHT, SEAT, ZONE)
