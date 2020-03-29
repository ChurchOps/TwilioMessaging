from app import db
from app.models import Contact

contacts = db.session.query(Contact).all()
for contact in contacts:
    db.session.delete(contact)

db.session.commit()
print("Contact table cleared")