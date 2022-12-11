from unittest import TestCase

from blenderdata import BlenderDataDict


class TestBlenderDataDict(TestCase):
    def test_get_dict(self):
        self.assertEqual({}, BlenderDataDict.get_dict(None))
