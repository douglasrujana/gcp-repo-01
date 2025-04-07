from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo v1'

# if __name__ == '__main__':
#    app.run(debug=True)



