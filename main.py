from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class Rate(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation="vertical"
        btnBox=BoxLayout()
        btnBox=BoxLayout()
        lbl_title=Label(text="оцени-ка фоточку",font_size=32,halign="center",size_hint=[1,0.1])      
        self.buttons=[]                                                                                         
        self.img=Image(source="photo/images.jpg")
        self.add_widget(lbl_title)
        self.add_widget(self.img)
        for i in range(5):
            btn=Button(text=str(i+1),background_normal="star0.png",color=[0,0,0,0],background_down="star0png")
            self.buttons.append(btn)
            btnBox.add_widget(btn)
            btn.bind(on_press=self.rating)
        self.add_widget(btnBox)
    def rating(self,btn):
        index=int(btn.text)-1
        for i in range(len(self.buttons)):
            if i<=index:
                self.buttons[i].background_normal="star1.png"
                self.buttons[i].background_down="star1png"
            else:
                self.buttons[i].background_normal="star0.png"
                self.buttons[i].background_down="star0png"
class LikeApp(App):
    def build(self):
        self.mainBox=BoxLayout(orientation='vertical')
        rate=Rate()
        self.mainBox.add_widget(rate)
        return self.mainBox
    def like(self,btn):
        print("Крута!")
    def dislike(self,btn):
        print("Фигня!")
LikeApp().run()