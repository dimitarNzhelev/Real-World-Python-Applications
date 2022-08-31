from base64 import decode
from datetime import datetime
import json, glob, random
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
            if username in users and users[username]['password'] == password:
                self.manager.current = 'login_success'
            else:
                self.ids.login_wrong.text = 'Wrong username or password!'

    def sing_up(self):
        self.manager.current = 'singup_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def get_quote(self, emotion):
        emotion = emotion.lower()
        avaliable_emotions = glob.glob('Quotes/*txt')

        avaliable_emotions = [Path(filename).stem for filename in 
                                            avaliable_emotions]
        
        if emotion in avaliable_emotions:
            with open(f'Quotes/{emotion}.txt', encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote_output.text = random.choice(quotes)
        else:
            self.ids.quote_output.text = 'Try a different feeling'

class RootWidget(ScreenManager):
    pass

class SingUpScreen(Screen):
    
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        
        users[username] = {'username': username, 'password': password,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", "w") as file:
            json.dump(users,file)

        self.manager.current = "singup_success"

class SingUpScreenSuccess(Screen):
    def success(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()