import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_ottaminen_toimii_saldo_riittaa(self):
        result = self.maksukortti.ota_rahaa(500)
        self.assertTrue(result)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_ottaminen_toimii_saldo_ei_riita(self):
        result = self.maksukortti.ota_rahaa(1200)
        self.assertFalse(result)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
