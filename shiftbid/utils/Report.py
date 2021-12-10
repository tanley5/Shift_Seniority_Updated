# import pandas as pd
# import database connection settings
# from email_object import email_connection

import time
from shiftbid.models import Shiftbid
from seniority.models import Seniority
from shift.models import Shift

class Report():
    def __init__(self, pk):
        
        self.first_sent = True
        self.sent_to_admin = False
        
        self.set_shiftbid(pk)
        self.set_report_name()
        self.set_all_shift()
        self.set_all_seniority()
        self.set_filled_shift()
        self.set_empty_shift()
        self.set_current_seniority()
        
        self.create_email_message_link()
        
        # Epoch Attributes
        self.set_current_epoch()
        self.set_last_epoch()
#----------------Setter---------------------
    def set_shiftbid(self,pk):
        self.shiftbid = Shiftbid.objects.get(pk=pk)

    def set_report_name(self):
        self.report_name = self.shiftbid.report_name

    def set_all_shift(self):
        shiftbid = Shiftbid.objects.get(report_name=self.get_report_name())
        self.all_shift = Shift.objects.filter(report=shiftbid)

    def set_all_seniority(self):
        # pd.read_sql(connection settings)
        shiftbid = Shiftbid.objects.get(report_name=self.get_report_name())
        self.all_seniority = Seniority.objects.filter(report=shiftbid)
    
    def set_filled_shift(self):
        shiftbid = Shiftbid.objects.get(report_name=self.get_report_name())
        self.filled_shift = Shift.objects.filter(report=shiftbid).filter(agent_email__contains='@')

    def set_empty_shift(self):
        shiftbid = Shiftbid.objects.get(report_name=self.get_report_name())
        self.empty_shift = Shift.objects.filter(report=shiftbid).exclude(agent_email__contains='@')

    def set_current_seniority(self):
        self.current_seniority = self.all_seniority.get(seniority_number=len(self.filled_shift)+1)
        # self.current_seniority = len(self.filled_shift)+1
#----------------End Setter-----------------
#----------------Getter---------------------
    def get_shiftbid(self):
        return self.shiftbid

    def get_report_name(self):
        return self.report_name

    def get_all_seniority(self):
        return self.all_seniority

    def get_all_shift(self):
        return self.all_shift()

    def get_filled_shift(self):
        return self.filled_shift

    def get_empty_shift(self):
        return self.empty_shift

    def get_current_seniority(self):
        return self.current_seniority

    def get_current_email_link(self):
        return self.email_message_link
#----------------End Getter-----------------
#----------------Epoch Setter---------------
    def set_current_epoch(self):
        self.current_epoch = len(self.filled_shift)

    def set_last_epoch(self):
        self.last_epoch = len(self.empty_shift)
#----------------End Epoch Setter-----------
#----------------Epoch Getter---------------
    def get_current_epoch(self):
        return self.current_epoch

    def get_last_epoch(self):
        return self.last_epoch
#----------------End Epoch Getter-----------
#----------------Other Methods--------------
    def update_fields(self):
        self.set_all_shift()
        self.set_filled_shift()
        self.set_empty_shift()
        self.set_current_seniority()

    def update_epoch(self):
        self.set_current_epoch()

    def check_fields_updated(self):
        self.update_fields()
        print(f"Current Epoch: {self.get_current_epoch()}")
        print(f"Filled Shift: {len(self.get_filled_shift())}")
        if self.current_epoch == len(self.filled_shift):
            return False
        else:
            return True

    # Modify this method to fit the view link
    def create_email_message_link(self):
        self.email_message_link = f"http://localhost:8000/response/response_collection/{self.get_report_name()}"

    def send_email(self):
        agent_email = self.current_seniority.agent_email
        message = f"Please Click On The Link To Select Your Shift. {self.get_current_email_link()}."
        print(agent_email)
        print(message)
        # send email
    
    def send_to_admin(self):
        email_address = "tanley.bench@usanainc.com"
        message = f"All fields for {self.report_name} are filled"
        print(email_address)
        print(message)
        # send email

    def create_report(self):
        while len(self.get_filled_shift()) != len(self.get_all_seniority()):
            # update all fields
            self.update_fields()
            # if the current epoch == 0, send first epoch email and update epoch
            if self.first_sent:
                self.send_email()
                self.first_sent = not self.first_sent
                time.sleep(20)
            # else check for updates
            else:
                if self.check_fields_updated():
                    print("subsequent sent")
                    self.send_email()
                    self.update_epoch()
                    time.sleep(20)
            # if the rows are updated, updated epoch and go forward to next seniority
                else:
                    print("sleep called")
                    time.sleep(20)
        #send email to admin
        self.send_to_admin()

    #     if self.first_sent:
    #         while(self.current_epoch < self.last_epoch):
    #             if self.check_fields_updated():
    #                 self.update_fields()
    #                 # send email
    #                 self.update_epoch()
    #             else:
    #                 break

    #         if self.current_epoch == self.last_epoch:
    #             # Send email to me
    #             self.sent_to_admin = not self.sent_to_admin
    #     else:
    #         # send first email
    #         self.first_sent = not self.first_sent

