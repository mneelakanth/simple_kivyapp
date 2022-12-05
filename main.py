import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.lang import Builder

from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, AggOperations
# import matplotlib.pyplot as plt

kv_file =  Builder.load_string('''

<MyDisplayData>:
    orientation: 'vertical'
    BoxLayout:    
        Label:
            text: root.display_text

    BoxLayout:
        Button:
            id: start_btn
            text: "start"
            on_press: root.on_btn_start()
            size_hint: .2, .2 
            disabled: not root.connect_stream

        Button:
            id: start_stream
            text: "Stream"
            on_press: root.on_btn_data_stream()
            size_hint: .2, .2 
            disabled: not root.data_stream
        
        Button:
            id: stop_btn
            text: "stop"
            size_hint: .2, .2 
            on_press: root.on_btn_stop()
            disabled: root.connect_stream
            
''')


class MyDisplayData(BoxLayout):
    display_text = StringProperty('Start Connection')
    connect_stream = BooleanProperty(True)
    data_stream = BooleanProperty(False)
    
    def on_btn_start(self):
        if self.connect_stream:
            self.display_text = 'Connected... Stream to display data'
            self.connect_stream = False
            self.data_stream = True
    
    def on_btn_data_stream(self):
        if self.data_stream:
            self.data_stream = False
            self.display_text = 'Displaying data.....'

    def on_btn_stop(self):
        self.display_text = 'Start Connection'
        self.connect_stream = True
        self.data_stream = False
        
class KivyApp(App):
    def build(self):
        return MyDisplayData()
      

if __name__ == "__main__":
    KivyApp().run()
