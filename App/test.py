# group.py
# def GetOne(self):
#     # id = self.Data['id']
#     #
#     # record = self.gdb.query(Groups).filter(Groups.group_id == id).one_or_none()
#     # if record is not None:
#     #     resp = {
#     #         'name': record.group_name,
#     #     }
#     #
#     #     return resp
#
#     members = self.gdb.query(GroupMembers).filter(GroupMembers.group_id == 1).filter(
#         GroupMembers.contact_id != 1).all()
# def GetAllGroups(self):
#     records = self.gdb.query(Groups).all()
#
#     resp = {
#         "records": [],
#         "total_records": len(records)
#     }
#     for rec in records:
#         resp['records'].append({
#             'group_id': rec.group_id,
#             'group_name': rec.group_name,
#         })
#
#     return resp

# def Update(self):
#     id = self.Data['group_id']
#
#     record = self.gdb.query(Groups).filter(Groups.group_id == id).one_or_none()
#     if record is not None:
#         record.group_name = self.Data['group_name']
#
# def Delete(self):
#     id = self.Data['group_id']
#
#     self.gdb.query(Groups).filter(Groups.group_id == id).delete()
#     self.gdb.flush()





# contacts.py
# def Update(self):
#     id = self.Data['id']
#
#     record = self.gdb.query(Contacts).filter(Contacts.contact_id == id).one_or_none()
#     if record is not None:
#         record.name = self.Data['name']
#         record.phone_no = self.Data['phone_no']





# msg.py
# def GetOneSend(self):
#     id = self.Data['send_msg_id']
#
#     record = self.gdb.query(Send).filter(Send.send_msg_id == id).one_or_none()
#     if record is not None:
#         resp = {
#             'send_msg_text': record.send_msg_text,
#             'sender_id': record.sender_id,
#             'receiver_id': record.receiver_id
#         }
#
#         return resp
#
# def GetOneReceive(self):
#     id = self.Data['receive_msg_id']
#
#     record = self.gdb.query(Receive).filter(Receive.receive_msg_id == id).one_or_none()
#     if record is not None:
#         resp = {
#             'receive_msg_text': record.receive_msg_text,
#             'sender_id': record.sender_id,
#             'receiver_id': record.receiver_id
#         }
#
#         return resp
#
# def GetAllSend(self):
#     records = self.gdb.query(Send).all()
#
#     resp = {
#         "records": [],
#         "total_records": len(records)
#     }
#     for rec in records:
#         resp['records'].append({
#             'send_msg_text': rec.send_msg_text,
#             'sender_id': rec.sender_id,
#             'receiver_id': rec.receiver_id,
#         })
#
#     return resp
#
# def GetAllReceive(self):
#     records = self.gdb.query(Receive).all()
#
#     resp = {
#         "records": [],
#         "total_records": len(records)
#     }
#     for rec in records:
#         resp['records'].append({
#             'receive_msg_text': rec.receive_msg_text,
#             'sender_id': rec.sender_id,
#             'receiver_id': rec.receiver_id
#         })
#
#     return resp
#
# def Delete(self):
#     id = self.Data['send_msg_id']
#
#     self.gdb.query(Send).filter(Send.send_msg_id == id).delete()
#     self.gdb.query(Receive).filter(Receive.send_msg_id == id).delete()
#     self.gdb.flush()

# def Update(self):
#     id = self.Data['send_msg_id']
#
#     record = self.gdb.query(Send).filter(Send.send_msg_id == id).one_or_none()
#     if record is not None:
#         record.send_msg_text = self.Data['send_msg_text']
#         record.sender_id = self.Data['sender_id']
#         record.receiver_id = self.Data['receiver_id']




