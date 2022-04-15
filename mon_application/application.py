from kivy.app import App            # appelation du class App          
from kivy.lang import Builder      #builder pour appeler un dos exter
from kivy.core.window import Window  #window -> controle :size,color
from kivy.uix.screenmanager import ScreenManager, Screen  #screenmanager page principale
Window.clearcolor = (0.0, 1.7, 0.3, 1.0)
Window.size = (300,350)
class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class Error(Screen):
    pass
class Python (Screen):
    pass
class Php (Screen):
    pass
class Html (Screen):
    pass
class Java (Screen):
    pass
class Sql (Screen):
    pass
class Css (Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv=Builder.load_file("my.kv")
class MyMainApp(App):
    def build(self): 
        return kv    
        self.title='driss'  
MyMainApp().run()