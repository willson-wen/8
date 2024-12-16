from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/test')
def test():
    return jsonify({'message': 'API is working!'})

# Vercel 需要这个
application = app

if __name__ == '__main__':
    app.run()
