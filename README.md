# Siranio-image-processor
This code defines a class AmbrosioTortorelliMinimizer that implements the Ambrosio-Tortorelli functional for image segmentation.

The class has four parameters:

img: the input image to segment

alpha: a parameter controlling the regularization term of the functional (default value is 1000)

beta: a parameter controlling the weight of the line integral term of the functional (default value is 0.01)

epsilon: a parameter controlling the weight of the edge integral term of the functional (default value is 0.01)

gamma: a parameter controlling the weight of the elasticity term of the snake (default value is 0.1)

The class has three methods:

__init__(self, img, alpha=1000, beta=0.01, epsilon=0.01, gamma=0.1): initializes the instance of the class with the input image and the four parameters.

solve_edges(self): applies a Sobel filter to the current image (self.f) to obtain the edges.

solve_image(self): applies an active contour algorithm to the current image (self.f) with the current edges (self.edges) and the four parameters to obtain a new image (self.f).

minimize(self, iterations=1): iteratively applies solve_edges and solve_image a number of iterations times (default is 1) and returns the final image (f) and the edges (edges).

The main block of the code reads an image file from the command line, creates an instance of AmbrosioTortorelliMinimizer with the image, and calls the minimize method to segment the image. The resulting image and edges are shown using a show_image function that is not included in the code snippet. Finally, the script waits for a key press before exiting.
