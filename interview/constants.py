# json fields
TYPE = "type"
STATION_NAME = "stationName"
TIMESTAMP = "timestamp"
TEMPERATURE = "temperature"
COMMAND = "command"
AS_OF = "asOf"
STATIONS = "stations"
HIGH = "high"
LOW = "low"

#message types
SAMPLE = "sample"
CONTROL = "control"

#command types
SNAPSHOT = "snapshot"
RESET = "reset"

# convenient commands
CONTROL_SNAPSHOT = {"type":"control", "command": "snapshot"}
CONTROL_RESET = {"type":"control", "command": "reset"}
