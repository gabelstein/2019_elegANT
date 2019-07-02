import pygame
import numpy as np
from .view_element import ViewElement


class MiniMap(ViewElement):
    def __init__(self, view, identifier, x, y, width, height, elements=[]):
        super(MiniMap, self).__init__(view, identifier, x, y, width, height)
        self.z_index = 20
        self.elements = elements
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
        if len(self.elements) > 0:
            positions, factor = self._get_minimap_positions()
            for i, element in enumerate(self.elements):
                element.x = positions[i][0]
                element.y = positions[i][1]

                element.width = element.width * 0.1
                element.height = element.height * 0.1

                element.draw()

    def _get_minimap_positions(self):
        positions = np.array([[element.x, element.y] for element in self.elements])

        x_min, y_min = np.min(positions, axis=0)
        x_max, y_max = np.max(positions, axis=0)

        x_span = x_max - x_min
        y_span = y_max - y_min

        #set minima to 0
        positions = positions - [x_min, y_min]

        #scale positions
        factor = np.min([self.width/x_span, self.height/y_span])
        positions = positions * factor

        #set positions to fit minimap
        positions = positions + [self.x, self.y]

        return positions, factor



