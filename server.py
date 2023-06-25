from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}! Form submitted successfully.'
    return render_template('form.html')

if __name__ == '__main__':
    app.debug = True

    app.run()



   