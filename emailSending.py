#!/usr/bin/python
# -*- coding: utf-8 -*-

import yagmail

class EmailSender:
    @staticmethod
    def SendMail(emailHost="smtp.gmail.com", emailPort=465, 
    senderEmailAdress="helperbotdevacc@gmail.com", receivers= ["blabak72@gmail.com", "emre.rauhofer@gmail.com"],
     appPassword="shevsscfesztaddu"):
        # In der finalen version lässt sich der email provider einstellen
        # In der finalen version lässt sich Username und Passwort einstellen
        subject = "Help me"
        message = [
            "I have fallen and I cant get back up",
            "Please help me!"
        ]

        try:
            with yagmail.SMTP(senderEmailAdress, appPassword) as yag:
                for receiver in receivers:
                    yag.send(receiver, subject, message)
                    pass
                pass
            return True
        except:
            return False