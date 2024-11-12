from flask import Flask, render_template, request
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure the API key for Google Generative AI
genai.configure(api_key="AIzaSyB8eaY5kLZdUawsSfEHRUXNorEYni0IJxg")
mymodel = genai.GenerativeModel("gemini-1.5-flash")
chat = mymodel.start_chat()

@app.route('/')
def home():
    return render_template("ai.html", messages=[])

@app.route('/send', methods=['POST'])
def send():
    uinput = request.form.get('user_input')  # Get user input
    response = chat.send_message(uinput)    # Send message to the model
    # Send user input and bot response back to the template
    return render_template('ai.html',
                           messages=[{'role': 'user', 'text': uinput},
                                     {'role': 'bot', 'text': response.text}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4546)
