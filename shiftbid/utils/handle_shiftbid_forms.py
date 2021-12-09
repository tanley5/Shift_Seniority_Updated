import pandas as pd

from shiftbid.models import Shiftbid
from shift.models import Shift
from seniority.models import Seniority


def handle_shiftbid_creation(name):
    shiftbid = Shiftbid.objects.create(report_name=name)


def handle_shift_creation(file_name, report_name):
    shiftbid = Shiftbid.objects.get(report_name=report_name)

    df = pd.read_excel(file_name)
    for index, row in df.iterrows():
        #the_shift = ''
        for i in row.to_numpy():
            shift = Shift.objects.create(shift=i)
            shift.report = shiftbid
            shift.save()


def handle_seniority_creation(filename, report_name):
    shiftbid = Shiftbid.objects.get(report_name=report_name)

    df = pd.read_excel(filename)
    print(type(df))
    for index, row in df.iterrows():
        agent_id = row.agent_id
        seniority_number = row.seniority_number
        agent_email = row.agent_email
        seniority = Seniority.objects.create(
            agent_net_id=agent_id, agent_email=agent_email, seniority_number=seniority_number)
        seniority.report = shiftbid
        seniority.save()
