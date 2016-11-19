from rapidsms.contrib.handlers import PatternHandler
from django.utils import timezone
from .models import Status, StatusCode, Dict, Borehole

class UpdateHandler(PatternHandler):
    pattern = r'^(\d{3})#(\d{0,3}).{0,2}\s*$'
    
    #Since the pattern above did not guarantee ANY digits, use None to avoid error
    def handle(self, boreholeID, msgCode):
        #Establish Dictionary as a Dictionary of status_code ##SHOULD NOT NEED TO CHANGE
        ##Change StatusCode on admin page, but not Dict
        dictionary= Dict.getDict('status_code') 
        
        #change passed variables to integers
        boreholeID, msgCode = int(boreholeID), int(msgCode)
        for code in dictionary.codes():
            if code == msgCode:              
                #Store status in table       
                status = Status.objects.create(
                    borehole_id     = boreholeID, 
                    status          = dictionary[code], 
                    datetime        = timezone.now())
                status.save() 
                #Update Status in Borehole
                for bh in Borehole.objects.all():
                    if bh.borehole_ID == boreholeID:
                        bh.current_status = dictionary[code]
                        bh.status_time = timezone.now()
                        bh.save()

                #Inquire About Issue of Borehole (Maintain the same connection)
                self.respond(
                    "Borehole %i  %s. (Received message: %d)" %
                    (boreholeID, dictionary[code], msgCode))         
        else:
            self.respond("Unclear Message. Try Again")

