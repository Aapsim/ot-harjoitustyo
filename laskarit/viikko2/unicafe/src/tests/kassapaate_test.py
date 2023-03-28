import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def test_kassassa_rahaa_oikea_alussa(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_ei_myyty_alussa(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.edulliset, 0)

    def test_maukkaita_lounaita_ei_myyty_alussa(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.maukkaat, 0)

    def test_edullinen_kateisosto_raha_riittaa(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(kassa.kassassa_rahaa, 100240)
        self.assertEqual(kassa.edulliset, 1)

    def test_edullinen_kateisosto_raha_ei_riita(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukas_kateisosto_raha_riittaa(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assertEqual(kassa.kassassa_rahaa, 100400)
        self.assertEqual(kassa.maukkaat, 1)

    def test_maukas_kateisosto_raha_ei_riita(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 0)

    def test_edullinen_korttiosto_raha_riittaa(self):
        kassa = Kassapaate()
        kortti = Maksukortti(500)
        tulos = kassa.syo_edullisesti_kortilla(kortti)
        self.assertTrue(tulos)
        self.assertEqual(kortti.saldo, 260)
        self.assertEqual(kassa.edulliset, 1)

    def test_edullinen_korttiosto_raha_ei_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        tulos = kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukas_korttiosto_raha_riittaa(self):
        kassa = Kassapaate()
        kortti = Maksukortti(1000)
        tulos = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tulos, True)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(kassa.maukkaat, 1)

    def test_maukas_korttiosto_raha_ei_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(200)
        tulos = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tulos, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(kassa.maukkaat, 0)
    


    def test_maukas_kateisosto_raha_ei_riita_mutta_kortilla_riittaa(self):
        kassa = Kassapaate()
        kortti = Maksukortti(1000)
        kassa.syo_edullisesti_kortilla(kortti)
        vaihtoraha = kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 0)
        self.assertEqual(kortti.saldo, 760)

    def test_edullinen_korttiosto_raha_ei_riita_eika_kortilla_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        tulos = kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukas_korttiosto_raha_ei_riita_eika_kortilla_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        tulos = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassa.maukkaat, 0)

    def test_kortille_lataaminen_toimii(self):
        kassa = Kassapaate()
        kortti = Maksukortti(0)
        kassa.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(kassa.kassassa_rahaa, 101000)

    def test_kortille_lataaminen_negatiivisella_summalla_ei_toimi(self):
        kassa = Kassapaate()
        kortti = Maksukortti(0)
        kassa.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(kassa.kassassa_rahaa, 100000)