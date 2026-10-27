from kivy.app import App
from kivy.uix.label import Label

class CyberApp(App):
    def build(self):
        return Label(text="Hello, Gojo Cyber!", font_size=50)

if __name__ == '__main__':
    CyberApp().run()
