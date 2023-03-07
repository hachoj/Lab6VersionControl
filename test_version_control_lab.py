from unittest import TestCase
from version_control_lab import *


class Test(TestCase):
    def test_encoder(self):
        self.assertEqual('45678888', encoder('12345555'))
        self.assertEqual('345628', encoder('012395'))
