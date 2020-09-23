import unittest
from app.models import Pitch, User
from app import db


class TestReview(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''
    def setUp(self):
        self.user_James = User(username='James',
                               password='potato',
                               email='james@ms.com')
        self.new_pitch = Pitch(pitch='An openning forum for youths',
                               user=self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch, 'An opening forum for youths')
        self.assertEquals(self.new_pitch.user, self.user_James)

    def test_save_review(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_review_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_all_piches()
        self.assertTrue(len(got_pitches) == 1)