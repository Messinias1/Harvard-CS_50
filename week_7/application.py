import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("Name") or not request.form.get("Faction") or not request.form.get("Role"):
        return render_template("error.html", message="Please fill in all fields before submission!!")

    with open('survey.csv', 'w') as f:
        fieldnames = ['Name', 'Faction', 'Role']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        thewriter.writeheader()
        thewriter.writerow({'Name' : 'Bill', 'Faction' : 'NCR', 'Role' : 'Sniper'})
        thewriter.writerow({'Name' :  request.form.get("Name"), 'Faction' :  request.form.get("Faction"), 'Role' :  request.form.get("Role")})

    return redirect("/sheet")
    # return render_template("error.html", message="TODO")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open('survey.csv') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        # line_count = 0
        # for row in reader:
        #     if line_count == 0:
        #         print(f'{", ".join(row)}')
        #         line_count += 1
        #     print(f'{row["Name"]}  {row["Faction"]}  {row["Role"]}.')
        #     line_count += 1
        # print(f'Processed {line_count} lines.')

    return render_template("sheet.html", data = data)
