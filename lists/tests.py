from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',
        data={
            'item_text': 'A new list item'
        })

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


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

        self.assertEqual(first_item.text, first_saved_item.text)
        self.assertEqual(second_item.text, second_saved_item.text)
