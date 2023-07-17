from abc import abstractmethod
import math
import drawsvg as draw

from draw_utils import rotate_str


class Panel(object):
    def __init__(
        self, side_len, sides, bite, stitches, stitch_length, hole_diameter, skip_sides:bool=False
    ) -> None:
        self.bite = bite
        self.stitches = stitches
        self.stitch_len = stitch_length
        self.hole_dia = hole_diameter
        self.side_len = side_len
        self.sides = sides
        self.skip_sides = skip_sides
        self.angle = 2 * math.pi / len(sides)
        self.vertices = self.get_vertices()
        self.x_coords, self.y_coords = self.get_xy_coord_lists()
        self.rotate_point = self.get_rotate_point()

    def get_vertices(self) -> list[tuple[float]]:
        vertices = []
        vertices.append((0, 0))

        for i in range(len(self.sides) - 1):
            x = self.sides[i] * math.cos(i * self.angle) + vertices[i][0]
            y = self.sides[i] * math.sin(i * self.angle) + vertices[i][1]
            coord = (x, y)
            vertices.append(coord)
        return vertices

    def get_xy_coord_lists(self) -> tuple[list[float], list[float]]:
        x_coords = []
        y_coords = []
        for x, y in self.vertices:
            x_coords.append(x)
            y_coords.append(y)
        return x_coords, y_coords

    def get_midway_point(self) -> tuple[int, int]:
        x_mid = math.floor((max(self.x_coords) + min(self.x_coords)) / 2)
        y_mid = math.floor((max(self.y_coords) + min(self.y_coords)) / 2)
        return (x_mid, y_mid)
    
    def get_rotate_point(self) -> tuple[int, int]:
        x_rot = math.floor(sum(self.x_coords) / len(self.x_coords))
        y_rot = math.floor(sum(self.y_coords) / len(self.y_coords))
        return (x_rot, y_rot)
    
    def gen_coord_list(self) -> list[float]:
        coords = list()
        for x, y in self.vertices:
            coords.append(x)
            coords.append(y)
        return coords

    def draw_stitch_row(self) -> draw.Group:
        total_holes = self.stitches * 2 + 2 if self.skip_sides else self.stitches*2
        stitch_offset = self.side_len / 2 - (total_holes - 1) * self.stitch_len / 2
        g_stitch_holes = draw.Group()
        for x in range(total_holes):
            g_stitch_holes.append(
                draw.Circle(
                    self.stitch_len * x + stitch_offset,
                    self.bite,
                    self.hole_dia / 2,
                )
            )

        return g_stitch_holes

    def draw_stitches(self) -> draw.Group:
        g_shape = draw.Group()
        if self.stitches > 0:
            g_stitch_holes = self.draw_stitch_row()

            for i in range(len(self.sides)):
                if i%2==1 and self.skip_sides:
                    pass
                else:
                    g_shape.append(
                        draw.Use(
                            g_stitch_holes,
                            -self.rotate_point[0],
                            -self.rotate_point[1],
                            transform=rotate_str(self.angle*180/math.pi*i),
                        )
                    )

        return g_shape

    @abstractmethod
    def render(self, rows: int = 2) -> draw.Group:
        pass

    @abstractmethod
    def draw_single(self) -> draw.Group:
        pass

    @abstractmethod
    def draw_row(self) -> draw.Group:
        pass
