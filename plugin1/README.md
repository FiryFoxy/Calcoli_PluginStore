# Change Converter Plugin

## Description
The Change Converter is a currency conversion tool that not only converts amounts between different currencies but also provides a detailed breakdown of the change in the target currency's denominations. It uses real-time exchange rates from the Exchange Rate API.

## Features
- Real-time currency conversion using current exchange rates
- Detailed breakdown of change in the target currency
- Support for major global currencies
- User-friendly interface
- Live API integration with Exchange Rates API

## Installation
1. Ensure you have the required dependencies:
   ```python
   pip install requests customtkinter
   ```
2. Place the `change_converter.py` file in your plugins directory
3. The plugin will automatically register with the main application

## Usage
1. Launch the main application
2. Navigate to the "Change Converter" tab
3. Enter the amount in USD
4. Enter the target currency code (e.g., EUR, GBP, JPY)
5. Click "Convert" to see the results

Example input:
- Amount: 123.45 USD
- Target Currency: EUR

Example output: