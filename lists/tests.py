from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.first().text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')

        self.assertEqual(Item.objects.count(), 0)

    def test_saves_multiple_list_items(self):
        items = ['A new list item', 'Another list item']

        [
            self.client.post('/', data={'item_text': item})
            for item in items
            ]


        self.assertEqual(Item.objects.count(), 2)
        [
            self.assertIn(item, saved_item.text)
            for (item, saved_item)
            in zip(items, Item.objects.all())
            ]

    def test_displays_all_list_items(self):
        items = ['A new list item', 'Another list item']
        [Item.objects.create(text=item) for item in items]

        response = self.client.get('/')

        [
            self.assertIn(item, response.content.decode())
            for item in items
            ]

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        items = [first_item, second_item]

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 2)

        [self.assertEqual(item, saved_item) for (item, saved_item) in zip(items, saved_items)]

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
