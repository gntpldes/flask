from flask import render_template


def index(): 
    return "Welcome to the homepage"

def index_tem():
    return render_template('index.html', name=name, marks=marks)

def index_for():
    data={
        'science': 80, 
        'machine learning': 50, 
        'Udemy':75
        }


    return render_template('index_for.html', data=data)