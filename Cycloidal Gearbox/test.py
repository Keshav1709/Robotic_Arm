####### WORKING PERFECTLY ########
# import math

# # Equation of the Cycloidal Contour:
# def x_coordinate(R,r,s,theta):
#     return (R+s*r)*(math.cos(theta))-(s*r*math.sin(theta*((R/r)+1)))
# def y_coordinate(R,r,s,theta):
#     return (R+s*r)*(math.sin(theta))-(s*r*math.cos(theta*((R/r)+1)))

# class Gearbox:
#     def __init__(self,R: float,r: float,s:float):
#         self.R = R
#         self.r = r
#         self.s = s
#         self.spline_points = []
#     def points_generator(self, num_points=1000) -> list:
#         num_points = 1000  # You can adjust this value for more or less points
#         angular_resolution = (2*math.pi)/num_points
#         i = 0
#         while(i<2*(math.pi)):
#             print(i)
#             i+=angular_resolution
#             self.spline_points.append((x_coordinate(self.R,self.r,self.s,i), 
#                                        y_coordinate(self.R,self.r,self.s,i), 
#                                        0))
#         return self.spline_points
        
# gear1 = Gearbox(10,2,3)
# print(gear1.points_generator())
##################################



####################################
import math
# Equation of the Cycloidal Contour:
def x_coordinate(C,R,N,E,theta):
    return (
        +(C*math.cos(theta))
        -(R*math.cos(theta + math.tanh((math.sin((1-N)*theta)) / ((C/(E*N)) - math.cos((1-N)*theta)))))
        -E*math.cos(N*theta))

def y_coordinate(C,R,N,E,theta):
    return (
        -(C*math.sin(theta))
        +(R*math.sin(theta + math.tanh((math.sin((1-N)*theta)) / ((C/(E*N)) - math.cos((1-N)*theta)))))
        +E*math.sin(N*theta))

def points_generator(C,R,N,E, num_points=400):
        spline_points = []
        angular_resolution = (2*math.pi)/num_points
        i = 0
        while(i<2*(math.pi)):
            print(i)
            i+=angular_resolution
            spline_points.append((x_coordinate(C,R,N,E,i), y_coordinate(C,R,N,E,i), 0))
        return spline_points

circle_points = points_generator(40,1.3,50,0.66)
for i in circle_points:
     print(i)
####################################



################ Previous Version ################

import adsk.core, adsk.fusion, adsk.cam, traceback
import math

# Equation of the Cycloidal Contour:
def x_coordinate(C,R,N,E,theta):
    return (
        +(C*math.cos(theta))
        -(R*math.cos(theta + math.tanh((math.sin((1-N)*theta)) / ((C/(E*N)) - math.cos((1-N)*theta)))))
        -E*math.cos(N*theta))

def y_coordinate(C,R,N,E,theta):
    return (
        -(C*math.sin(theta))
        +(R*math.sin(theta + math.tanh((math.sin((1-N)*theta)) / ((C/(E*N)) - math.cos((1-N)*theta)))))
        +E*math.sin(N*theta))

######## ALTERNATIVE EQUATION: Derived Using Polar Coordinates ########
# def x_coordinate(R,r,s,theta):
    # return (R+s*r)*(math.cos(theta))-(s*r*math.sin(theta*((R/r)+1)))
# def y_coordinate(R,r,s,theta):
    # return (R+s*r)*(math.sin(theta))-(s*r*math.cos(theta*((R/r)+1)))

def points_generator(C,R,N,E, num_points=1000):
        spline_points = []
        angular_resolution = (2*math.pi)/num_points
        i = 0
        while(i<2*(math.pi)):
            print(i)
            i+=angular_resolution
            spline_points.append(adsk.core.Point3D.create(x_coordinate(C,R,N,E,i), y_coordinate(C,R,N,E,i), 0))
        return spline_points

def fit_spline(points):
    app = adsk.core.Application.get()
    design = app.activeProduct
    root = design.activeComponent

    sketches = root.sketches
    xyPlane = root.xYConstructionPlane
    sketch = sketches.add(xyPlane)

    fitPoints = adsk.core.ObjectCollection.create()
    for point in points:
        fitPoints.add(point)

    spline = sketch.sketchCurves.sketchFittedSplines.add(fitPoints)

    # Extend the spline to join the first and last points
    spline.isClosed = True

def run(context):
    try:
        circle_points = points_generator(4,0.1,50,0.05)
        fit_spline(circle_points)

    except Exception as e:
        ui = None
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        if ui:
            ui.messageBox('Script stopped')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Run the script
if __name__ == "__main__":
    app = adsk.core.Application.get()
    ui = app.userInterface
    ui.messageBox('Run the script by selecting "Run" from the Add-Ins menu.')


