# Copyright (c) 2026, mano and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json
import os



class ExternalBooks(Document):

	path = frappe.get_app_path(
		"library_management",
		"library",
		"data",
		"book.json"
	)

	@staticmethod
	def get_current_data():
		if not os.path.exists(ExternalBooks.path) :
			return {}

		with open(ExternalBooks.path) as f:
			return json.load(f)
	
	def db_insert(self, *args, **kwargs):
		data = ExternalBooks.get_current_data()

		data[self.name] = {
			"name" : self.name,
			"title" : self.title,
			"author":self.author,
			"price": self.price
		}

		with open(ExternalBooks.path, "w") as f:
			json.dump(data, f , indent=4)

	def load_from_db(self, *args, **kwargs):
		data = ExternalBooks.get_current_data()
		book = data.get(self.name)

		if not book:
			frappe.throw(f"Book {self.name} is not found")
		super(Document,self).__init__(book)


	def db_update(self, *args, **kwargs):
		raise NotImplementedError

	def delete(self, *args, **kwargs):
		raise NotImplementedError

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		data = ExternalBooks.get_current_data()

		return [
			frappe._dict(book) 
			for book in data.values()
		]

	@staticmethod
	def get_count(filters=None, **kwargs):
		data = ExternalBooks.get_current_data()
		return len(data)

	@staticmethod
	def get_stats(**kwargs):
		pass

