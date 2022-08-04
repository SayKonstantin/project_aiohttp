from typing import Optional

from app.crm.models import User
from app.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Optional[Application] = None

    def

    def add_user(self, user: User):
        self.app.database['users'].append(user)

