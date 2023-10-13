from flask import Flask, request
import logging
import os

app = Flask(__name__)

app_log = logging.getLogger(__name__)
log_path = "LOGS"
os.makedirs(log_path, exist_ok=True)
file_name = "app.log"
log_file_path = os.path.join(log_path, file_name)

app_log.setLevel(logging.INFO)
formatter = logging.Formatter('[[%(asctime)s] [Function: %(funcName)s] [%(levelname)s] [Line: %(lineno)d]] :-> %(message)s')
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
app_log.addHandler(file_handler)

@app.route("/", methods = ['GET', 'POST'])
def index():
    app_log.info(f"{request.remote_addr} Hello Guys welcome back to my channel")
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port = 1010, host='0.0.0.0') 