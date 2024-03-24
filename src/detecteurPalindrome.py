import os


class DetecteurPalindromme:

    def __init__(self, langue, moment):
        self.__langue = langue
        self.__moment = moment

    def detect(self, mot):
        reflect = mot[::-1]

        start = self.__langue.bonjour(self.__moment) + os.linesep + reflect
        end = os.linesep + self.__langue.auRevoir(self.__moment)

        if (reflect == mot):
            return start + os.linesep + self.__langue.bienDit() + end

        return start + end
