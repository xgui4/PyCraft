from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController
    

app = Ursina()
player = FirstPersonController()
Sky()

boxes = [] 
for i in range(30):
    for j in range(30):
        box = Button(color=color.white, model='cube',position=(j, 0, i),
                    texture='stone.png', parent=scene, origin_y=0.5)
        boxes.append(box)
        
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal, 
                            texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)
            if key == 'middle mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal, 
                    texture='stone.png', parent=scene, origin_y=0.5)
                boxes.append(new)
                    
app.run()
