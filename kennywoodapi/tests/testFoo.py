import unittest
from unittest import skip
from django.test import TestCase

class TestFoo(TestCase):
    # Have to pass in a reason for skipping
    # A skipped test will display as an 's' in your test results
    # and you will see "OK (skipped=1)" at the end of the test results
    @skip("demonsrating skipping")
    def test_foo(self):
        self.assertEqual(2 + 2, 5)
