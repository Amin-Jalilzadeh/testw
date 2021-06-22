from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__)
# print(app)


# pip3 install Flask


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data ["email"]
        subject = data ["subject"]
        message = data ["message"]
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode = 'a') as database2:
        email = data ["email"]
        subject = data ["subject"]
        message = data ["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something is wrong'
        # return redirect('/thankyou.html')

# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
# @app.route("/contact.html")
# def works():
#     return render_template("contact.html")











# py -3 -m venv venv
# venv\Scripts\activate
# python server.py
# set FLASK_APP=server.py
# flask run

# set FLASK_ENV=development



#############
# git clone https://github.com/Amin-Jalilzadeh/resume.git

