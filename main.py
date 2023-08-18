
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.cols = 1
        self.add_widget(Label(text="SmileApp!"))
       # self.cam = Camera(play = True, resolution=(640,480))
       # self.add_widget(self.cam)

        self.img1 = Image()
        self.add_widget(self.img1)
        self.capture = cv2.VideoCapture(0)
        #cv2.namedWindow("CV2 image")
        Clock.schedule_interval(self.update, 1.0/33.0)

        self.submit = Button(text="Check your smile!", font_size=40)
        self.add_widget(self.submit)
        self.check = Label(text="Authentic!")
        self.add_widget(self.check)


    def update(self, dt):
        ret, frame = self.capture.read()
       # cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1





class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
