#!/usr/bin/env python

"""
This example creates a dashboard with two rows
in it. Each row has one panel (graph) in it.
So, we first create two panels. We then create two rows.
We then add one panel to one row and the other panel to
the other row. Finally, we create a dashboard, and add
these two rows to that dashboard. This completes creating
local entities - they aren't yet created on the actual
grafana server.

To complete that step, we simply create a DashboardClient, add
the dashboard created above to it, and and issue a create()
on this Dashboard client object.

"""
from src.client.dashboard import DashboardClient
from src.entities.row.row import Row
from src.entities.panel.panel import Panel
from src.entities.datasource.datasource import DataSource
from src.client.datasource import DataSourceClient
from src.entities.target.target import Target

def main():
    dataSource = DataSource("prometheusDataSource", "http://192.168.99.100:9090", "prometheus", "direct")
    dataSourceClient = DataSourceClient(dataSource, "192.168.99.100", 3000, "admin", "admin")
    res = dataSourceClient.get()
    dataSourceClient.dataSourceRequest = dataSource
    dataSourceClient.create()
    panel = Panel(1, dataSource)
    graph = Target("process_cpu_seconds_total")
    panel.addTarget(graph)
    row = Row()
    row.addPanel(panel)
    # Create a dashboard client with the grafana hostname/ip and port.
    # With a dashboard, we actually need to assign the id ourselves.
    dash = DashboardClient("CPUDashboard", None, "192.168.99.100", 3000, "admin", "admin")
    # Illustrating how to set dash's properties.
    dash.dashboard.setTitle("promdashboard")
    import pdb; pdb.set_trace()
    dash.dashboard.addRow(row)
    dash.create()

main()