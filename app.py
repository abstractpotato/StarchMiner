# temp location for new app.py
# check config to see if it needs ui
from json import load
from pathlib import Path
from modules.ui.window import Window, Button, Text

def get_config():
    if not Path("config.json").exists():
        return {}

    print("starting with config")
    with open("config.json") as json_data:
        return load(json_data)

def test_func(button, event):
    new_position = (button.position[0] + 1, button.position[1])
    button.position = new_position

if __name__ == "__main__":
    config = get_config()
    window = Window(config)
    b1 = Button("start mining $", (32, 32), test_func, "green")
    # b2 = Button("testing", (0, 20), test_func, "red")
    window.add_element(b1)
    # window.add_element(b2)
    # window.add_process(test_func)
    window.run()
