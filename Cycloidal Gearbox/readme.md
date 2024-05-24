# Basically:
This code is calculating coordinates of densely packed points, spanning over a single teeth of cycloidal geometry(with two extra points on both sides for overlapping, so that the result is an area enclosing loop),
<br>the fit_spine function fits a spline on those points.
<br> Then the spline is circularly patterned around the center.
<br> Finally the resulting area, if any, is extruded as a new component.

### ALTERNATIVE EQUATION: Derived Using Polar Coordinates
```
def x_coordinate(R,r,s,theta):
    return (R+s*r)*(math.cos(theta))-(s*r*math.sin(theta*((R/r)+1)))
def y_coordinate(R,r,s,theta):
    return (R+s*r)*(math.sin(theta))-(s*r*math.cos(theta*((R/r)+1)))

def points_generator(C,R,N,E, num_points=1000):
        spline_points = []
        angular_resolution = (2*math.pi)/num_points
        i = 0
        while(i<2*(math.pi)):
            print(i)
            i+=angular_resolution
            spline_points.append(adsk.core.Point3D.create(x_coordinate(C,R,N,E,i), y_coordinate(C,R,N,E,i), 0))
        return spline_points
```

### Section generator function:
Instead of generating thousands of points between 0 to 2pi.<br>
Just generate hundreds of points between 0 to alpha.
    Where alpha = angle subtended by a single teeth of the cycloid.<br>
But instead of one section, sketch one extra point to the left and also to the right 
    This will allow circular pattern to create area enclosing geometry(two successive sections will join).<br>
This will make the same geometry much quicker because the number of computations requried for spline fitting 
    on n points scales with n^3.<br>
And here if we break down the bigger problem into 150th of the original(when making 150 teeth) it'll take only 1/(150^3)th of the original time!<br>

### Fit Spline function:
Previously we were generating the points on the entire cycloid and we had to manually close the resulting spline by the following piece of code:
```
    # Extend the spline to join the first and last points
    spline.isClosed = True
```