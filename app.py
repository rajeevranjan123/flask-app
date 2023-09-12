from flask import Flask

app = Flask(__name__)
print("i love docker images & container...")

@app.route('/')
def hello_world():
    return "welcome to G20!!!"

if __name__ == '__main__':
    print("calling webapp")
    app.run(host='0.0.0.0', debug=True)
else:
    print("i am in else...")
