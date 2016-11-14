#!/usr/bin/env python

import grafana.exceptions

class GrafanaClient(object):
    """
    Represents a grafana client endpoint.
    It doesn't have a connection that is
    always alive but has the grafana credentials
    and hostname/ip.
    """
    server = "localhost"    # default
    port = 3000             # default
    username = "admin"      # default.
    password = "admin"      # default.
    api_token = ""          # default.
    session_cookie = ""     # default.
    auth_mode = "basic"     # default. Can be "basic", "token", "session_cookie".

    def __init__(self, server, port, auth_mode):
        if len(server) == 0:
            throw EmptyServerException()
        else:
            self.server = server
        if !isValidPort(port):
            throw InvalidPortException()
        else:
            self.port = port
        if !isValidAuthMode(mode):
            throw InvalidAuthModeException()
        else:
            self.auth_mode = auth_mode

    def setCredentials(self, **kwargs):
        if self.auth_mode == "basic":
            self.username = kwargs['username']
            self.password = kwargs['password']
        else:
            throw UnsupportedAuthModeException()




