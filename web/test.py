from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.test import Client
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

import os

from django.test import TestCase

class SiteTestCase(TestCase):
    def setUp(self):
        site = Site(domain='test.leaguebits.com', name="Test Site")
        site.save()
        settings.SITE_ID = 1

    def tearDown(self):
        Site.objects.clear_cache()
        
    def test_site_manager(self):
        # Make sure that get_current() does not return a deleted Site object.
        s = Site.objects.get_current()
        self.assertIsInstance(s, Site)
        s.delete()
        with self.assertRaises(ObjectDoesNotExist):
            Site.objects.get_current()
            
    def test_site_by_domain(self):
        request = HttpRequest()
        request.META = {
            "SERVER_NAME": "test.leaguebits.com",
            "SERVER_PORT": "80",
        }
        
        site = get_current_site(request)
        self.assertIsInstance(site, Site)
        self.assertEqual(site.id, settings.SITE_ID)