#!/usr/bin/env python

import requests
import json
from src.entities.dashboard.dashboard import Dashboard
from src.exceptions.grafana_exceptions import DashboardCreateFailedException
from src.client.grafanaclient.grafanaEP import GrafanaEndPoint
import pickle


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, set)):
            return json.JSONEncoder.default(obj)
        return {'_python_object': pickle.dumps(obj)}


class DashboardClient(object):
    grafanaEndPoint = None
    dashboard = None

    def __init__(self, title, id, grafana_ip="localhost", grafana_port=3000, username="admin", pwd="admin"):
        self.grafanaEndPoint = GrafanaEndPoint(grafana_ip, grafana_port, username, pwd)
        self.dashboard = Dashboard(title, id)

        return

    def prepare_create_uri(self, protocol="http"):
        uri = protocol + "://" +  self.grafanaEndPoint.username + ":" + self.grafanaEndPoint.password + "@" +\
              self.grafanaEndPoint.grafana_ip + ":" +\
              str(self.grafanaEndPoint.grafana_port) + "/api/dashboards/db"
        return uri

    def prepare_delete_uri(self, protocol="http"):
        uri = protocol + "://" +  self.grafanaEndPoint.username + ":" + self.grafanaEndPoint.password + "@" +\
              self.grafanaEndPoint.grafana_ip + ":" + \
              str(self.grafanaEndPoint.grafana_port) + "/api/dashboards/db/" + self.dashboard.title.lower()
        return uri

    def create(self):
        # Creates a dashboard.
        uri = self.prepare_create_uri()
        headers = {'Content-Type': 'application/json'}
        import pdb; pdb.set_trace()
        res = requests.post(uri, json.dumps(self.dashboard.__dict__, cls=SetEncoder), headers=headers)
        if res.status_code != requests.codes.ok:
            #import pdb; pdb.set_trace()
            print("Failed to create dashboard, response: " + str(res))
            raise DashboardCreateFailedException()
        return res

    def delete(self):
        # Deletes this dashboard.
        uri = self.prepare_delete_uri("http")
        r = requests.delete(uri)
        return

    def update(self):
        return

    def get(self):
        return

    def list(self):
        return


