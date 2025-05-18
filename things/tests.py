# things/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Thing


class ThingModelTest(TestCase):
    def test_create_thing(self):
        thing = Thing.objects.create(name="Test Thing", description="Just testing.")
        self.assertEqual(thing.name, "Test Thing")
        self.assertEqual(str(thing), "Test Thing")

    def test_get_absolute_url(self):
        thing = Thing.objects.create(name="Test Thing", description="Just testing.")
        self.assertEqual(
            thing.get_absolute_url(),
            reverse("things:thing_detail", args=[str(thing.id)]),
        )


class ThingViewTest(TestCase):
    def setUp(self):
        self.thing = Thing.objects.create(
            name="Sample Thing", description="Sample description."
        )

    def test_list_view(self):
        response = self.client.get(reverse("things:thing_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Thing")

    def test_detail_view(self):
        response = self.client.get(reverse("things:thing_detail", args=[self.thing.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Thing")

    def test_create_view(self):
        response = self.client.post(
            reverse("things:thing_create"),
            {"name": "New Thing", "description": "New description."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Thing.objects.filter(name="New Thing").exists())

    def test_update_view(self):
        response = self.client.post(
            reverse("things:thing_update", args=[self.thing.id]),
            {"name": "Updated Thing", "description": "Updated description."},
        )
        self.assertEqual(response.status_code, 302)
        self.thing.refresh_from_db()
        self.assertEqual(self.thing.name, "Updated Thing")

    def test_delete_view(self):
        response = self.client.post(
            reverse("things:thing_delete", args=[self.thing.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Thing.objects.filter(id=self.thing.id).exists())
