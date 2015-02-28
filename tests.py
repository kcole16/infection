from flask import Flask, jsonify, request, render_template, redirect, Response
from flask.ext.mongoengine import MongoEngine

from utils import generate_fake_users, build_clusters, build_limited_infection
from models import User

import unittest
import os
import time

def setUp():
	''' Creates Users with multiple coaching/is_coached_by 
	relationships to test with'''

	users = generate_fake_users(5, test_case=True)
	master_coach = users.pop()
	coach = users.pop()
	master_coach.coaches.append(coach)
	master_coach.save()
	coach.is_coached_by.append(master_coach)
	for user in users:
		user.is_coached_by.append(coach)
		user.save()
		coach.coaches.append(user)
		coach.save()
	build_clusters(test_case=True)
	return master_coach, coach, users

def tearDown():
	'''Deletes test_case Users'''

	User.objects.filter(test_case=True).delete()

def test_infection(user, fake=False):
	'''Runs infect() on a given users, compares effects to test_case count.
	All users are expected to receive infection'''

	expected_infection_count = User.objects.filter(test_case=True).count()
	if fake:
		user.infect(fake=True)
		infected_count = User.objects.filter(test_case=True, fake_infected=True).count()
	else:
		user.infect()
		infected_count = User.objects.filter(test_case=True, infected=True).count()
	tearDown()
	return expected_infection_count, infected_count


class InfectionTest(unittest.TestCase):

	def testMasterCoachInfection(self):
		'''Tests infection starting with User 
		with only coaches relationships'''

		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(master_coach)
		self.assertEqual(expected_infection_count, infected_count)

	def testCoachInfection(self):
		'''Tests User with both coaches and is_coached_by relationships'''

		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(coach)
		self.assertEqual(expected_infection_count, infected_count)

	def testUserInfection(self):
		'''Tests one of users with only is_coached_by relationships'''

		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(users[1])
		self.assertEqual(expected_infection_count, infected_count)

	def testFakeMasterCoachInfection(self):
		'''Tests fake_infect() method'''
		
		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(master_coach, fake=True)
		self.assertEqual(expected_infection_count, infected_count)

	def testFakeCoachInfection(self):
		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(coach, fake=True)
		self.assertEqual(expected_infection_count, infected_count)

	def testFakeUserInfection(self):
		master_coach, coach, users = setUp()
		expected_infection_count, infected_count = test_infection(users[1], fake=True)
		self.assertEqual(expected_infection_count, infected_count)

	def testBuildLimitedInfectionLess(self):
		'''Tests limited infection with < number of users'''

		master_coach, coach, users = setUp()
		infected_count = len(build_limited_infection(3))
		expected_infection_count = User.objects.filter(test_case=True).count()
		tearDown()
		self.assertEqual(expected_infection_count, infected_count)

	def testBuildLimitedInfectionMore(self):
		'''Tests limited infection with > number of users'''
		
		master_coach, coach, users = setUp()
		infected_count = len(build_limited_infection(7))
		expected_infection_count = User.objects.filter(test_case=True).count()
		tearDown()
		self.assertEqual(expected_infection_count, infected_count)


if __name__ == '__main__':
    unittest.main()

