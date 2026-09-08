import frappe
from frappe.tests.utils import FrappeTestCase
from library_management.library.doctype import article
class TestArticle(FrappeTestCase):
    def test_article_creation(self):
        article = frappe.get_doc({
            "doctype" : "article",
            "title" : "My Frist Test",
            "status" : "Published"
        })
        article.insert()

        self.assertEqual(article.title, "My Frist Test")
        self.assertTrue(frappe.db.exists("article",article.name))