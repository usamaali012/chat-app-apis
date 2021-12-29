from models.app_models import Contacts


class ContactController:
    def __init__(self, context):
        self.slug = 'contacts'
        self.PublicMethods = ['Create', 'Update', 'GetAll', 'GetOne', 'Delete']

        self.Data = context.Data if hasattr(context, 'Data') and context.Data is not None else {}
        self.gdb = context.gdb if hasattr(context, 'gdb') and context.gdb is not None else None

    def Create(self):
        contact = Contacts()
        contact.name = self.Data['name']
        contact.phone_no = self.Data['phone_no']

        self.gdb.add(contact)
        self.gdb.flush()


    def GetOne(self):
        id = self.Data['id']

        record = self.gdb.query(Contacts).filter(Contacts.contact_id == id).one_or_none()
        if record is not None:
            resp = {
                'name': record.name,
                'phone': record.phone_no
            }

            return resp

    def GetAll(self):
        records = self.gdb.query(Contacts).all()

        resp = {
            "records": [],
            "total_records": len(records)
        }
        for rec in records:
            resp['records'].append({
                'id': rec.contact_id,
                'name': rec.name,
                'phone_no': rec.phone_no,
            })

        return resp


    def Delete(self):
        id = self.Data['id']

        self.gdb.query(Contacts).filter(Contacts.contact_id == id).delete()
        self.gdb.flush()