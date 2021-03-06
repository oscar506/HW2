# Roaming-Ralph was modified to remove collision part.

#Team: Bruno Recillas // Oscar Ramirez // Garret Jackson // Saul Castro // Steven Hewitt

import direct.directbase.DirectStart
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.gui.DirectGui import *

SPEED = 0.5
login_text = "Login/Register"
bk_text = "This is my Demo"
textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95), 
scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

 

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1), pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1), pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

#login/registration GUI    

#RIGHT HERE IS WHERE THE CONFIRMATION FOR REGISTER WOULD BE  
def confirmRegister():
    bk_text = "Registration Complete"
    textObject.setText(bk_text)
    w = World()
    
    
    
#RIGHT HERE IS WHERE THE CONFIRMATION FOR LOGIN WOULD BE    
def confirmLogin():
    bk_text = "Login Complete"
    textObject.setText(bk_text)
    w = World()


#login Screen
def setLogin():
    loginFrame = DirectFrame(frameColor=(1, 0, 0, 1),frameSize=(-0.5, 0.5, -0.5, 0.5), pos=(1, 0, 0.5) )
    
    bk_text = "Login"
    textObject.setText(bk_text)
    
    emailBox = DirectEntry(parent=loginFrame, text = "",scale = .05,pos=(-0.35,0,.25),numLines= 1)
    emailLabel = DirectLabel(parent=loginFrame, text="Email: ",scale=0.05,
                             pos=(-0.35,0,.32))
    passwordBox = DirectEntry(parent=loginFrame, text = "",scale = .05,pos=(-0.35,0,.12))
    passwordLabel = DirectLabel(parent=loginFrame,text="Password: ",scale=0.05,
                                                         pos=(-0.30,0,.19))
        
    loginButton = DirectButton(parent=loginFrame, text="login",scale=0.09,command=confirmLogin,pos=(0.1,0,-.25))
  

#registration Screen 
def setRegister():
    registerFrame = DirectFrame(frameColor=(0, 0, 0.2, 1),frameSize=(-0.5, 0.5, -0.5, 0.5), pos=(1, 0, 0.5) )
    
    bk_text = "Register"
    textObject.setText(bk_text)

    emailBox = DirectEntry(parent=registerFrame, text = "",scale = .05,pos=(-0.35,0,.25),numLines= 1)
    emailLabel = DirectLabel(parent=registerFrame,text="Email: ",scale=0.05,
                             pos=(-0.35,0,.32))
    passwordBox = DirectEntry(parent=registerFrame, text = "",scale = .05,pos=(-0.35,0,.12))
    passwordLabel = DirectLabel(parent=registerFrame,text="Password: ",scale=0.05,
                                                      pos=(-0.30,0,.19))
    confirmPass = DirectEntry(parent=registerFrame, text = "",scale = .05,pos=(-0.35,0,-0.02))
    confierPass = DirectLabel(parent=registerFrame,text="confirm Password: ",scale=0.05,
                                pos=(-0.20,0,0.05))
    registerButton = DirectButton(parent=registerFrame, text="register",scale=0.09,command=confirmRegister,pos=(0.1,0,-.25))

#first screen you see that asks if user wants to login or register
def firstScreen():
    frame = DirectFrame(frameColor=(0, 1, 0, 1),frameSize=(-0.45, 0.45, -0.2, 0.3), pos=(0, 0, 0) )
    #add button
    button_1 = DirectButton(parent=frame, text="login",scale=0.09,command=setLogin,pos=(-.2,0,0))
    #add button
    button_1 = DirectButton(parent=frame, text="register",scale=0.09,command=setRegister,pos=(0.2,0,0))
    #add Label
    label_1 = DirectLabel(parent=frame,text="What would you like to do?",scale=0.07,
                          pos=(0,0,.2))

class World(DirectObject):
    firstScreen()

    def __init__(self):

        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        base.win.setClearColor(Vec4(0,0,0,1))

        # Post the instructions

        self.title = addTitle("HW2: Roaming Ralph Modified (Walking on the Moon)")
        self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        self.inst2 = addInstructions(0.90, "[A]: Rotate Ralph Left")
        self.inst3 = addInstructions(0.85, "[D]: Rotate Ralph Right")
        self.inst4 = addInstructions(0.80, "[W]: Run Ralph Forward")
        self.inst6 = addInstructions(0.70, "[Left Arrow]: Rotate Camera Left")
        self.inst7 = addInstructions(0.65, "[Right Arrow]: Rotate Camera Right")

        # Set up the environment
        #
        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(100,100,1)
        self.moon_tex = loader.loadTexture("models/moon_1k_tex.jpg")
        self.environ.setTexture(self.moon_tex, 1)

        # Create the main character, Ralph

        self.ralph = Actor("models/ralph", {"run":"models/ralph-run", "walk":"models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(.2)
        self.ralph.setPos(0,0,0)

        #creates Earth
        self.earth = Actor("models/planet_sphere.egg.pz")
        self.earth.reparentTo(render)
        self.earth.setScale(6.0)
        self.earth.setPos(40,25,6)
        self.earth_texture = loader.loadTexture("models/earth_1k_tex.jpg")
        self.earth.setTexture(self.earth_texture)

        #creates Mercury
        self.mercury = Actor("models/planet_sphere.egg.pz")
        self.mercury.reparentTo(render)
        self.mercury.setScale(2.0)
        self.mercury.setPos(-40,-25,2)
        self.mercury_texture = loader.loadTexture("models/mercury_1k_tex.jpg")
        self.mercury.setTexture(self.mercury_texture)

        #creates Venus
        self.venus = Actor("models/planet_sphere.egg.pz")
        self.venus.reparentTo(render)
        self.venus.setScale(4.0)
        self.venus.setPos(40,-30,4)
        self.venus_texture = loader.loadTexture("models/venus_1k_tex.jpg")
        self.venus.setTexture(self.venus_texture)

        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        self.accept("a", self.setKey, ["left",1])
        self.accept("d", self.setKey, ["right",1])
        self.accept("w", self.setKey, ["forward",1])
        self.accept("arrow_left", self.setKey, ["cam-left",1])
        self.accept("arrow_right", self.setKey, ["cam-right",1])
        self.accept("a-up", self.setKey, ["left",0])
        self.accept("d-up", self.setKey, ["right",0])
        self.accept("w-up", self.setKey, ["forward",0])
        self.accept("arrow_left-up", self.setKey, ["cam-left",0])
        self.accept("arrow_right-up", self.setKey, ["cam-right",0])

        taskMgr.add(self.move,"moveTask")

        # Game state variables
        self.isMoving = False

        # Set up the camera

        base.disableMouse()
        base.camera.setPos(self.ralph.getX(),self.ralph.getY()+10,2)


        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value


    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):

        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.

        base.camera.lookAt(self.ralph)
        if (self.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.ralph.getPos()

        # If a move-key is pressed, move ralph in the specified direction.

        if (self.keyMap["left"]!=0):
            self.ralph.setH(self.ralph.getH() + 300 * globalClock.getDt())
        if (self.keyMap["right"]!=0):
            self.ralph.setH(self.ralph.getH() - 300 * globalClock.getDt())
        if (self.keyMap["forward"]!=0):
            self.ralph.setY(self.ralph, -25 * globalClock.getDt())

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.ralph.stop()
                self.ralph.pose("walk",5)
                self.isMoving = False

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.ralph.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0


        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.

        self.floater.setPos(self.ralph.getPos())
        self.floater.setZ(self.ralph.getZ() + 2.0)
        base.camera.lookAt(self.floater)

        return task.cont


 


firstScreen()
base.run()