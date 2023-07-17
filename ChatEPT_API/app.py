from flask import Flask, request
from llama_index import StorageContext, load_index_from_storage
import openai
import os


application = Flask(__name__)

# openai.api_key = os.getenv("API_KEY")

openai.api_key = "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"

# DEBUG=True
# SECRET_KEY=your_secret_key


@application.route('/ask_question', methods=['POST'])
def process_text():
    text = request.form['question']

    storage_context = StorageContext.from_defaults(persist_dir='./chatEPT_Index/storage')
    loaded_index = load_index_from_storage(storage_context)
    result = loaded_index.as_query_engine().query(text)
    response_text = result.response.replace("\n", "")
    return response_text

if __name__ == '__main__':
    application.run()