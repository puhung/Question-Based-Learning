from flask import Flask, request, jsonify
from langchain_main import generate_question

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    topic = data.get('topic')
    
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    
    question = generate_question(topic)
    return jsonify({"question": question})

if __name__ == '__main__':
    app.run(port=5000)