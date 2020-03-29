from pathlib import Path
from app import db
import csv
import xlrd
from app.models import Contact

class Uploader:
    def __init__(self, contacts):
        self.db = db
        self.contacts = contacts
        self.detect_upload()
    def detect_upload(self):
        contacts = self.contacts
        print("contacts received: ", contacts)
        if isinstance(contacts, list):
            self.upload_type = 'list'
        elif isinstance(contacts, str):
            if contacts.split('.')[-1] == 'csv':
                self.upload_type = 'csv'
            elif contacts.split('.')[-1] == 'xlsx':
                self.upload_type = 'xlsx'
            else:
                raise Exception(f'Unprocessable type: {type(contacts)}')
        else:
            raise Exception(f'Unprocessable type: {type(contacts)}')
    def upload_contacts(self):
        contacts = self.contacts
        if self.upload_type == 'list':
            for row in contacts:
                c = Contact(FirstName=row['first_name'],
                            LastName=row['last_name'],
                            Email=row['email'],
                            Phone=row['phone'])
                db.session.add(c)
                db.session.commit()
        if self.upload_type == 'csv':
            if not Path(contacts).exists():
                raise Exception('Invalid Path')
            else:
                with open(contacts) as csvDataFile:
                    csvReader = csv.DictReader(csvDataFile)
                    for row in csvReader:
                        c = Contact(FirstName=row['First'],
                                    LastName=row['Last'],
                                    Email=row['Email'],
                                    Phone=row['Phone'])
                        db.session.add(c)
                        db.session.commit()
        if self.upload_type == 'xlsx':
            wb = xlrd.open_workbook(contacts)
            sheet = wb.sheet_by_index(0)
            first_names = [x.value for x in sheet.col(0)][1:]
            last_names = [x.value for x in sheet.col(1)][1:]
            emails = [x.value for x in sheet.col(2)][1:]
            phones = [x.value for x in sheet.col(2)][1:]
            for first, last, email, phone in zip(first_names, last_names, emails, phones):
                c = Contact(FirstName=first,
                            LastName=last,
                            Email=email,
                            Phone=phone)
                db.session.add(c)
                db.session.commit()




