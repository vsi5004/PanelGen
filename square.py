import drawsvg as draw
from panel import Panel


class Square(Panel):
    def __init__(self, side_len, bite, stitches, stitch_length, hole_diameter) -> None:
        sides = [side_len, side_len, side_len, side_len]
        self.width = side_len
        self.cols = 3
        super().__init__(side_len, sides, bite, stitches, stitch_length, hole_diameter)

    def render(self, rows: int = 2) -> draw.Group:
        g_squares = draw.Group()
        g_outlines = draw.Group()
        full_width = self.side_len*self.cols
        full_height = self.side_len*rows
        g_outlines.append(draw.Line(0,0,full_width,0))
        for i in range(rows):
            g_squares.append(draw.Use(self.draw_row(), 0, self.width*i))
            bottom_line_y = self.side_len*(i+1)
            g_outlines.append(draw.Line(0,bottom_line_y,full_width,bottom_line_y))

        g_outlines.append(draw.Line(0,0,0, full_height))
        for i in range(self.cols):
            right_line_x = self.side_len*(i+1)
            g_outlines.append(draw.Line(right_line_x,0,right_line_x, full_height))
        g_squares.append(draw.Use(g_outlines,-self.width/2,-self.width/2))
        return g_squares

    def draw_single(self) -> draw.Group:
        coords = self.gen_coord_list()
        square = draw.Lines(
            coords[0],
            coords[1],
            coords[2],
            coords[3],
            coords[4],
            coords[5],
            coords[6],
            coords[7],
            close="true",
        )

        g_square = self.draw_stitches()
        #g_square.append(draw.Use(square, -self.rotate_point[0], -self.rotate_point[1]))

        return g_square

    def draw_row(self) -> draw.Group:
        g_row = draw.Group()
        for i in range(self.cols):
            g_row.append(draw.Use(self.draw_single(), (self.width) * i, 0))
        
        return g_row
