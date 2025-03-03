# 📊 Progress Bar

A simple Python function that displays a dynamic progress bar in the terminal. The bar updates in place as the task progresses, showing the percentage of completion.

## `start_bar` Function

The `start_bar` function displays a progress bar on a single line, updating it in place without creating a new line. It supports custom characters for the filled and unfilled portions of the bar.

## 🐍 Requirements

- Python 3.x

## 📥 Installation

You don't need to install anything — simply download [this](./progress_bar.py) file and use the function in your project.

## 👤 Usage

```python
import time
from progress_bar import start_bar

for i in range(101):
    start_bar(i, 100, 50, '#', '-', last_progress=i-1)
    time.sleep(0.1)
```

## 📥 Parameters

- **current**(`int`): The current progress value.
- **total**(`int`): The total value to reach 100%.
- **bar_length**(`int`): The length of the progress bar.
- **fill_char**(`str`): The character used to fill the progress bar.
- **empty_char**(`str`): The character used for the unfilled portion of the progress bar.
- **last_progress**(`int`): The last progress value to avoid flickering.

## 📄 Example

The example file is named `download-file-example.py` and demonstrates how to use the `start_bar` function in a file download scenario. It requires the `requests` library to download a file from a URL. Click [here](./download-file-example.py) to view the example.

