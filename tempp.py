from flask import Flask

# Create the Flask application
app = Flask(__name__)


# Define a route and its handler
@app.route("/")
def hello():
    return "Hello, World it works!"


# Run the application
if __name__ == "__main__":
    app.run()
