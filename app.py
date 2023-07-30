from flask import Flask, request
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    #temporarily this will just print email instead of send the form data to my email
    print(f'Name: {name}, Email: {email}, Message: {message}')

    return 'Form submitted Successfully!'

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)