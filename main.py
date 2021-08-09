from flask import Flask
app = Flask(__name__)

@app.route('/')

def fun_name():

    return 'learning python'

if __name__=="__main__":
    app.run()
     
