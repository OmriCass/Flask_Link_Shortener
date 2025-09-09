from flask import render_template, request, redirect, abort
import string
import random

from models import Link

def register_routes(app, db):

    #this function will check the DB to see if the short link provided exists and redirect to the longer link otherwise it will return a 404 error
    @app.route('/<short_link>')
    def redirect(short_link):
        shorten = Link.query.filter_by(short=short_link).first()

        if shorten :
            return redirect(shorten.long)
        else:
            return abort(404)
        
    #This is the function to randomly generate a 5 character short link using digits and letters    
    def generate_short_code(length=5):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
    
    @app.route('/shorten', methods=['POST', 'GET'])
    def shorten():

        short_url = None

        if request.method == "POST":
            long_url = request.form.get("url")

            # because we are using a limited amount of characters in random to generate the link we need to kep generating links until we have a unique one
            while True:
                short_code = generate_short_code()
                #check if the generated short_code is unique, if so break out of the loop
                if not Link.query.filter_by(short=short_code).first():
                    break


        new_Link = Link(short=short_code, long=long_url)
        db.session.add(new_Link)
        db.session.commit()

        short_url = request.host_url + short_code

        return render_template("index.html", short_url=short_url)
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template("index.html")
        