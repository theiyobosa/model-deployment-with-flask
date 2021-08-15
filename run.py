from flask_wrapper.server import *
from webbrowser import open

if __name__ == '__main__':
    open('http://localhost:5000')
    app.run(debug=True)