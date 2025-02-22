from customtkinter import *
from plugins.base_plugin import BasePlugin
import requests

class ChangeConversionPlugin(BasePlugin):
    def __init__(self, app, parent):
        """
        Initialize the Change Conversion plugin
        
        Parameters:
            app: The main application window
            parent: The frame where the plugin content will be displayed
        """
        self.app = app  # Store the app reference
        self.content_frame = parent  # Store the parent frame
        self.tab_name = "Change Converter"  # Display name in navigation
        self.api_url = "https://open.er-api.com/v6/latest/USD"
        
    def create_view(self, parent):
        """
        Create the plugin's user interface
        
        Parameters:
            parent_frame: The frame where the plugin UI should be created
        """
        container = CTkFrame(parent)
        container.pack(expand=True, fill="both", padx=10, pady=10)
        
        title = CTkLabel(container, text="Change Conversion", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        self.amount_entry = CTkEntry(container, placeholder_text="Enter amount in USD")
        self.amount_entry.pack(pady=5)
        
        self.currency_entry = CTkEntry(container, placeholder_text="Enter target currency (e.g., EUR)")
        self.currency_entry.pack(pady=5)
        
        convert_button = CTkButton(container, text="Convert", command=self.calculate_change)
        convert_button.pack(pady=5)
        
        self.result_label = CTkLabel(container, text="")
        self.result_label.pack(pady=10)
        
    def fetch_exchange_rate(self, currency):
        """Fetch the exchange rate for the given currency."""
        try:
            response = requests.get(self.api_url)
            data = response.json()
            return data['rates'].get(currency.upper(), None)
        except Exception as e:
            return None
        
    def calculate_change(self):
        """Convert the amount based on exchange rates and calculate change breakdown."""
        try:
            amount = float(self.amount_entry.get())
            currency = self.currency_entry.get().upper()
            exchange_rate = self.fetch_exchange_rate(currency)
            
            if exchange_rate is None:
                self.result_label.configure(text="Invalid currency or API error.")
                return
            
            converted_amount = amount * exchange_rate
            denominations = [50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
            change_breakdown = {}
            
            for denom in denominations:
                count = int(converted_amount // denom)
                if count > 0:
                    change_breakdown[denom] = count
                    converted_amount -= count * denom
            
            result_text = f"{amount:.2f} USD = {amount * exchange_rate:.2f} {currency}\nChange breakdown:\n" \
                          + "\n".join(f"{v} x {k:.2f} {currency}" for k, v in change_breakdown.items())
            self.result_label.configure(text=result_text)
        except ValueError:
            self.result_label.configure(text="Invalid input. Enter a number.")

def register_plugin(app, content_frame):
    """
    Required function to register the plugin with the main application
    """
    return ChangeConversionPlugin(app, content_frame)
