from momentJournee import MomentJournee
from src.detecteurPalindrome import DetecteurPalindromme
from utilities.LangueStub import LangueStub


class DetecteurPalindrommeBuilder:
    __langue = LangueStub()
    __moment = MomentJournee.INCONNU

    def build(self):
        return DetecteurPalindromme(self.__langue, self.__moment)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self

    def ayantPourMoment(self, moment):
        self.__moment = moment
        return self
