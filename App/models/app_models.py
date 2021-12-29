from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Contacts(Base):
    __tablename__ = 'contacts'

    contact_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    phone_no = Column(String(64), unique=True, nullable=False)


class Groups(Base):
    __tablename__ = 'chat_groups'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(256), nullable=False)


class GroupMembers(Base):
    __tablename__ = 'chat_group_members'

    group_member_id = Column(Integer, primary_key=True)

    group_id = Column(ForeignKey(Groups.group_id, ondelete='RESTRICT'))
    group = relationship(Groups, remote_side=Groups.group_id, foreign_keys=group_id)

    contact_id = Column(ForeignKey(Contacts.contact_id, ondelete='RESTRICT'), nullable=False)
    contact = relationship(Contacts, remote_side=Contacts.contact_id, foreign_keys=contact_id)


class Msg(Base):
    __tablename__ = 'msg'

    msg_id = Column(Integer, primary_key=True)
    msg_text = Column(String(1024))

    sender_id = Column(ForeignKey(Contacts.contact_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    sender = relationship(Contacts, remote_side=Contacts.contact_id, foreign_keys=sender_id)

    receiver_id = Column(ForeignKey(Contacts.contact_id, onupdate='RESTRICT', ondelete='RESTRICT'), nullable=True)
    receiver = relationship(Contacts, remote_side=Contacts.contact_id, foreign_keys=receiver_id)

    group_id = Column(ForeignKey(Groups.group_id, ondelete='RESTRICT'), nullable=True)
    group = relationship(Groups, remote_side=Groups.group_id, foreign_keys=group_id)


