import numpy as N
import pylab as P

dx = (0.663, 0.007)  #X start position, X width
dy = (-0.191, 0.007) #Y start position, Y width
v = N.zeros((1024,1024), "uint8")  #The color matrix

#Create the const. matrix and initialize
c = N.zeros((1024,1024), "complex")
c[:].real = N.linspace(dy[0],dy[0]+dy[1],
                       c.shape[0])[:,N.newaxis]
c[:].imag = N.linspace(dx[0],dx[0]+dx[1],
                       c.shape[1])[N.newaxis,:]
z  = c.copy()           # The z function is initialized from c
for it in xrange(256):  # Use 256 colors
    z *= z              # Compute z = z*z
    z += c              # Compute z = z + c
    # Set colors for which z has diverged
    v += (N.abs(z) >= 4)*(v == 0)*it
P.imgshow(v)      # Display the image
P.show()