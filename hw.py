from abc import ABC , abstractmethod
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def send_command(self):
        pass
class Smartlight(SmartDevice):
    def send_command(self):
        return f"{self.name} is now turned on."
class SmartThermostat(SmartDevice):
    def send_command(self):
        return f"{self.name} is now Set to 16°C."
devices = [Smartlight("Living Room Light"), SmartThermostat("Room Thermostat")]
for device in devices:
    print(device.send_command())
