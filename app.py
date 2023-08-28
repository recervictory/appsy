from flask import Flask, jsonify, request

app = Flask(__name__)

visitor_count = 0  # Initialize the visitor count

@app.route('/count_visitor', methods=['GET', 'POST'])
def count_visitor():
    global visitor_count  # Access the global visitor_count variable

    if request.method == 'GET':
        return jsonify({"visitor_count": visitor_count})
    elif request.method == 'POST':
        visitor_count += 1
        return jsonify({"visitor_count": visitor_count})

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

