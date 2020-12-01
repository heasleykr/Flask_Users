# !/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: Specifies CRUD Routes"""

from flask import request, render_template #allows interations with any requests. #renders our templates!
from app import app
from app.database import create, read, update, delete, scan
from app.forms.user import UserForm
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S") # verify server time. Used for users to verify if server is running
    tout = {}
    tout["ok"] = True
    tout["version"] = "1.0.0"
    tout["server_time"] = serv_time
    return render_template("index.html", out=tout)

@app.route("/user_form", methods=["GET", "POST"])
def user_form():
    if request.method == "POST":
        u_Fname = request.form.get("f_name")
        u_Lname = request.form.get("l_name")
        u_Hobby = request.form.get("hobby")

        create(u_Fname, u_Lname, u_Hobby)
        
    form = UserForm()

    return render_template("user_form.html", form=form)

@app.route("/users")
def get_all_users():
    out = scan() 
    out["ok"] = True
    out["message"] = "Success"
    # return out
    return render_template("users.html", users=out["body"])

@app.route("/users/<uid>")#uid is user id 
def get_one_user(uid):
    out = read(int(uid)) #read incomming user, format as an integer
    out["ok"] = True
    out["message"] = "Success"
    return out

#method to create a new user and add to db
#you can add multiple request methods as params if you need. Not recommended.
@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    new_id = create(
        user_data.get("first_name"), #find the key "name" and set value
        user_data.get("last_name"),
        user_data.get("hobby"),
    )
    #this is returned as a JSON first, then converted to a python dictionary
    return {"ok": True, "message": "Success", "new_id": new_id}

@app.route("/users/<uid>", methods=["PUT"])
def update_user(uid):
    user_data = request.json
    out = update(int(uid), user_data)
    return {"ok": out, "message": "Updated"}

