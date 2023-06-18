from ._utils import create_arg
from ._utils import create_config
from env import math_api

class SetReminder:

    config = create_config(
        name="set_reminder",
        desc="Sets a reminder for a number of hours later.",
        required=["hours"],
        input=create_arg(
            desc="The number of hours that the user would like to set a reminder for. "
        ),
    )

    @staticmethod
    def run(hours):
        return f"Set a reminder for {hours} hours from now."