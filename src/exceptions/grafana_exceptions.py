class EmptyServerException(Exception):
    message = "Server ip/hostname not provided"

class EmptyDashboardTitleException(Exception):
    message = "Title for dashboard not provided"

class InvalidPanelIDFormatException(Exception):
    message = "Panel ID should be an integer"

class DashboardCreateFailedException(Exception):
    message = "Failed to create dashboard"

class DataSourceCreateFailedException(Exception):
    message = "Failed to create datasource"

class InvalidPortFormatException(Exception):
    message = "Invalid port provided"

class InvalidDataSourceFormatException(Exception):
    message = "Passed object not of expected DataSource type"