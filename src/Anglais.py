from momentJournee import MomentJournee


class Anglais:
    def bienDit(self):
        return "Well said"

    def bonjour(self, moment):
        if moment == MomentJournee.MATIN:
            return "Good Morning"
        if moment == MomentJournee.APRES_MIDI:
            return "Good Afternoon"
        if moment == MomentJournee.SOIR:
            return "Good Evening"
        if moment == MomentJournee.NUIT:
            return "Good Night"

        return "Hello"

    def auRevoir(self, moment):

        if moment == MomentJournee.MATIN:
            return "Good bye am"
        if moment == MomentJournee.APRES_MIDI:
            return "Good bye pm"
        if moment == MomentJournee.SOIR:
            return "Good bye soir"
        if moment == MomentJournee.NUIT:
            return "Good bye nuit"

        return "Good bye"

    def __str__(self):
        return "Langue Anglaise"
