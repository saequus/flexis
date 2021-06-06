import ujson
from django.test import TestCase

class TestFlexi(TestCase):

    @staticmethod
    def url(param: str) -> str:
        return f'/flexis/{param}'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.temp = 1

    def setUp(self):
        self.new = 2

    def test_temp(self):
        self.assertEqual(self.temp, 1)


    def test_new(self):
        self.assertEqual(self.new, 2)

    def test_setting_key_view(self):
        res = self.client.get(self.url('setting-key'))
        content = ujson.loads(res.content)  
        self.assertEqual(content, {'value': 'ok', 'status': 'ok'})

    def test_non_existing(self):
        res = self.client.get(self.url('nonexisting'))
        content = ujson.loads(res.content)
        self.assertEqual(content, {'errors': 'object_not_found', 'status': 'error'})

