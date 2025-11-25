

class Object:
    obj_id = 0
    def __init__(self,x=0,y=0,mass=0,radius=0):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = mass
        self.radius = radius
        self.color = (255, 255, 255)
        self.obj_type = "circle"

        self.obj_id += 1
    def update_velocity(self):
        self.x = self.vx

class Engine:
    def __init__(self):
        self.objects = []
    def create_obj(self):
        self.objects.append(Object(0,0,100,10))
    def update(self,inputs):
        for obj in self.objects:
            obj.vx += (inputs["a"] + inputs["d"])*2
            obj.vy += (inputs["w"] + inputs["s"])*2
