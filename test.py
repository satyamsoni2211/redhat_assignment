import json
import unittest
from util import get_hero_info, get_film_info, get_film_complete_info


class TestApiUtils(unittest.TestCase):

    def test_hero_info_object(self):
        '''
            Test case for validating the structure of the returned
            object
        '''
        data = get_hero_info(1)
        self.assertTrue('name' in data.keys())
        self.assertTrue('films' in data.keys())
        self.assertTrue('id' in data.keys())

    @unittest.expectedFailure
    def test_hero_info_invalid_id(self):
        '''
            Test case for validating the structure of the returned
            object
        '''
        data = get_hero_info(100)
        self.assertTrue('name' in data.keys())
        self.assertTrue('films' in data.keys())
        self.assertTrue('id' in data.keys())

    def test_get_film_info(self):
        '''
            checks for length of the returned object
        '''
        data = get_film_info(1)
        self.assertEqual(len(data), 2, 'Does not match the length')

    @unittest.expectedFailure
    def test_get_film_info_invalid_id(self):
        '''
            checks for length of the returned object
        '''
        data = get_film_info(100)
        self.assertEqual(len(data), 2, 'Does not match the length')

    def test_get_film_complete_info(self):
        '''
            checks for keys in film object
        '''
        data = get_film_complete_info(1)
        self.assertIn('title', data.keys(), 'data does not contain title')
        self.assertIn('characters', data.keys(),
                      'data does not contain characters')
        self.assertIn('planets', data.keys(), 'data does not contain planets')
        self.assertIn('starships', data.keys(),
                      'data does not contain starships')
        self.assertIn('vehicles', data.keys(),
                      'data does not contain vehicles')
        self.assertIn('species', data.keys(), 'data does not contain species')

    @unittest.expectedFailure
    def test_get_film_complete_info_invalid_id(self):
        '''
            expects error on invalid id
        '''
        data = get_film_complete_info(100)
        self.assertIn('title', data.keys(), 'data does not contain title')
        self.assertIn('characters', data.keys(),
                      'data does not contain characters')
        self.assertIn('planets', data.keys(), 'data does not contain planets')
        self.assertIn('starships', data.keys(),
                      'data does not contain starships')
        self.assertIn('vehicles', data.keys(),
                      'data does not contain vehicles')
        self.assertIn('species', data.keys(), 'data does not contain species')


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestApiUtils))
    runner.run(suite)
