import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Customer


class CustomerTests(TestCase):

    def test_first_published_a(self):
        self.assertEqual(0,0)
