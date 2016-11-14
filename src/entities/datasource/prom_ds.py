#!/usr/bin/env python

from src.entities.datasource.ds import DataSource

class PrometheusDataSource(DataSource):
    def __init__(self, name, url):
        super.__init__(self, name, url, "prometheus", "direct")
        return
