from kivy.app import App
from kivy.uix.button import Button

class QasosApp(App):
    def build(self):
        # Tugma bosilganda o'yin boshlanishi haqida xabar
        return Button(text="Qasos o'yini\nBexruz tomonidan tayyorlandi", font_size='20sp')

if __name__ == '__main__':
    QasosApp().run()
