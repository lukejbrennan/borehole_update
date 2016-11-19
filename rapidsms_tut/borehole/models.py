from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible

############################################
#                                          #   
#  Remember to run                         #
#                                          #
#   $ python manage.py makemigrations      #
#   $ python manage.py migrate             #
#                                          #
# after making changes to this doc         #
#                                          #
############################################

class Status(models.Model):
    #Unique to each borehole. Value taken from "messagelog_message" column: contact_id
    borehole_id = models.IntegerField()
    
    #Functioning (222), Partially Functioning (111), Not Functioning (000) 
    # value taken from message text
    status      = models.CharField(max_length=30)

    datetime= models.DateTimeField()    
    
    #Value taken from survey only if message text was 111 or 000:
    #(Not Funct. or Partially Funct.)
    description = models.CharField(max_length=30, default='N/A')
    def __str__(self):
        return "Borehole %i Status: %s" %( self.borehole_id, self.status)

class Borehole(models.Model):
    #One one mapping with borehole_id from Status
    borehole_ID = models.IntegerField() 
    name = models.CharField(max_length=30, default='None')    
    current_status = models.CharField(max_length=30, default='None')
    # Must be assigned on the website. Might be useful to store automatically
    # See Procedure with Unicef documentation
    contact_number = models.CharField(max_length=30, default='None')
    # Assigned on website.
    lat = models.FloatField(_('Latitude'), blank=True, null=True)  
    lon = models.FloatField(_('Longitude'), blank=True, null=True)   
    status_time = models.DateTimeField(default=None)
    def __str__(self):
        return "Borehole %i" % (self.borehole_ID)

class Dict(models.Model):
    name      = models.CharField(max_length=50)

    @staticmethod    
    def getDict(name):
        #Returns Dict of the given name.
        df= Dict.objects.select_related().get(name=name)
        return df

#   def statuscode_set??

    def __getitem__(self, code):    
        #Returns status when for a particular code
        return self.statuscode_set.get(code=code).status

    def __len__(self):
        #Returns the length of this Dictionary.
        return self.statuscode_set.count()

    def codes(self):
        #Returns all keys (in our case, codes) in this Dictionary as a list
        return [statcodepair.code for statcodepair in self.statuscode_set.all()]

    #Displays name of dict on admin page
    def __str__(self):
        return self.name
    

class StatusCode(models.Model):
    container = models.ForeignKey(Dict, db_index=True)
    status    = models.CharField(max_length=40, db_index=True)
    code      = models.IntegerField( db_index=True)
    def __str__(self):
        return "%s: %s" %(self.code, self.status)
