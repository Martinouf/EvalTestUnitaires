import locale
import time

from momentJournee import MomentJournee
from Anglais import Anglais
from Francais import Francais
from detecteurPalindrome import DetecteurPalindromme


class Last:

    def __init__(self):
        self.__lang = Anglais()
        if locale.getdefaultlocale()[0] == 'fr_FR':
            self.__lang = Francais()

        hour = time.localtime().tm_hour
        self.__moment = MomentJournee.INCONNU
        if 6 <= hour <= 12:
            self.__moment = MomentJournee.MATIN
        elif 13 <= hour <= 17:
            self.__moment = MomentJournee.APRES_MIDI
        elif 18 <= hour <= 23:
            self.__moment = MomentJournee.SOIR
        else:
            self.__moment = MomentJournee.NUIT


        print(self.__lang, self.__moment)

    def detect(self):
        mot = input("Choisir un mot : ")
        detecteur = DetecteurPalindromme(self.__lang, self.__moment)
        return detecteur.detect(mot)


last = Last()
print(last.detect())