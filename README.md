```markdown
# Weather Application

This is a simple weather application built using Python and the Tkinter library for the GUI. It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly interface.

## Features

- Fetches current weather information for any city.
- Displays temperature, humidity, pressure, wind speed, sunrise and sunset times, cloudiness, and weather description.
- User-friendly GUI with input validation.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Requests
- Pillow (PIL Fork)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Install the required packages:
    ```bash
    pip install requests pillow
    ```

3. (Optional) If you don't have Tkinter installed, you can install it using:
    ```bash
    sudo apt-get install python3-tk
    ```

## Usage

1. Replace the `api_key` variable in the `get_weather` function with your OpenWeatherMap API key. You can get a free API key by signing up on the [OpenWeatherMap website](https://openweathermap.org/).

2. Run the application:
    ```bash
    python weather_app.py
    ```

3. Enter the name of the city in the input field and click on the "Get Weather" button to fetch the weather information.

## Code Overview

### `weather_app.py`

This is the main script that contains the following functions:

- `get_weather(city)`: Fetches weather data for the specified city from the OpenWeatherMap API.
- `show_weather()`: Retrieves the city name from the input field, calls `get_weather`, and updates the weather information label.
- GUI setup: Creates the main window, input field, button, and label to display the weather information.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.
- [Python](https://www.python.org/) for being an awesome programming language.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI library.

```

Save this content into a `README.md` file in your project's root directory. This file provides a comprehensive overview of your weather application, including installation instructions, usage, and a code overview.

Sample of GUI Window: ![image](https://github.com/user-attachments/assets/1f5a52b8-ae37-4258-be6e-5d8922bf724f)
