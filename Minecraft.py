# imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# coding
block_count = 1
app = Ursina()
text = Text()
def update():
    global block_count
    if held_keys["1"]: block_count = 1
    if held_keys["2"]: block_count = 2
    if held_keys["3"]: block_count = 3
    if held_keys["4"]: block_count = 4

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), color=color.rgb(0, 255, 100), white=color.rgb(255, 255, 255)):
        super().__init__(
            parent=scene,
            model="cube",
            color=color,
            position=position,
            origin=(0, 50.5, 0),
            highligh_color=white
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if block_count == 1:
                    vox = Voxel(position=self.position + mouse.normal, color=color.gray)
                    print("Rock Block")
                if block_count == 2:
                    vox = Voxel(position=self.position + mouse.normal, color=color.blue)
                    print("I don't know block")
                if block_count == 3:
                    vox = Voxel(position=self.position + mouse.normal, color=color.cyan)
                    print("Sky Block?")
                if block_count == 4:
                    vox = Voxel(position=self.position + mouse.normal, color=color.brown)
                    print("Dirt block")
            if key == "right mouse down":
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            color=color.rgb(0, 100, 255),
            scale = 150,
            double_sided = True
        )

player = FirstPersonController()
sky = Sky()

for x in range(20):
    for y in range(3):
        for z in range(20):
            vox = Voxel(position=(x, y, z))

app.run()