import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

player = {
    "score": 0,
    "power": 1
}
def read_data():
    global player
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player = json.load(file)
    except:
        print("невдача((((((")

def save_data():
    global player
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player, file, indent=4, ensure_ascii=True)
    except:
        print("невдача((((((")

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def click(self):
        self.ids.ball.size_hint = (0.5, 0.5)
        read_data()
        player["score"] += player["power"]
        self.ids.score_lbl.text = "рахунок: " + str(player["score"])
        save_data()

    def switch_to_shop(self):
        self.manager.current = "shop"

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class ShopScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def buy(self, price, power):
        read_data()
        if price <= player["score"]:
            player["score"] -= price
            player["power"] += power
            save_data()

class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ShopScreen(name="shop"))
        return sm

app = ClickerApp()
app.run()