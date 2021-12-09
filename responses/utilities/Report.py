# import pandas as pd
# import database connection settings
# from email_object import email_connection

class Report():
    def __init__(self, report_name, email_object):
        self.report_name = report_name
        self.first_sent = False
        self.sent_to_admin = False
        # Email Attributes
        self.email_object = email_object
        self.create_email_message_link()
        self.set_all_shift()
        self.set_all_seniority()
        self.set_filled_shift()
        self.set_empty_shift()
        self.set_current_seniority()
        # Epoch Attributes
        self.set_current_epoch()
        self.set_last_epoch()

    def set_last_epoch(self):
        self.last_epoch = len(self.empty_shift)

    def get_last_epoch(self):
        return self.last_epoch

    def set_current_epoch(self):
        self.current_epoch = len(self.filled_shift)

    def get_current_epoch(self):
        return self.current_epoch

    def set_current_seniority(self):
        self.current_seniority = len(self.filled_shift)+1

    def get_current_seniority(self):
        return self.current_seniority

    def set_all_seniority(self):
        df = ''  # pd.read_sql(connection settings)
        #self.all_seniority = df.filter(self.report_name)

    def get_all_seniority(self):
        return self.all_seniority

    def set_all_shift(self):
        df = ''  # pd.read_sql(connection settings)
        #self.all_shift = df.filter(self.report_name)

    def get_all_shift(self):
        return self.all_shift()

    def set_filled_shift(self):
        df = self.all_shift  # get all filled email address, remove the rest
        #self.filled_shift = df.filter(self.report_name)

    def get_filled_shift(self):
        return self.filled_shift

    def set_empty_shift(self):
        df = self.all_shift  # get all empty email address column, remove the rest
        # self.empty_shift = self.all_shift  # filter self.allfilled_shift

    def get_empty_shift(self):
        return self.empty_shift

    def update_fields(self):
        self.set_all_shift()
        # self.set_all_seniority()
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
