from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/applicants")
def applicants_list():
    return render_template(
        "applicants-list.html", applicants=data_manager.get_all_applicants()
    )


@app.route("/applicants-phone", methods=["post"])
def applicants_phone():
    if request.form.get("applicant-name"):
        applicant_name = request.form.get("applicant-name")
        applicants = data_manager.get_applicant_data_by_name(applicant_name)
    elif request.form.get("applicant-email"):
        email = request.form.get("applicant-email")
        applicants = data_manager.get_applicant_data_by_email_ending(email)
    return render_template("applicants-phone.html", applicants=applicants)


@app.route("/mentors")
def mentors_list():
    mentor_name = request.args.get("mentor-last-name")
    city = request.args.get("city")

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template("mentors.html", mentors=mentor_details)


if __name__ == "__main__":
    app.run()
