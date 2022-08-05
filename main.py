from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import TwoLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from db_func import add_new_unit, all_units, delit_us




class MainWindow(Screen):
    ...

class NewUnit(Screen):
    ...

class MyUnits(Screen):
    ...
    
class MyPopup(MDDialog):
    ...
    
class MyListItem(TwoLineListItem):
    
    def __init__(self, user_id, **kwargs):
        super(MyListItem, self).__init__(**kwargs)
        self.user_id = user_id
        
    def choice_unit(self):
        self.theme_text_color = "Custom"
        self.text_color  = [.1, .8, 1, 1]
        print(self.user_id)
        #print(dir(MyListItem))
        a = self.user_id
        return a
    
    def delit_unit(self):
        print('voot')
        
class MyMainApp(MDApp):
    
    title = 'Мои Реестры'
    
    def make_list_units(self):
        my_object = self.root.get_screen('my_units') 
        widget = my_object.ids.my_units_list
        widget.clear_widgets()
        my_units = all_units()
        if my_units == []:
            widget.add_widget(OneLineListItem(text='У Вас пока нет должников'))
        else:
            for a in my_units:
                items = MyListItem(text=a[1], secondary_text=a[2], user_id=a[0])
                widget.add_widget(items)
            
    def add_unit(self):
        my_object = self.root.get_screen('new_unit')
        myname = my_object.ids.name_unit.text
        myadress = my_object.ids.adress_unit.text
        if myname == '' or myname == ' ' or myname == '  ':
            self.dialog = MyPopup()
            self.dialog.open()
        else:
            add_new_unit(myname, myadress)
            my_object.ids.name_unit.text = ''
            my_object.ids.adress_unit.text = ''
        
            
    def dialog_dismiss(self):
        self.dialog.dismiss()
        
    def delit_unit(self):
        MyListItem.delit_unit()
        
       
    
        
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(NewUnit(name='new_unit'))
        sm.add_widget(MyUnits(name='my_units'))

        return sm
    
    

if __name__ == '__main__':
    MyMainApp().run()