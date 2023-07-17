import drawsvg as draw
from draw_utils import rotate_str
from hexagon import Hexagon
from pentagon import Pentagon
from square import Square

pent_long = 33
pent_rows = 3
square_long = 49
square_rows = 2
hex_long = 48
hex_short = 12
hex_rows = 2
bite = 5
stitches = 0
stitch_length = 25
hole_diameter = 0.4

square = Square(square_long, bite, stitches, stitch_length, hole_diameter)
hex = Hexagon(hex_long, hex_short, bite, stitches, stitch_length, hole_diameter)
pent = Pentagon(pent_long, bite, stitches, stitch_length, hole_diameter)

d = draw.Drawing(350, 300, origin="center")
d.set_pixel_scale(3.78)

d.append(draw.Use(pent.render(pent_rows), -pent.width, -pent_rows*pent.midpoint[1], stroke="black", fill="none", stroke_width=0.5))
#d.append(draw.Use(square.render(rows=square_rows), 0, 0, stroke="black", fill="none", stroke_width=0.5))

d.save_svg("hexes.svg")  # Save to file
