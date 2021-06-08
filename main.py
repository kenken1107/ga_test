from flask import Flask
from routes.so_what.api_so_what import so_what

app = Flask(__name__)
app.register_blueprint(so_what)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False, 
    threaded=False)