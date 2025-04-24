from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Category, Company

class CategoryViewTests(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(name="CompanyTest1")

    def test_list(self):
        url = reverse("category_list")

        names = [
            'カテゴリ1',
            'カテゴリ2'
        ]

        for value in names:
            Category.objects.create(name=value, company=self.company)
    
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
        for key,value in enumerate(names):
            self.assertEqual(response.data[key]['name'], value)

        pass

    def test_retrieve(self):
        category = Category.objects.create(name="カテゴリ1", company=self.company)
        url = reverse("category_detail", kwargs={'pk': category.id})

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "カテゴリ1")

        pass

    def test_create(self):
        url = reverse("category_list")
        response = self.client.post(
            url, 
            {"name": "カテゴリ1", "company": self.company.id}, 
            format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "カテゴリ1")

        pass

    def test_update(self):
        category = Category.objects.create(name="カテゴリ1", company=self.company)
        url = reverse("category_detail", kwargs={'pk': category.id})

        response = self.client.put(
            url,
            {"name": "カテゴリ1 更新", "company": self.company.id},
            format="json"
        )

        self.assertEqual(response.status_code, 200)
        category.refresh_from_db()
        self.assertEqual(category.name, "カテゴリ1 更新")

        pass

    def test_destroy(self):
        category = Category.objects.create(name="カテゴリ1", company=self.company)
        url = reverse("category_detail", kwargs={'pk': category.id})

        response = self.client.delete(url, format="json")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 0)

        pass
