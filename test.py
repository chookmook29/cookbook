import os
from flask import url_for
from run import app
import unittest

class FlaskTestCase(unittest.TestCase):

	def setUp(self):#App initialize
		self.app = app.test_client()
		self.app.application.config['SECRET_KEY'] = ']Nk(`K24HLRuRkdN'
		self.app.application.config['SESSION_COOKIE_DOMAIN'] = None
		self.app.application.config["SERVER_NAME"] = "{0} {1}".format(os.environ.get('PORT'), os.environ.get('IP'))
	
	def test_initial(self):#Check if index.html has been created
		with app.app_context():
			response = self.app.get('/')
			self.assertEqual(response.status_code, 200)

	def test_show_all(self):#Check if show_all.html has been created
		with app.app_context():
			response = self.app.get('/show_all')
			self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	
	unittest.main()