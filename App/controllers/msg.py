from models.app_models import Msg, GroupMembers


class MsgController:
    def __init__(self, context):
        self.slug = 'msg'
        self.PublicMethods = ['CreateMsg', 'CreateGroupMsg', 'GetOneSend', 'GetOneReceive', 'GetAllSend',
                              'GetAllReceive', 'Delete', 'Update']

        self.Data = context.Data if hasattr(context, 'Data') and context.Data is not None else {}
        self.gdb = context.gdb if hasattr(context, 'gdb') and context.gdb is not None else None

    def CreateMsg(self):
        msg = Msg()
        msg.msg_text = self.Data['msg_text']
        msg.sender_id = self.Data['sender_id']
        msg.receiver_id = self.Data['receiver_id']

        self.gdb.add(msg)
        self.gdb.flush()

    def CreateGroupMsg(self):
        msg_text = self.Data['msg_text']
        sender_id = self.Data['sender_id']
        group_id = self.Data['group_id']

        members = self.gdb.query(GroupMembers).filter(GroupMembers.group_id == group_id).all()
        for member in members:
            if sender_id == member.contact_id:
                records = self.gdb.query(GroupMembers).filter(GroupMembers.group_id == group_id).all()
                for record in records:
                    if sender_id != record.contact_id:
                        group_msg = Msg()
                        group_msg.msg_text = msg_text
                        group_msg.sender_id = sender_id
                        group_msg.receiver_id = record.contact_id
                        group_msg.group_id = record.group_id

                        self.gdb.add(group_msg)
                        self.gdb.flush()




