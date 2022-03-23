from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs= []

    def create_herd(self):
        for dinosaurs in Dinosaur(None):
            self.dinosaurs.append(Dinosaur(None))