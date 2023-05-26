# Currency-ExchangeRate
# Currency Converter

This is a Python project that implements a real-time currency converter using an API key URL. The application fetches the latest exchange rates from a reliable source and provides users with the ability to convert between different currencies.

## Installation

To run this project, please follow these steps:

1. Clone the repository to your local machine or download the project files.

2. Make sure you have Python installed on your system. This project is compatible with Python 3.

3. Install the required dependencies by running the following command:

   ```shell
   pip install requests Pillow
   ```

## Usage

To use the currency converter, follow these steps:

1. Obtain an API key URL for exchange rate data. You can use services like Open Exchange Rates or Fixer.io to get an API key URL.

2. Replace the `url` variable in the code with your API key URL:

   ```python
   url = 'YOUR_API_KEY_URL'
   ```

3. Run the Python script using the following command:

   ```shell
   python currency_converter.py
   ```

4. The currency converter application will open in a GUI window.

5. Select the source and target currencies from the dropdown menus.

6. Enter the amount to convert in the input field.

7. Click the "Convert" button to perform the conversion.

8. The converted amount will be displayed in the output field.

9. You can click the "Reset" button to clear the input and output fields.

10. To exit the application, click the "Exit" button or close the window.

## Dependencies

- requests: This library is used to make HTTP requests to the API key URL and fetch the exchange rate data.

- Pillow: This library is used for image processing and displaying an animated text on the GUI window.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This project utilizes exchange rate data from the API key URL, provided by reputable exchange rate data providers.

- The GUI interface is implemented using the tkinter library in Python.

- The animation of the text is implemented using the PIL (Python Imaging Library) module.

## Contributors

- Vinay
- 

Please feel free to contribute to this project by submitting pull requests with improvements or additional features.

Enjoy using the Currency Converter!
