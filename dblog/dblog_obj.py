from dblog.models import *

class DBlog:
    def __init__(self):

        self.name = 'dfsdf'
        self.tagline = ''
        self.domain = ''
        self.ga_id = ''

        self.set_vars()

    def set_vars(self):
        q = dblog_Settings.objects.all()
        if q:
            obj = q[0]
            self.name = obj.name
            self.tagline = obj.tagline
            self.domain = obj.domain
            self.ga_id = obj.ga_id 