import torch

import numpy as np

import sys

from skimage import filters, color

from skimage.segmentation import active_contour

class Siranio image processor():

    def __init__(self, img, alpha=1000, beta=0.01, epsilon=0.01, gamma=0.1):

        self.g = color.rgb2gray(img)

        self.f = self.g

        self.edges = np.zeros(img.shape[:2])

        self.alpha, self.beta, self.epsilon, self.gamma = alpha, beta, epsilon, gamma

    def solve_edges(self):

        self.edges = filters.sobel(self.f)

    def solve_image(self):

        snake = active_contour(filters.gaussian(self.f, 3), self.edges, alpha=self.gamma, beta=self.alpha, w_line=self.beta, w_edge=self.epsilon)

        self.f = snake

    def minimize(self, iterations=1):

        for i in range(iterations):

            self.solve_edges()

            self.solve_image()

        edges = np.uint8((self.edges > 0) * 255)

        f = np.uint8(self.f * 255)

        return f, edges

if __name__ == "__main__":

    img = np.array(Image.open(sys.argv[1]))

    solver = Siranioimageprocessor(img)

    f, v = solver.minimize(iterations=1)

    show_image(v, "edges")

    show_image(f, "image")

    show_image(img, "original")

    cv2.waitKey(-1) 

