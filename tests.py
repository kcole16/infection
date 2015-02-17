from flask import Flask, jsonify, request, render_template, redirect, Response
from flask.ext.mongoengine import MongoEngine

from utils import generate_fake_users
from models import User

import unittest
import os
import time

def disinfect(user):
	user.infected = False
	user.save()

def get_infection_count():
	infected_users = User.objects.filter(infected=True, test_case=True)
	infected_user_count = infected_users.count()
	map(lambda x: disinfect(x), infected_users)

	print infected_user_count
	
	return infected_user_count

class InfectionTest(unittest.TestCase):
	users = generate_fake_users(5, test_case=True)
	master_coach = users.pop()
	coach = users.pop()
	master_coach.coaches.append(coach)
	master_coach.save()
	coach.is_coached_by.append(master_coach)
	objects = [master_coach, coach]+users
	for user in users:
		user.is_coached_by.append(coach)
		user.save()
		coach.coaches.append(user)
		coach.save()

	# def _get_infection_count(self):
	# 	infected_users = User.objects.filter(infected=True, test_case=True)
	# 	infected_user_count = infected_users.count()
	# 	map(lambda x: self._disinfect(x), infected_users)
		
	# 	return infected_user_count

	def testInfection(self):
		expected_infection_count = (User.objects.filter(test_case=True).count()*5)
		infected_count = 0
		for obj in self.objects:
			obj.infect()
			time.sleep(5)
			infected_count += get_infection_count()
		User.objects.filter(test_case=True).delete()
		self.assertEqual(expected_infection_count, infected_count)


if __name__ == '__main__':
    unittest.main()







