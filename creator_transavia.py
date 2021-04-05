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
    field.textAlignment = Alignment.RIGHT
    cardInfo.headerFields.append(field)

    field = Field("fli", FLIGHT, "Flight")
    field.textAlignment = Alignment.RIGHT
    cardInfo.headerFields.append(field)

    cardInfo.primaryFields.append(Field("src", FROM[0], FROM[1]))
    field = Field("dst", TO[0], TO[1])
    field.textAlignment = Alignment.RIGHT
    cardInfo.primaryFields.append(field)

    cardInfo.secondaryFields.append(field)

    cardInfo.auxiliaryFields.append(
        Field("nam", NOM_PRENOM, "Passenger")
    )

    field = Field("ter", TERMINAL, "Terminal")
    field.textAlignment = Alignment.RIGHT
    cardInfo.auxiliaryFields.append(field)

    field = Field("sea", SEAT, "Seat")
    field.textAlignment = Alignment.RIGHT
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

    field = DateField(
        "gat",
        (EMBARQUEMENT + datetime.timedelta(minutes=15)).isoformat(),
        "Gate closed",
        dateStyle=DateStyle.NONE,
        timeStyle=DateStyle.SHORT,
    )
    field.textAlignment = Alignment.RIGHT
    cardInfo.secondaryFields.append(field)

    field = DateField(
        "dep",
        (EMBARQUEMENT + datetime.timedelta(minutes=30)).isoformat(),
        "Departure",
        dateStyle=DateStyle.NONE,
        timeStyle=DateStyle.SHORT,
    )
    field.textAlignment = Alignment.RIGHT
    cardInfo.secondaryFields.append(field)

    cardInfo.backFields.append(
        Field(
            "hnd",
            """You are permitted 1 piece of hand luggage per adult/child of max. 10 kg.
You can choose from:
1 piece of hand luggage of max. 45x40x25 cm. Guaranteed to be allowed into the cabin.
or
1 piece of hand luggage of max. 55x40x25 cm. Keep in mind that it will be transported as hold luggage on crowded flights.
If you are only traveling with hand luggage, you can go straight to security and onto your gate.

<a href="https://www.transavia.com/en-NL/faq/hand-luggage/">More information about hand luggage</a>
""", 
            "Hand luggage",
        )
    )
    cardInfo.backFields.append(
        Field(
            "dro",
            "Are you travelling with hold luggage or special luggage? You can drop it off at the 'baggage drop-off' counters. If there is no drop-off counter, you can check in your bags at the check-in desk.",
            "Dropping off luggage at the airport",
        )
    )
    cardInfo.backFields.append(
        Field("ont", "Make sure you arrive at the airport well ahead of time (at least 2 hours before departure). This way, you can start your trip without any stress and make sure we can depart on time.", "Go to the airport on time")
    )

    cardInfo.backFields.append(
        Field("mor", "On the <a href='https://www.transavia.com/en-EU/service'>website of Transavia</a> you will find all the information to prepare for your trip.", "More information")
    )

    organizationName = "Transavia.sncf"
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
        format=BarcodeFormat.QR,
        altText="seq. nr. " + FLIGHT + ":80"
    )

    passfile.labelColor = "rgb(26, 209, 89 )"
    passfile.foregroundColor = "rgb(96, 96, 96)"
    passfile.backgroundColor = "rgb(255, 255, 255)"

    passfile.description = "Transavia"

    passfile.relevantDate = EMBARQUEMENT.isoformat()

    # Including the icon and logo is necessary for the passbook to be valid.
    passfile.addFile("icon.png", open("images/logo-transavia.png", "rb"))
    passfile.addFile("logo@2x.png", open("images/logo-transavia@2x.png", "rb"))
    passfile.addFile("logo.png", open("images/logo-transavia.png", "rb"))

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
