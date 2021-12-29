from .contacts import ContactController
from .msg import MsgController
from .group import GroupController

registry = {
    'contacts': ContactController,
    'msg': MsgController,
    'group': GroupController,
    }