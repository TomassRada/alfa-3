from controller import Controller
from model import Model
from view import View


if __name__ == "__main__":
    model = Model()
    controller = Controller()
    view = View(controller)
    view.run()