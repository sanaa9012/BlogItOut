from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/chatbot')
def about():
    return '<h1>Chatbot</h1>'    

@app.route('/health_camp')
def health():
    return '<h1>health_camp</h1>'    

@app.route('/patient_info')
def patient():
    return '<h1>patient_info</h1>'    

if __name__ == '__main__':
    app.run(debug=True)