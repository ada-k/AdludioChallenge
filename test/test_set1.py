try:
    import sys, os
    sys.path.append(os.path.abspath(os.path.join('..')))

    import unittest
    import numpy as np
    from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
    from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
    from app import app
    from app.lib import recommender_data
    from app.lib.recommender_data import calculate_score, calculate_rates

except Exception:
    print('some modules missing.')


class FlaskTests(unittest.TestCase):

    self.arr1 = np.ones((2,2))
    self.arr2 = np.full((2,2), 6)

    def test_basic_test(self):
        out = {}
        assert_equal(isinstance(out, dict), True)
    
    # calculate_score test - return type
    def test_calculate_score(self):
        val = int(calculate_score(self.arr2))
        self.assert_equal(isinstance(val, int), True)


    # calculate_rates test - return type
    def test_calculates_rates(self):
        self.assert_equal(isinstance(calculate_rates(self.arr1, self.arr2), np.ndarray), True)


    # route test (check status code)
    def test_homepage(self):
	test = app.test_client(self)
	response = test.get('/demo1')
	self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
