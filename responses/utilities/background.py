import pandas as pd

import threading
import time

import schedule

from shiftbid.models import Shiftbid
from shift.models import Shift
from seniority.models import Seniority


class Report():
    def __init__(self, report_name, email_object):
        self.report_name = report_name
        self.first_sent = False
        self.sent_to_admin = False
        self.set_report()
        self.set_all_shift()
        self.set_all_seniority()
        self.set_filled_shift()
        self.set_empty_shift()
        self.set_current_seniority()
        # Epoch Attributes
        self.set_current_epoch()
        self.set_last_epoch()
        # Email Attributes
        self.email_object = email_object
        self.create_email_message_link()

    def set_report(self):
        shiftbid_object = Shiftbid.objects.get(report_name=self.report_name)
        self.report = shiftbid_object

    def set_all_shift(self):
        df = pd.DataFrame.from_records(
            Shift.objects.filter(report=self.report).values())
        self.all_shift = df

    def set_all_seniority(self):
        df = pd.DataFrame.from_records(
            Seniority.objects.filter(report=self.report).values())
        self.all_seniority = df

    def set_filled_shift(self):
        df = self.all_shift
        self.filled_shift = df[df["agent_email"] != '']

    def set_current_seniority(self):
        self.current_seniority = len(self.filled_shift)+1

    def set_empty_shift(self):
        df = self.all_shift
        self.empty_shift = df[df["agent_email"] == '']

    def set_current_epoch(self):
        self.current_epoch = len(self.filled_shift)

    def set_last_epoch(self):
        self.last_epoch = len(self.empty_shift)

    def get_last_epoch(self):
        return self.last_epoch

    def get_current_epoch(self):
        return self.current_epoch

    def get_current_seniority(self):
        return self.current_seniority

    def get_all_seniority(self):
        return self.all_seniority

    def get_all_shift(self):
        return self.all_shift()

    def get_filled_shift(self):
        return self.filled_shift

    def get_empty_shift(self):
        return self.empty_shift

    def update_fields(self):
        self.set_all_shift()
        self.set_filled_shift()
        self.set_empty_shift()
        self.set_current_seniority()

    def update_epoch(self):
        self.set_current_epoch()

    def check_fields_updated(self):
        if self.current_epoch == len(self.filled_shift):
            return False
        else:
            return True

    # Modify this method to fit the view link
    def create_email_message_link(self):
        self.email_message_list = f"https://localhost/8000/shiftbid_response/{self.report_name}"

    def create_report(self):
        if self.first_sent:
            while(self.current_epoch < self.last_epoch):
                if self.check_fields_updated():
                    self.update_fields()
                    # send email
                    self.update_epoch()
                else:
                    break

            if self.current_epoch == self.last_epoch:
                # Send email to me
                self.sent_to_admin = not self.sent_to_admin
        else:
            # send first email
            self.first_sent = not self.first_sent


# Get All Reports By Name


def get_report_names():
    report_names = []
    reports = Shiftbid.objects.all()
    for i in reports:
        report_names.append(i.report_name)
    return report_names

# Create a list of Report objects & Schedule and call report creation function

# This is the function to repeat


def report_objects():
    list_of_reports = [Report(report_name=i, email_object="")
                       for i in get_report_names()]
    [report.create_report() for report in list_of_reports]

# Set up multi threading


def run_threaded(job):
    job_threaded = threading.Thread(target=job)
    job_threaded.start()


# setup scheduler. The function below is for testing
def job():
    print("I'm running on thread %s" % threading.current_thread())


def schedule_task():
    print("called the background_task thread")
    schedule.every(10).seconds.do(run_threaded, job)
    while 1:
        schedule.run_pending()
        time.sleep(1)

    # End the scheduled report when all shifts are filled
