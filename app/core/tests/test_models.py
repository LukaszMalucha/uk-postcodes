from django.test import TestCase
from core.models import PostcodeModel





class PostcodeModelTests(TestCase):


    def setUp(self):
        self.postcode = PostcodeModel.objects.create(
            postcode="Test",
            lat="232",
            long="123",
            county="test",
            district="test",
            ward="test ok",
            constituency="test",
        )

    def tearDown(self):
        self.postcode.delete()

    def test_postcode(self):
        self.assertEqual(self.postcode.postcode, "Test")

    def test_erratic_postcode(self):
        self.assertNotEqual(self.postcode.postcode, "error")

    def test_string(self):
        self.assertEqual(str(self.postcode), "Test")


