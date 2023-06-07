import unittest
from unittest.mock import patch, MagicMock
import tempfile
import os
import numpy as np
from my_module import zillow_train_model
from my_module import tennis_train_model
from my_module import flowers_train_model
from flower_inference import generate_flower_inference
from tennis_inference import generate_tennis_inference
from zillow_inference import generate_zillow_inference

class TestFlowersTrainModel(unittest.TestCase):
    
    
    def setUpClass(cls):
        cls.epochs = 10
        cls.image_target_size = (180, 180)
        cls.validation_split = 0.2
        
    def test_image_count(self):
        with patch('tensorflow.keras.utils.get_file') as mock_get_file:
            mock_get_file.return_value = os.path.join(tempfile.gettempdir(), 'flower_photos')
            from flowers_train_model import flowers_train_model
            flowers_train_model(self.epochs, self.image_target_size, self.validation_split)
            mock_get_file.assert_called_once_with('flower_photos', origin='https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz', untar=True)
        
        with patch('pathlib.Path.glob') as mock_glob:
            mock_glob.return_value = ['image1.jpg', 'image2.jpg', 'image3.jpg']
            from flowers_train_model import flowers_train_model
            self.assertEqual(flowers_train_model(self.epochs, self.image_target_size, self.validation_split), 3)
            mock_glob.assert_called_once_with('*/*.jpg')
    
    def test_image_datasets(self):
        mock_train_ds = MagicMock()
        mock_val_ds = MagicMock()
        with patch('tensorflow.keras.utils.image_dataset_from_directory') as mock_image_dataset_from_directory:
            mock_image_dataset_from_directory.side_effect = [mock_train_ds, mock_val_ds]
            from flowers_train_model import flowers_train_model
            self.assertEqual(flowers_train_model(self.epochs, self.image_target_size, self.validation_split), (mock_train_ds, mock_val_ds))
            mock_image_dataset_from_directory.assert_any_call(mock.ANY, validation_split=self.validation_split, subset="training", seed=123, image_size=self.image_target_size, batch_size=32)
            mock_image_dataset_from_directory.assert_any_call(mock.ANY, validation_split=self.validation_split, subset="validation", seed=123, image_size=self.image_target_size, batch_size=32)
    
    def test_model_training(self):
        mock_history = MagicMock()
        with patch('tensorflow.keras.models.Sequential.fit') as mock_fit:
            mock_fit.return_value = mock_history
            from flowers_train_model import flowers_train_model
            _, _ = flowers_train_model(self.epochs, self.image_target_size, self.validation_split)
            mock_fit.assert_called_once_with(mock.ANY, validation_data=mock.ANY, epochs=self.epochs)
class TestTennisTrainModel(unittest.TestCase):
    
    @patch('my_module.tf.keras.utils.image_dataset_from_directory')
    @patch('my_module.Sequential')
    def test_tennis_train_model(self, mock_model, mock_dataset):
        mock_dataset.return_value = tf.data.Dataset.from_tensor_slices(([1]*10, [2]*10))
        mock_model.return_value = mock_model
        mock_model.fit.return_value = None
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            tennis_train_model(epochs=2, image_taget_size=(360, 360), validation_split=0.2, save_dir=tmp_dir)
            self.assertTrue(mock_model.compile.called)
            self.assertTrue(mock_model.fit.called)

class TestZillowTrainModel(unittest.TestCase):

    def setUp(self):
        self.epochs = 5
        self.image_target_size = (224, 224)
        self.validation_split = 0.2

    def test_zillow_train_model(self):
        # Call the function
        zillow_train_model(self.epochs, self.image_target_size, self.validation_split)
        
        # Assert that the saved model file exists
        self.assertTrue(os.path.exists("/Users/michaelmills/Saved_Models/zillow_model"))
        
class TestFlowerInference(unittest.TestCase):

    def setUp(self):
        self.model = tf.keras.models.load_model('/path/to/model')
        self.class_names = ["Daisy", "Dandelion", "Rose", "Sunflower", "Tulip"]

    def test_generate_flower_inference(self):
        result = generate_flower_inference(self.model, self.class_names)
        self.assertTrue(isinstance(result, str))
        
