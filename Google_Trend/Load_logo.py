from PIL import Image, ImageTk

def root_logo():
    image = Image.open(r"F:\100+ Projects\Google_Trend\artboard_123065.png") 
    logo = ImageTk.PhotoImage(image)
    return logo


