import unittest
from get_pet_labels import to_pet_label

class TestToPetLabel(unittest.TestCase):
    def test_removes_file_extension(self):
        result = to_pet_label('Boston_terrier_02259.jpg')
        self.assertNotIn('.jpg', result)

    def test_replaces_underscores_with_spaces(self):
        result = to_pet_label('Boston_terrier_02259.jpg')
        self.assertIn(' ', result)
        self.assertNotIn('_', result)

    def test_removes_numbers(self):
        result = to_pet_label('Boston_terrier_02259.jpg')
        self.assertNotIn('02259', result)

    def test_converts_to_lowercase(self):
        result = to_pet_label('Boston_terrier_02259.jpg')
        self.assertEqual(result, result.lower())

    def test_trims_extra_spaces(self):
        result = to_pet_label(' Boston_terrier_02259.jpg ')
        self.assertEqual(result, result.strip())
        
    def test_appropriate_output(self):
        result = to_pet_label('Boston_terrier_02259.jpg')
        self.assertEqual('boston terrier', result)

if __name__ == '__main__':
    unittest.main()