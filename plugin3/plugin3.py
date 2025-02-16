import requests
import customtkinter as ctk
import io

try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "Pillow"])
    from PIL import Image, ImageTk

packages = []

# Function to fetch and display a cute image
def fetch_cute_image(cute_image_label):
    url = "https://api.thecatapi.com/v1/images/search"  # The Cat API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            img_url = data[0]["url"]

            # Download the image
            img_response = requests.get(img_url)
            img_data = img_response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((300, 300), Image.Resampling.LANCZOS)

            # Display the image in the GUI
            cute_image = ctk.CTkImage(light_image=img, size=(300, 300))
            cute_image_label.configure(image=cute_image)
            cute_image_label.image = cute_image  # Keep a reference

    except Exception as e:
        print("Error fetching image:", e)

def register_plugin(app, tabview):
    """Registers the plugin with the main application."""
    # Add a new tab to the app
    new_tab = tabview.add("Cute Images")

    # Label to display the image
    cute_image_label = ctk.CTkLabel(new_tab, text="")
    cute_image_label.pack(pady=10)

    # Button to load an image
    fetch_button = ctk.CTkButton(new_tab, text="Get Cute Image", 
                                 command=lambda: fetch_cute_image(cute_image_label))
    fetch_button.pack(pady=10)
