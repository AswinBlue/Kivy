from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout


class StackExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 10):
            size = dp(100)  # dp로 크기 선언법
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))  # 버튼 세팅
            self.add_widget(b)  # layout에 widget 추가

# class GridExample(GridLayout):
#     pass

class AnchorExample(AnchorLayout):
    pass

class BoxExample(BoxLayout):
  def __init__(self, **kargs):
    super().__init__(**kargs)
    b1 = Button(text="A")
    b2 = Button(text="B")
    self.add_widget(b1)
    self.add_widget(b2)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()