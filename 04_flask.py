from flask import Flask 

my_app = Flask (__name__)

@my_app.route('/')
def root():
    return "Default page"

@my_app.route('/exciting')
def excite():
    return "This page is exciting"

@my_app.route('/boring')
def bore():
    return "This page is boring"

@my_app.route('/indecisive')
def idk():
    return "This page is questionable"

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
