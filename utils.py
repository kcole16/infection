from random import randint
from models import User


def total_infection():
    users = User.objects.all()
    infection_count = len(users)

    for user in users:
        user.infected = True
        user.save()

    return infection_count

def disinfect(fake=False):
    users = User.objects.all()
    disinfect_count = len(users)

    for user in users:
        if fake:
            user.fake_infected = False
        else:
            user.infected = False
        user.save()

    return disinfect_count

def get_coaches():
    users = User.objects.all()
    coaches = [user for user in users if user.coaches != []]
    return coaches

def make_fake_relationships():
    users = User.objects.all()
    user_count = len(users)
    num_coaches = randint(1,user_count/5)
    coaches = users[:num_coaches]
    students = users[num_coaches:]
    students_per_coach = len(students)/len(coaches)
    students_left = len(students)
    for coach in coaches:
        count = 0
        while count < students_per_coach:
            student = students[students_left-1]
            coach.coaches.append(student)
            coach.save()
            student.is_coached_by.append(coach)
            student.save()
            students_left -= 1
            count += 1
    print "Done"

def generate_fake_users(number):
    fake_user_count = 0
    while (fake_user_count < int(number)):
        fake_user = User()
        fake_user.save()
        fake_user_count += 1
    return fake_user_count

def estimate_infection(user_id):
    user = User.objects.get(id=user_id)
    fake_infection(user)
    number_infected = len(User.objects.filter(fake_infected=True))
    disinfect(fake=True)
    return number_infected

def fake_infection(user):
    user.infect(fake=True)

def start_infection(user_id):
    user = User.objects.get(id=user_id)
    user.infect()
    number_infected = len(User.objects.filter(infected=True))
    return number_infected

# def infect(user, fake=False):
#     if fake:
#         user.fake_infected = True
#         user.save()
#         if user.coaches != None and user.is_coached_by != None:
#             for user in user.coaches:
#                 if user.fake_infected:
#                     pass
#                 else:
#                     infect(user, fake)
#             for user in user.is_coached_by:
#                 if user.fake_infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         elif user.coaches != None:
#             for user in user.coaches:
#                 if user.fake_infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         elif user.is_coached_by != None:
#             for user in user.is_coached_by:
#                 if user.fake_infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         else:
#             print "Done"
#     else:
#         user.infected = True
#         user.save()
#         if user.coaches != None and user.is_coached_by != None:
#             for user in user.coaches:
#                 if user.infected:
#                     pass
#                 else:
#                     infect(user, fake)
#             for user in user.is_coached_by:
#                 if user.infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         elif user.coaches != None:
#             for user in user.coaches:
#                 if user.infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         elif user.is_coached_by != None:
#             for user in user.is_coached_by:
#                 if user.infected:
#                     pass
#                 else:
#                     infect(user, fake)
#         else:
#             print "Done"










