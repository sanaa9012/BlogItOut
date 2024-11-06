from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Sai Kiran',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 26, 2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html' , posts=posts)

@app.route('/chatbot')
def chat():
    return render_template('chatbot.html')    

@app.route('/health_camp')
def health():
    return render_template('health_camp.html')    

@app.route('/patient_info')
def patient():
    return render_template('patient_info.html')    

if __name__ == '__main__':
    app.run(debug=True)