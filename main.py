from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask (__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #0d7673;
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
    <form action= "/" method= "POST">
        <label>Rotate by: <input name="rot" type="text" value=0 /></label>
        <textarea name="text" >{0}</textarea>
        <input type="submit"/>
    </form>
    </body>
</html>
"""    


@app.route("/")
def index():
    return form.format('')

def is_integer(rot):
    try:
        int(rot)
        return True
    except ValueError:
        return False


@app.route("/", methods = ['POST', 'GET'])
def encrypt():
    if not is_integer(request.form['rot']):
        encrypt = "Not a valid integer"
        
        
    else:
        rot=int(request.form['rot'])
        text=cgi.escape(request.form['text'])
        encrypt=rotate_string(text,rot)
    
    return form.format(encrypt)

app.run()