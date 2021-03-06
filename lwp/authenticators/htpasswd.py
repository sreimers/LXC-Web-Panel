# -*- coding: utf-8 -*-
from lwp.utils import check_htpasswd, config


class htpasswd:
    def __init__(self):
        self.HTPASSWD_FILE = config.get('htpasswd', 'file')

    def authenticate(self, username, password):
        user = None
        if check_htpasswd(self.HTPASSWD_FILE, username, password):
            user = {
                'username': username,
                'name': username,
                'su': 'Yes'
            }

        return user
