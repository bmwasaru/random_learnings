import unittest

from parse_csv import read_data


class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'County_Center_Populations.csv'

    def test_csv_read_data_headers(self):
        self.assertEqual(
            read_data(self.data)[0],
                ['County','% Rural','% Urban','Rural','Urban','Total','Location 1']
        )

    def test_csv_read_data_county_name(self):
        self.assertEqual(read_data(self.data)[1][0], 'Baringo')

    def test_csv_read_data_total_population(self):
        self.assertEqual(read_data(self.data)[1][5], '555561')

if __name__ == '__main__':
    unittest.main()
