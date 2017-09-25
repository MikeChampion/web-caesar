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
        <form action='/' method = 'POST'>
            
            Rotate by:
            <input type='text' name='rot' value='0'>
            <p>
            <textarea name='text'>
            </textarea>
            <p>
            <input type='submit' value='Submit'>
            <br>
        </form>
    </body>
</html>
"""

@app.route('/', methods=['POST'])
def index():
    return form

def encrypt():
    rot=int(request.form['rot'])
    text=request.form['text']
    rotate_string(rot, text)
    #return """<h1>rotate_string()</h1>"""

app.run()