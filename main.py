from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>Rotate by:
                <input type="text" name="rot" value="0"/>
            </label>
            <label>
                <textarea name="text"/></textarea>
            </label>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form


@app.route("/", methods=['POST'])
def encrypt():
    rot_number = request.form['rot']
    rot_text = request.form['text']
    rotatestring = "<h1>" + rotate_string(rot_text, int(rot_number)) + "</h1>"
    return rotatestring
    
app.run()
