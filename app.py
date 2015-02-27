#!flask/bin/python
from flask import Flask, jsonify, request, render_template, redirect, Response
from flask.ext.mongoengine import MongoEngine

import utils
from models import User

import json
from werkzeug.routing import BaseConverter


app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.route('/', methods=['GET', 'POST'])
def coaches():
    users = User.objects.all()
    num_infected = User.objects.filter(infected=True).count()
    coaches = [user for user in users if user.coaches != []]
    
    return render_template('coaches.html', coaches=coaches, num_infected=num_infected)

@app.route('/coach/<regex(".+"):coach_id>/', methods=['GET', 'POST'])
def students(coach_id):
    coach = User.objects.get(id=coach_id)
    coaches = []
    students = User.objects.all()
    students = [student for student in students if coach in student.is_coached_by]

    return render_template('students.html', students=students, coach=coach)

@app.route('/make_fake_relationships/', methods=['GET'])
def make_fake_relationships():
    utils.make_fake_relationships()
    return jsonify(done=True)

@app.route('/estimate_infection/', methods=['GET'])
def estimate_infection():
    user = request.args['user']
    number_infected = utils.estimate_infection(user)
    infected = utils.build_limited_infection(53)
    return jsonify(infected=number_infected)

@app.route('/start_infection/', methods=['GET'])
def start_infection():
    user = request.args['user']
    number_infected = utils.start_infection(user)
    return jsonify(total_infected=number_infected)

@app.route('/total_infection/', methods=['GET'])
def total_infection():
    number = utils.total_infection()
    return jsonify(infected=number)

@app.route('/disinfect/', methods=['GET'])
def disinfect():
    number = utils.disinfect()
    return jsonify(infected=number)

@app.route('/clear_users/', methods=['GET'])
def clear_users():
    users = User.objects.all()
    for user in users:
        user.delete()
    return jsonify(users="deleted")

@app.route('/create_fake_users/', methods=['GET'])
def create_fake_users():
    fake_user_count = len(utils.generate_fake_users(100))
    utils.make_fake_relationships()
    utils.build_clusters()

    return jsonify(fake_users=fake_user_count)


"""Run server"""
if __name__ == '__main__':
    app.run(debug = True)
