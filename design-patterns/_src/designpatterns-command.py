from datetime import datetime, timezone

class Switch:
    """The Invoker Class"""

    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._history.append((datetime.now(tz=timezone.utc), command_name))
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Light:
    """The Receiver"""

    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


if __name__ == "__main__":
    # The Light is the Receiver
    light = Light()

    # Register the commands with the invoker (Switch)
    SWITCH = Switch()
    SWITCH.register("ON", SwitchOnCommand(light))
    SWITCH.register("OFF", SwitchOffCommand(light))

    # Execute the commands that are registered on the Invoker
    SWITCH.execute("ON")
    SWITCH.execute("OFF")
    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    # For fun, we can see the history
    print(SWITCH.history)
