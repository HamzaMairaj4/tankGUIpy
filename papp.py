# import all necessary libraries
# sudo rm papp2.py
# sudo nano papp2.py
# sudo cat tankClass.py and email to me
from flask import Flask, render_template, request
from tankClass import Tank
# import cv2


# create the tank object
tank = Tank()

# create the flask server
app = Flask(__name__)
# camera = cv2.VideoCapture(0)


# this is the main page, which will just show the html gui
@app.route('/')
def default():
    return render_template('indexvid.html')



# this is the endpoint for the API, it gets a json file of the data from the html page and sets all the data from the 'button' key to a variable
# then, it checks what that button data is, calls the appropriate function, and adds that movement to the log dictionary
@app.route('/moving', methods=['POST'])
def moved():
    data = request.json
    pressed = data.get('button')
    if pressed == "forward":
        tank.forward()
    elif pressed == "go":
        tank.forward()
    elif pressed == "stop":
        tank.stop()
    elif pressed == "left":
        tank.leftturn()
    elif pressed == "right":
        tank.rightturn()
    elif pressed == "backward":
        tank.backward()
    else:
        tank.stop()
    return "Movement Successful"


# runs the program and API server
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4200)