#!/usr/bin/env python3

from passbook.models import (
    Pass,
    Barcode,
    BoardingPass,
    DateField,
    BarcodeFormat,
    Field,
    DateStyle,
    TransitType,
    Alignment,
)
from os.path import expanduser


def OUI_PASS(FROM, TO, DEPART, ARRIVEE, NOM, PRENOM, NUM_TRAIN, dest):
    cardInfo = BoardingPass(transitType=TransitType.TRAIN)
    field = DateField("date", DEPART, "VOYAGE DU")
    field.textAlignment = Alignment.RIGHT
    cardInfo.headerFields.append(field)

    cardInfo.primaryFields.append(Field("src", FROM[0], FROM[1]))
    field = Field("dst", TO[0], TO[1])
    field.textAlignment = Alignment.RIGHT
    cardInfo.primaryFields.append(field)

    cardInfo.secondaryFields.append(Field("nam", NOM, "NOM"))
    cardInfo.secondaryFields.append(Field("srn", PRENOM, "PRÉNOM"))

    cardInfo.auxiliaryFields.append(
        DateField(
            "dep", DEPART, "DÉPART", dateStyle=DateStyle.NONE, timeStyle=DateStyle.SHORT
        )
    )
    cardInfo.auxiliaryFields.append(Field("trn", f"N° {NUM_TRAIN}", "TRAIN"))
    cardInfo.auxiliaryFields.append(
        DateField(
            "arr",
            ARRIVEE,
            "ARRIVÉE",
            dateStyle=DateStyle.NONE,
            timeStyle=DateStyle.SHORT,
        )
    )

    cardInfo.backFields.append(
        Field(
            "ebl",
            "Le e-billet est nominatif, personnel et incessible. Une pièce d'identité pourra vous être demandée.",
            "E-BILLET",
        )
    )
    cardInfo.backFields.append(
        Field(
            "rec",
            "Il est conseillé de présenter le e-billet depuis votre application OUI.sncf.",
            "Recommandé pour le contrôle",
        )
    )
    cardInfo.backFields.append(
        Field("app", "http://bit.ly/appli_ouisncf", "Application OUI.sncf")
    )

    organizationName = "OUIOUI"
    passTypeIdentifier = "pass.com.sear.app"
    teamIdentifier = "836469M6XW"

    passfile = Pass(
        cardInfo,
        passTypeIdentifier=passTypeIdentifier,
        organizationName=organizationName,
        teamIdentifier=teamIdentifier,
    )
    passfile.serialNumber = "AZERTYUIOP"
    passfile.barcode = Barcode(
        message="Doudou slut slutDoudou slut slutDoudou slut slutDoudou slut slutDoudou slut slutDoudou slut slutDoudou slut slutDoudou slut slut   !!",
        format=BarcodeFormat.AZTEC,
    )

    passfile.labelColor = "rgb(120, 114, 100)"
    passfile.foregroundColor = "rgb(203, 70, 40)"
    passfile.backgroundColor = "rgb(255, 255, 255)"

    passfile.description = "OUI PASS"

    passfile.relevantDate = ARRIVEE

    # Including the icon and logo is necessary for the passbook to be valid.
    passfile.addFile("icon.png", open("images/logo-oui.png", "rb"))
    passfile.addFile("logo@2x.png", open("images/logo-oui@2x.png", "rb"))
    passfile.addFile("logo.png", open("images/logo-oui.png", "rb"))

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
    TO = ("Paris", "GARE SAINT LAZARE (PARIS)")
    FROM = ("LE HAVRE", "LE HAVRE")
    DEPART = "2020-01-07T23:00+02:00"
    ARRIVEE = "2020-01-07T23:57+02:00"
    NOM = "MMM"
    PRENOM = "ARNAUD"
    NUM_TRAIN = "3109"
    FICHIER = "toto"
    OUI_PASS(FROM, TO, DEPART, ARRIVEE, NOM, PRENOM, NUM_TRAIN, FICHIER)
