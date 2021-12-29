from models.app_models import Groups, GroupMembers


class GroupController:
    def __init__(self, context):
        self.slug = 'group'
        self.PublicMethods = ['CreateGroup', 'CreateGroupMember', 'GetOneGroup', 'GetAllGroups', 'GetOne', 'Delete']

        self.Data = context.Data if hasattr(context, 'Data') and context.Data is not None else {}
        self.gdb = context.gdb if hasattr(context, 'gdb') and context.gdb is not None else None

    def CreateGroup(self):
        group = Groups()
        group.group_name = self.Data['group_name']

        self.gdb.add(group)
        self.gdb.flush()

    def CreateGroupMember(self):
        group_member = GroupMembers()
        group_member.contact_id = self.Data['contact_id']
        group_member.group_id = self.Data['group_id']

        self.gdb.add(group_member)
        self.gdb.flush()

    def GetOneGroup(self):
        id = self.Data['group_id']

        group = self.gdb.query(Groups).filter(Groups.group_id == id).one_or_none()
        records = self.gdb.query(GroupMembers).filter(GroupMembers.group_id == id).all()
        resp = {
            'group_name': group.group_name,
            'group_members': [],
            "total_members": len(records)
        }

        for rec in records:
            resp['group_members'].append({
                'id': rec.contact_id,
                'name': rec.contact.name
            })

        return resp

   