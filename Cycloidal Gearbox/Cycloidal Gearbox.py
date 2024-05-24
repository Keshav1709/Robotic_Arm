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

def section_generator(C,R,N,E, num_points=250):
    spline_points = []
    n = N-1 # Number of teeth
    alpha = (2*math.pi)/(n) # Angle Subtended by one teeth(in radians)
    angular_resolution = (alpha)/num_points
    i = -2*angular_resolution
    while(i<alpha+(2*angular_resolution)):
        print(i)
        spline_points.append(adsk.core.Point3D.create(x_coordinate(C,R,N,E,i), y_coordinate(C,R,N,E,i), 0))
        i+=angular_resolution
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
    return spline

def run(context):
    try:
        scale = 2 # Will make a disc of radius = 8 cm # Just there to change scale without affecting the teeth geometry

        C = 4 * scale # True radius of the cycloidal disc
        R = 0.05 * scale
        teeth = 151 # Please keep it odd so that you can create even teeth(they'll be symmertrical about bothx and y axis)
        E = 0.02 * scale

        circle_points = section_generator(C, R, teeth+1, E) #151 teeth, odd for easily getting the second center along the x axis.
        spline = fit_spline(circle_points)
        
        # Get the active sketch
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        active_sketch = design.activeSketch

        if not active_sketch:
            ui.messageBox('No active sketch found.')
            return
        
        # # Get the selected entity in the sketch
        # selected_entities = ui.activeSelections

        selected_entity = spline
        if selected_entity.count != 1:
            ui.messageBox('Please select a single sketch entity.')
            return

        # Center point for the circular pattern:
        center_point = adsk.core.Point3D.create(0, 0, 0)

        # Number of instances to be created in the circular pattern:
        num_instances = teeth
        pattern_input = active_sketch.sketch.sketchCurves.sketchCircularPattern.circular_patterns.createInput(spline, center_point, num_instances)

        # Create the circular pattern
        active_sketch.sketch.sketchCurves.sketchCircularPattern.add(pattern_input)

        ui.messageBox('Circular pattern created successfully.')

        # Select the profile enclosed by the circular pattern
        prof = active_sketch.profiles.item(0)  # Assuming the first profile is the enclosed area

        # Create an extrusion
        extrudes = root.features.extrudeFeatures
        ext_input = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define the distance for the extrusion
        distance = adsk.core.ValueInput.createByReal(1)  # Change this value to the desired extrusion depth
        ext_input.setDistanceExtent(False, distance)
        
        # Create the extrusion
        extrudes.add(ext_input)

        ui.messageBox('Extrusion created successfully.')


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

