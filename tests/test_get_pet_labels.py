import unittest
from get_pet_labels import get_pet_labels
from os import listdir

class TestGetPetLabels(unittest.TestCase):
    def setUp(self):
        self.image_dir = "pet_images"

    def test_returns_dictionary(self):
        result = get_pet_labels(self.image_dir)
        self.assertIsInstance(result, dict)

    def test_dictionary_keys_are_filenames(self):
        result = get_pet_labels(self.image_dir)
        expected_keys = listdir(self.image_dir)
        self.assertListEqual(list(result.keys()), expected_keys)
        
    def test_dictionary_values_are_lists(self):
        result = get_pet_labels(self.image_dir)
        for value in result.values():
            self.assertIsInstance(value, list)
            
    def test_dictionary_values_are_pet_labels(self):
        result = get_pet_labels(self.image_dir)
        for value in result.values():
            self.assertIsInstance(value[0], str)

    def test_no_duplicate_filenames(self):
        get_pet_labels(self.image_dir)
        

if __name__ == '__main__':
    unittest.main()