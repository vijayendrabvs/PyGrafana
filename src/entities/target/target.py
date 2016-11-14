#!/usr/bin/env python

"""
                                "targets": [{
                                        "refId": "A",
                                        "expr": "avg(rate(container_cpu_usage_seconds_total{container_name=\"roxdb\"}[30m])*100)",
                                        "intervalFactor": 2,
                                        "metric": "",
                                        "step": 1
                                }],
"""

class Target(object):
    refId = "A"         # default
    expr = ""
    intervalFactor = 2  # default
    metric = ""
    step = 1            # default

    def __init__(self, expr):
        self.expr = expr
        return