import math
import drawsvg as draw

from draw_utils import rotate_str
from panel import Panel


class Hexagon(Panel):
    def __init__(
        self, hex_long, hex_short, bite, stitches, stitch_length, hole_diameter
    ) -> None:
        self.short_side_len = hex_short
        sides = [
            hex_long,
            hex_short,
            hex_long,
            hex_short,
            hex_long,
            hex_short,
        ]
        super().__init__(
            hex_long,
            sides,
            bite,
            stitches,
            stitch_length,
            hole_diameter,
            skip_sides=True,
        )

        self.midpoint = self.get_midway_point()
        self.width = self.get_hex_width()

    def get_hex_width(self) -> float:
        p1 = self.vertices[2]
        p2 = self.vertices[3]
        a = p1[1] - p2[1]
        b = p2[0] - p1[0]
        c = a * (p1[0]) + b * (p1[1])
        # ax + by = c or x=(c-by)/a
        x = (c - b * self.midpoint[1]) / a
        return (x - self.midpoint[0]) * 2

    def draw_single(self) -> draw.Group:
        coords = self.gen_coord_list()
        hexagon = draw.Lines(
            coords[0],
            coords[1],
            coords[2],
            coords[3],
            coords[4],
            coords[5],
            coords[6],
            coords[7],
            coords[8],
            coords[9],
            coords[10],
            coords[11],
            close="true",
        )

        g_hexagon = self.draw_stitches()
        g_hexagon.append(
            draw.Use(hexagon, -self.rotate_point[0], -self.rotate_point[1])
        )

        return g_hexagon

    def draw_row(self) -> draw.Group:
        g_pair = draw.Group()
        for i in range(2):
            g_pair.append(
                draw.Use(
                    self.draw_single(),
                    self.width / 2,
                    0,
                    transform=rotate_str(
                        180 * i, 0, (self.midpoint[1] - self.rotate_point[1])
                    ),
                )
            )

        g_row = draw.Group()
        for i in range(2):
            g_row.append(draw.Use(g_pair, (self.width) * 2 * i, 0))

        return g_row

    def render(self, rows: int = 2) -> draw.Group:
        g_hexes = draw.Group()
        for i in range(rows):
            g_hexes.append(
                draw.Use(self.draw_row(), 0, self.midpoint[1] * 2 * i + 2 * i)
            )

        return g_hexes
