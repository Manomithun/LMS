import frappe
from frappe.tests.utils import FrappeTestCase

class TestArticle(FrappeTestCase):
    def test_article_creation(self):
        article = frappe.doc({
            "doctype" : "Article",
            "title" : "My Frist Test",
            "status" : "Published"
        })
        article.insert()

        article.assertEqual(article.title, "My First Test")
        article.assertTrue(frappe.db.exists("Article",article.name))