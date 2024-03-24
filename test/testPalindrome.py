import os
import unittest

from Anglais import Anglais
from Francais import Francais
from momentJournee import MomentJournee
from utilities.detecteurPalindrommeBuilder import DetecteurPalindrommeBuilder

testNonPalindrome = ["maison", "truc", "ceiling-shot", "flip-rest"]


class TestPalindrome(unittest.TestCase):
    def testMirroir(self):
        for mot in testNonPalindrome:
            with(self.subTest(mot)):
                detecteur = DetecteurPalindrommeBuilder().build()
                resultat = detecteur.detect(mot)

                attendu = mot[::-1]
                self.assertIn(attendu, resultat)

    def testBienDit(self):

        cas = [[Francais(), "Bien dit"], [Anglais(), "Well said"]]

        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).build()
                resultat = detecteur.detect(palindrome)

                bienDit = param[1]

                attendu = palindrome + os.linesep + bienDit
                self.assertIn(attendu, resultat)

    def testBonjour(self):

        cas = [
            [Francais(), 'Bonjour', MomentJournee.INCONNU],
            [Francais(), 'Bonjour', MomentJournee.MATIN],
            [Francais(), 'Bonjour', MomentJournee.APRES_MIDI],
            [Francais(), 'Bonsoir', MomentJournee.SOIR],
            [Francais(), 'Bonsoir', MomentJournee.NUIT],
            [Anglais(), 'Hello', MomentJournee.INCONNU],
            [Anglais(), 'Good Morning', MomentJournee.MATIN],
            [Anglais(), 'Good Afternoon', MomentJournee.APRES_MIDI],
            [Anglais(), 'Good Evening', MomentJournee.SOIR],
            [Anglais(), 'Good Night', MomentJournee.NUIT],
        ]
        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                moment = param[2]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).ayantPourMoment(moment).build()
                resultat = detecteur.detect(palindrome)

                premiereLigne = resultat.split(os.linesep)[0]
                self.assertEqual(param[1], premiereLigne)

    def testAuRevoir(self):

        cas = [
            [Francais(), 'Au revoir', MomentJournee.INCONNU],
            [Francais(), 'Bonne journée', MomentJournee.MATIN],
            [Francais(), 'Bon après midi', MomentJournee.APRES_MIDI],
            [Francais(), 'Bonne soirée', MomentJournee.SOIR],
            [Francais(), 'Bonne nuit', MomentJournee.NUIT],
            [Anglais(), 'Good bye', MomentJournee.INCONNU],
            [Anglais(), 'Good bye am', MomentJournee.MATIN],
            [Anglais(), 'Good bye pm', MomentJournee.APRES_MIDI],
            [Anglais(), 'Good bye soir', MomentJournee.SOIR],
            [Anglais(), 'Good bye nuit', MomentJournee.NUIT],
        ]

        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                moment = param[2]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).ayantPourMoment(moment).build()
                resultat = detecteur.detect(palindrome)

                derniereLigne = resultat.split(os.linesep)[-1]
                self.assertEqual(param[1], derniereLigne)

    def testSautDeLigne(self):

        cas = [
            [Francais(), 'Au revoir', MomentJournee.INCONNU],
            [Francais(), 'Bonne journée', MomentJournee.MATIN], 
            [Francais(), 'Bon après midi', MomentJournee.APRES_MIDI],
            [Francais(), 'Bonne nuit', MomentJournee.NUIT],
            [Anglais(), 'Good bye', MomentJournee.INCONNU],
            [Anglais(), 'Good bye am', MomentJournee.MATIN],
            [Anglais(), 'Good bye pm', MomentJournee.APRES_MIDI],
            [Anglais(), 'Good bye soir', MomentJournee.SOIR],
            [Anglais(), 'Good bye nuit', MomentJournee.NUIT],
        ]

        for param in cas:
            with(self.subTest(param[0])):
                langue = param[0]
                moment = param[2]
                palindrome = 'kayak'

                detecteur = DetecteurPalindrommeBuilder().ayantPourLangue(langue).ayantPourMoment(moment).build()
                resultat = detecteur.detect(palindrome)

                derniereLigne = resultat.split(os.linesep)[-1]
                self.assertTrue(derniereLigne.find(os.linesep) == -1)