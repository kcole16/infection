from datetime import datetime
from db import db


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.now, required=True)
    infected = db.BooleanField(default=False)
    fake_infected = db.BooleanField(default=False)
    coaches = db.ListField(db.ReferenceField('User'))
    is_coached_by = db.ListField(db.ReferenceField('User'))

    meta = {
        'indexes': ['coaches', 'is_coached_by'],
        'ordering': ['-created_at']
    }

    def infect_users(self):
        if self.coaches != None and self.is_coached_by != None:
            for user in self.coaches:
                if user.infected:
                    pass
                else:
                    user.infect()
            for user in self.is_coached_by:
                if user.infected:
                    pass
                else:
                    user.infect()
        elif self.coaches != None:
            for user in self.coaches:
                if user.infected:
                    pass
                else:
                    user.infect()
        elif self.is_coached_by != None:
            for user in self.is_coached_by:
                if user.infected:
                    pass
                else:
                    user.infect()
        else:
            print "Done"


    def fake_infect_users(self):
        if self.coaches != None and self.is_coached_by != None:
            for user in self.coaches:
                if user.fake_infected:
                    pass
                else:
                    user.infect(fake=True)
            for user in self.is_coached_by:
                if user.fake_infected:
                    pass
                else:
                    user.infect(fake=True)
        elif self.coaches != None:
            for user in self.coaches:
                if user.fake_infected:
                    pass
                else:
                    user.infect(fake=True)
        elif self.is_coached_by != None:
            for user in self.is_coached_by:
                if user.fake_infected:
                    pass
                else:
                    user.infect(fake=True)
        else:
            print "Done"

    def infect(self, fake=False):
        if fake:
            self.fake_infected = True
            self.save()
            self.fake_infect_users()
        else:
            self.infected = True
            self.save()
            self.infect_users()




