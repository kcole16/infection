from datetime import datetime
from db import db


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.now, required=True)
    infected = db.BooleanField(default=False)
    fake_infected = db.BooleanField(default=False)
    coaches = db.ListField(db.ReferenceField('User'))
    is_coached_by = db.ListField(db.ReferenceField('User'))
    test_case = db.BooleanField(default=False)
    cluster = db.ListField(db.ReferenceField('User'))

    meta = {
        'indexes': ['coaches', 'is_coached_by'],
        'ordering': ['-created_at']
    }

    def _infect_related(self):
        '''Recursively searches through users related to parent User.
        If User is infected, moves on. Else, calls infect'''

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


    def _fake_infect_related(self):
        '''Same as _infect_related, but with fake=True flag'''
        
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
        '''Starts infection with parent User'''

        if fake:
            self.fake_infected = True
            self.save()
            self._fake_infect_related()
        else:
            self.infected = True
            self.save()
            self._infect_related()





