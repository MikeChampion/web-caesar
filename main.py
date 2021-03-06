from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action='/' method='post'>
            <label for="user_input">
            Rotate by:
            <input type='text' name='rot' value='0'>
            <br>
            <textarea name='text'>
            {0}
            </textarea>
            <br>
            </input>
            <input type='submit' value='Submit'>
            <br>
        </form>
    </body>
</html>
"""

@app.route('/', methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    text=request.form['text']
    enc=rotate_string(text, rot)
    #final="<h1>" + enc + "</h1>"
    return form.format(enc)

@app.route('/')
def index():
    return form.format('')

app.run()