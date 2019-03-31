import os
from flask import url_for
from run import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):# app initialize
        self.app = app.test_client()
        self.app.application.config['SECRET_KEY'] = ']Nk(`K24HLRuRkdN'
        self.app.application.config['SESSION_COOKIE_DOMAIN'] = None
        self.app.application.config["SERVER_NAME"] = "{0} {1}".format(os.environ.get('PORT'), os.environ.get('IP'))
    

    def test_initial(self):# check if index.html has been created
        with app.app_context():
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)


    def test_show_all(self):# check if show_all.html has been created
        with app.app_context():
            response = self.app.get('/show_all')
            self.assertEqual(response.status_code, 200)


    def test_show_single(self):# check if show_single.html has been created
        with app.app_context():
            response = self.app.get('/show_single/5c6b439899e7e318893a9373')
            self.assertEqual(response.status_code, 200)


    def test_vote_logic(self):
        voted_down = "bob"
        voted_up = "frank"
        downvotes =  3
        upvotes =  4
        user = "frank"
        voted_down = str(voted_down)
        voted_up = str(voted_up)
        if user in voted_down:  
            self.assertNotEqual(voted_up, "")
        elif user in voted_up:
            downvotes = int(downvotes)
            downvotes = downvotes + 1
            downvotes = str(downvotes)
            voted_down = voted_down + user
            upvotes = int(upvotes)
            upvotes = upvotes - 1
            upvotes = str(upvotes)
            voted_up = voted_up.replace('frank', '')
            self.assertEqual(voted_up, "")

        else:
            downvotes = int(downvotes)
            downvotes = downvotes + 1
            downvotes = str(downvotes)
            voted_down = voted_down + user
            self.assertNotEqual(voted_up, "")


if __name__ == '__main__':
    
    unittest.main()