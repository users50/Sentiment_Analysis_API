# Sentiment_Analysis_API
Sentiment Analysis API using FastAPI and HuggingFace Transformers
This repository contains a FastAPI application that uses a pre-trained model from HuggingFace's model hub to perform sentiment analysis on text provided by the user, sentence by sentence.

Installation and Setup
Clone this repository to your local machine.
git clone <repo-link>
Enter the directory of the cloned repository.
cd <repo-name>
It's recommended to set up a virtual environment to isolate the project's dependencies. You can do this using the following commands:
python3 -m venv env
source env/bin/activate
Install the project dependencies:
pip install -r requirements.txt
Running the Application
To start the server, execute the following from the command line:
uvicorn main:app --reload    
The API will now be live at http://localhost:8000.

API Usage
The API accepts a .txt file containing the text that you want to analyze for sentiment. The text is split into sentences, and the sentiment of each sentence is evaluated separately.

To use this API, send a POST request to the /analyze_sentiments/ endpoint using your preferred API testing tool such as cURL or Postman.

The POST request should contain a single parameter file which is the text file to be processed. The text file should be included in the body of the request as form-data.

The response from the API is a JSON object where the key sentiments contains a list of the sentiment analysis results for each sentence in the text.

Example Response

{
  "sentiments": ["positive", "negative", "positive", ...]
}
Each string in the sentiments list represents the sentiment of the corresponding sentence in the text (in order). The sentiment can be "positive", "negative", or "neutral".

License
This project is released under the MIT License.
