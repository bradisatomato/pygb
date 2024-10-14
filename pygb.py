from pyboy import PyBoy
from keyboard import on_press_key
from flask import Flask, render_template, request
from webbrowser import open
from os import listdir, mkdir
from os.path import isfile, join, exists
if not exists("./games/"):
    mkdir("games")
webinterface = Flask(__name__)
@webinterface.route("/")
def webindex():
    return render_template("index.html")
@webinterface.route("/getgames")
def webgetgames():
    return [f for f in listdir("./games") if isfile(join("./games", f))]
@webinterface.route("/launch", methods=["POST"])
def weblaunch():
    gameboy(f"./games/{request.data.decode()}")
    return ""
def gameboy(rom: str):
    game = PyBoy(rom)
    on_press_key("a", lambda _:game.button("a"))
    on_press_key("b", lambda _:game.button("b"))
    on_press_key("z", lambda _:game.button("start"))
    on_press_key("x", lambda _:game.button("select"))
    on_press_key("left", lambda _:game.button("left"))
    on_press_key("right", lambda _:game.button("right"))
    on_press_key("up", lambda _:game.button("up"))
    on_press_key("down", lambda _:game.button("down"))
    while game.tick():
        pass
    game.stop()
open("http://127.0.0.1:6060")
webinterface.run(port=6060)