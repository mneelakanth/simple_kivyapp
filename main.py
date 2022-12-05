import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

from kivy.clock import Clock
from functools import partial


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

class DisplayData:

    def start(self):
        print('started streaming!! ')
    
    def start_stream(self):
        Clock.schedule_interval(self.data_gen, 0.5)
    
    def data_gen(self, *args):
        i = 0
        data = i+1
        return data
    
    def stop(self):
        Clock.unschedule(self.data_gen)
        print('streaming stopped!! ')

class MyDisplayData(BoxLayout, DisplayData):
    display_text = StringProperty('Start Connection')
    connect_stream = BooleanProperty(True)
    data_stream = BooleanProperty(False)
    dis_flow = DisplayData()

    def on_btn_start(self):
        if self.connect_stream:
            self.dis_flow.start()
            self.display_text = 'Connected... Stream to display data'
            self.connect_stream = False
            self.data_stream = True
            print('start connection')
    
    def on_btn_data_stream(self):
        if self.data_stream:
            self.dis_flow.start_stream()
            self.data_stream = False
            self.display_text = str(self.dis_flow.data_gen() + 1)  
            print('Displaying data.....')

    def on_btn_stop(self):
        self.dis_flow.stop()
        self.display_text = 'Start Connection'
        self.connect_stream = True
        self.data_stream = False
        print('stop connection')
        
class KivyApp(App):
    def build(self):
        return MyDisplayData()
      

if __name__ == "__main__":
    KivyApp().run()
