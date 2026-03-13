import tkinter as tk
from PIL import Image
import os

class IconManager:
    """Utility class to handle window icons"""
    
    @staticmethod
    def set_icon_from_png(window, png_path='assets/icon.png'):
        """Set window icon from PNG file"""
        try:
            if os.path.exists(png_path):
                icon_image = tk.PhotoImage(file=png_path)
                window.iconphoto(True, icon_image)
                # Store the image on the window to prevent garbage collection
                window.icon_image = icon_image
                print(f"✓ Icon loaded from {png_path}")
                return True
            else:
                print(f"! Icon file not found: {png_path}")
                return False
        except Exception as e:
            print(f"✗ Error loading icon: {e}")
            return False
    
    @staticmethod
    def set_icon_from_ico(window, ico_path='assets/icon.ico'):
        """Set window icon from ICO file"""
        try:
            if os.path.exists(ico_path):
                window.iconbitmap(ico_path)
                print(f"✓ Icon loaded from {ico_path}")
                return True
            else:
                return False
        except Exception as e:
            print(f"✗ Error loading icon: {e}")
            return False
    
    @staticmethod
    def convert_png_to_ico(png_path='assets/icon.png', ico_path='assets/icon.ico', sizes=None):
        """Convert PNG to ICO file"""
        if sizes is None:
            sizes = [(16,16), (32,32), (64,64)]
        
        try:
            if os.path.exists(png_path):
                img = Image.open(png_path)
                img.save(ico_path, format='ICO', sizes=sizes)
                print(f"✓ Converted {png_path} to {ico_path}")
                return True
            else:
                print(f"! Cannot convert: {png_path} not found")
                return False
        except Exception as e:
            print(f"✗ Error converting icon: {e}")
            return False
    
    @classmethod
    def auto_set_icon(cls, window, png_path='assets/icon.png', ico_path='assets/icon.ico'):
        """Automatically try PNG first, then convert to ICO, then try ICO"""
        # Try PNG directly first
        if cls.set_icon_from_png(window, png_path):
            return True
        
        # If PNG exists but direct loading failed, try converting to ICO
        if os.path.exists(png_path):
            if cls.convert_png_to_ico(png_path, ico_path):
                return cls.set_icon_from_ico(window, ico_path)
        
        # Try ICO directly
        return cls.set_icon_from_ico(window, ico_path)