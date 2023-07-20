# panelgen

A simple python script that generates a set of panels (with stitch holes) for 12, 14, or 32 panel freestyle footbags / hackysacks and saves it as an SVG.
The SVG is optimized for laser cutting panels - GCode can be generated using a tool like LaserWeb.
The following parameters are editable at the top of main.py:
 - `pent_long` (mm): the length of one side of a pentagon panel
 - `pent_rows`: the number of rows of 4 pentagons generated
 - `square_long` (mm): the length of one side of a square panel
 - `square_rows`: the numnber of rows of 3 squares generated
 - `hex_long` (mm): the length of the long side of a hexagon panel
 - `hex_short` (mm): the length of a short side of a hexagon panel
 - `hex_rows`: the number of rows of 4 hexagons generated
 - `bite` (mm): the distance between the edge of the panel and the stitch hole line
 - `stitches`: the number of stitches per side
 - `stitch_length` (mm): the length of each stitch
 - `hole_diameter` (mm): the diameter of the stitch hole (for laser cutting)
