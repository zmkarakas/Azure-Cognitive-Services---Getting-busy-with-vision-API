#Change variables according to your setup
import requests
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def describe_image(file_name):
    with open(file_name, 'rb') as image_file:
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': config['key1']
        }
        uri = config['endPoint'] + '/describe?maxCandidates=3'

        response = requests.post(uri, headers=headers, data=image_file)
        print(response.json())

def analyze_image(file_name):
    with open(file_name, 'rb') as image_file:
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': config['key1']
        }
        uri = config['endPoint'] + '/analyze?visualFeatures=Tags'

        response = requests.post(uri, headers=headers, data=image_file)
        print(response.json())

def read_image(file_path):
    with open(file_path, 'rb') as image_file:
        return image_file.read()

# Get a simple description   - Change the file names according to your photo name
describe_image('./Mert.jpg')

# Demo Mert.jpg with visual features "Tags"
analyze_image('./Mert.jpg')