class TestTennisInference(unittest.TestCase):

    @patch('tensorflow.keras.utils.load_img')
    def test_generate_tennis_inference(self, mock_load_img):
        # Mock the load_img function
        mock_img = tf.ones([360, 360, 3])
        mock_load_img.return_value = mock_img

        # Define test data
        model = tf.keras.Sequential([tf.keras.layers.Dense(2, activation='softmax')])
        class_names = ["Agassi", "Federer"]
        expected_output = "This image most likely belongs to Agassi with a 80.00 percent confidence."

        # Generate inference
        with patch('builtins.print') as mock_print:
            generate_tennis_inference(model, class_names)

            # Check that the print statement contains the expected output
            mock_print.assert_called_with(expected_output)
            
class TestGenerateZillowInference(unittest.TestCase):

    @patch('my_module.load_model')
    @patch('my_module.pd.read_csv')
    @patch('my_module.requests.get')
    @patch('my_module.Image.open')
    def test_generate_zillow_inference(self, mock_open, mock_requests, mock_read_csv, mock_load_model):
        
        # Create mock objects to return from patched functions
        mock_model = MagicMock()
        mock_model.predict.return_value = np.array([0.1, 0.2, 0.3])
        mock_load_model.return_value = mock_model
        
        mock_csv_data = 'photo_url,price,beds,baths,sqft,doz,zpid\nhttp://test.com,100000,2,1,1000,0,1234'
        mock_csv = MagicMock()
        mock_csv.__iter__.return_value = mock_csv_data.splitlines().__iter__()
        mock_read_csv.return_value = mock_csv
        
        mock_img = MagicMock()
        mock_img.resize.return_value = mock_img
        mock_img_array = np.zeros((360, 360, 3), dtype=np.uint8)
        mock_img_array = np.expand_dims(mock_img_array, axis=0)
        mock_img_array = np.concatenate([mock_img_array, mock_img_array], axis=0)
        mock_img_array = np.concatenate([mock_img_array, mock_img_array], axis=0)
        mock_open.return_value = mock_img
        
        mock_response = MagicMock()
        mock_response.content = b'mock content'
        mock_requests.return_value = mock_response

        # Call the function
        generate_zillow_inference()
        
        # Check that the expected functions were called
        mock_load_model.assert_called_once_with('/Users/michaelmills/Saved_Models/zillow_model')
        mock_read_csv.assert_called_once_with('/Users/michaelmills/Zillow_Dataset/mini-zillow.csv', names=['photo_url', 'price', 'beds', 'baths', 'sqft', 'doz', 'zpid'])
        mock_requests.assert_called_once_with('http://test.com')
        mock_open.assert_called_once_with(mock_response.content)
        mock_model.predict.assert_called_once_with([mock_img_array, np.array([[2, 1, 1000, 0]])])

class TestGetListings(unittest.TestCase):

    def test_get_Xb_Xb_sort_X_doz_X(self):

        with patch('requests.get') as mock_get:
            mock_response = Response()
            mock_response.status_code = 200
            mock_response._content = b'{"totalResultCount": 1, "results": [{"imgSrc": "http://imageurl.com/image.jpeg", "price": "1500", "bathrooms": "2.0", "bedrooms": "2.0", "livingArea": "1000", "daysOnZillow": "14", "zpid": "123456"}]}'
            mock_get.return_value = mock_response

            num_page_results, listings_per_page, max_results, no_results, num_results, total_results, results_per_page, days_on_zillow_list , current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list = define_variables_and_lists()

            bed_input = 2
            bath_input = 2
            sort = "priorityScore"
            doz = 1
            num_page_results, listings_per_page, max_results, no_results, num_results, total_results, results_per_page, days_on_zillow_list , current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list = get_Xb_Xb_sort_X_doz_X(num_page_results, listings_per_page, max_results, no_results, num_results, results_per_page, days_on_zillow_list , current_page, photo_urls, listing_prices, bathrooms, bedrooms, living_areas, days_on_zillow, zpids, total_results, bed_input, bath_input, sort, doz, bathrooms_list, bedrooms_list)

            self.assertEqual(num_results, 1)
            self.assertEqual(listing_prices, [1500])
            self.assertEqual(bathrooms_list, [2])
            self.assertEqual(bedrooms_list, [2])
            self.assertEqual(living_areas, [1000])
            self.assertEqual(zpids, [123456])
            self.assertEqual(photo_urls, ["http://imageurl.com/image.jpeg"])
            self.assertEqual(days_on_zillow_list, [14])

    
if __name__ == '__main__':
    unittest.main()
    

