from momentJournee import MomentJournee


class Francais:
    def bienDit(self):
        return "Bien dit"

    def bonjour(self, moment):
        if moment == MomentJournee.SOIR or moment == MomentJournee.NUIT:
            return "Bonsoir"
        return "Bonjour"

    def auRevoir(self, moment):

        if moment == MomentJournee.MATIN:
            return "Bonne journée"
        if moment == MomentJournee.APRES_MIDI:
            return "Bon après midi"
        if moment == MomentJournee.SOIR:
            return "Bonne soirée"
        if moment == MomentJournee.NUIT:
            return "Bonne nuit"

        return "Au revoir"

    def __str__(self):
        return "Langue Francaise"
