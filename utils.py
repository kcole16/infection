from random import randint
from models import User


def total_infection():
    '''Infects all users'''

    users = User.objects.all()
    infection_count = len(users)

    for user in users:
        user.infected = True
        user.save()

    return infection_count

def disinfect(fake=False):
    '''Disinfects all users'''

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
    '''Returns list of coaches'''

    users = User.objects.all()
    coaches = [user for user in users if user.coaches != []]
    return coaches

def make_fake_relationships():
    '''Makes random mock relationships
    between users'''

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
            
def generate_fake_users(number, test_case=False):
    '''Creates fake users in db'''

    fake_users = []
    fake_user_count = 0
    
    while (fake_user_count < int(number)):
        if test_case:
            fake_user = User(test_case=True)
        else:
            fake_user = User()
        fake_user.save()
        fake_users.append(fake_user)
        fake_user_count += 1
        
    return fake_users

def start_infection(user_id, fake=False):
    '''Start infection with given user, 
    return total infection count'''

    user = User.objects.get(id=user_id)
    if fake:
        user.infect(fake=True)
    else:
        user.infect()
    number_infected = len(User.objects.filter(infected=True))
    return number_infected

def estimate_infection(user_id):
    '''Runs infect() with fake=True flag, 
    counts magnitude of infection, disinfects'''

    start_infection(user_id, fake=True)
    number_infected = len(User.objects.filter(fake_infected=True))
    disinfect(fake=True)
    return number_infected



