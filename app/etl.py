from pathlib import Path
from app import db
from app.models import Contact

class Uploader:
    def __init__(self, contacts):
        self.db = db
        self.contacts = contacts
        self.detect_upload()
    def detect_upload(self):
        contacts = self.contacts
        if isinstance(contacts, list):
            self.upload_type = 'list'
        elif isinstance(contacts, str):
            if contacts.split('.')[-1] == '.csv':
                self.upload_type = 'csv'
            elif contacts.split('.')[-1] == '.xlsx':
                self.upload_type = 'xlsx'
        else:
            raise Exception(f'Unprocessable type: {type(contacts)}')
    def upload_contacts(self):
        if self.upload_type == 'list':
            for row in self.contacts:
                c = Contact(FirstName=row['first_name'],
                            LastName=row['last_name'],
                            Email=row['email'],
                            Phone=row['cell_phone'])
                db.session.add(c)
                db.session.commit(c)


