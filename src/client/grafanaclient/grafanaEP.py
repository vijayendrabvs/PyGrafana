#!/usr/bin/env python

from src.exceptions.grafana_exceptions import InvalidPortFormatException

class GrafanaEndPoint(object):
    grafana_ip = "localhost"
    grafana_port = 3000
    username = ""
    password = ""

    def __init__(self, hostname, port, username="admin", pwd="admin"):
        if isinstance(port, int):
            self.grafana_port = port
        else:
            raise InvalidPortFormatException("Grafana endpoint port must be an int")
        self.grafana_ip = hostname
        self.username = username
        self.password = pwd