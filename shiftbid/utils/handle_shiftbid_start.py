import pandas as pd
import schedule
import threading
import time

from shift.models import Shift
from seniority.models import Seniority

from .Report import Report



def test_running():
    for i in range(10):
        print(i)
        time.sleep(1)
            

def handleShiftbidStart(pk):
    report = Report(pk)
    report.create_report()
    #test_running()

#_____________________________________________________________________________________

# def check_fields_updated(current_epoch, shiftbid):
#     all_shift = Shift.objects.filter(report=shiftbid)
#     filled_shift = all_shift.exclude(agent_email__isnull=False)
#     if current_epoch == len(filled_shift):
#         return False
#     else:
#         return True



# def track_attributes(report_object):
#     shiftbid = report_object.get_shiftbid()
#     all_shift = report_object.get_all_shift()
#     filled_shift = report_object.get_filled_shift()
#     empty_shift = report_object.get_empty_shift()
#     all_seniority = report_object.get_all_seniority()
#     current_seniority = report_object.get_current_seniority()

#     current_epoch=report_object.get_current_epoch()
#     last_epoch = report_object.get_last_epoch()
#     # first_sent= False
#     sent_to_admin= False

#     # start_schedule = 1
    
#     # while start_schedule:
#     if current_epoch < last_epoch:
#         if check_fields_updated(current_epoch,shiftbid):
#             # update_fields
#             all_shift = Shift.objects.filter(report=shiftbid)
#             filled_shift = all_shift.exclude(agent_email__isnull=False)
#             empty_shift = all_shift.exclude(agent_email__isnull=True)
#             current_seniority = all_seniority.get(seniority_number=len(filled_shift)+1)
#             # send email
#             current_epoch = len(filled_shift)
#     else:
#         sent_to_admin = not sent_to_admin
#         # send email to admin
#             # start_schedule = 0
