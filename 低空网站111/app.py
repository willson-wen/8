from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

@app.route('/api/test')
def test():
    return {'message': 'API is working!'}

# Vercel 需要这个
application = app

if __name__ == '__main__':
    app.run() 