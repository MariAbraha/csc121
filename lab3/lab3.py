import arcade

arcade.open_window(700, 700, "Drawing")

# Set the background color
arcade.set_background_color(arcade.color.COLUMBIA_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the water
arcade.draw_lrtb_rectangle_filled(0, 700, 200, 0, arcade.color.BLEU_DE_FRANCE)

# Draw the boat
arcade.draw_polygon_filled([[400, 130], [420, 100], [470, 100], [490, 130]], arcade.color.COFFEE)
arcade.draw_line(445, 130, 445, 190, arcade.color.BLACK_OLIVE)
arcade.draw_arc_filled(445, 135, 35, 55, arcade.color.BABY_POWDER, 0, 90, 0, 128)

# Draw the first building on the left
arcade.draw_rectangle_filled(120, 450, 150, 500, arcade.color.CHARCOAL)

# Draw windows for building
arcade.draw_rectangle_outline(125, 600, 40, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(125, 450, 60, 40, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(125, 300, 40, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(125, 525, 20, 20, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(125, 375, 20, 20, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(125, 600, 40, 30, arcade.color.EERIE_BLACK, 1)
arcade.draw_rectangle_outline(125, 450, 60, 40, arcade.color.EERIE_BLACK, 1)
arcade.draw_rectangle_outline(125, 300, 40, 30, arcade.color.EERIE_BLACK, 1)
arcade.draw_rectangle_outline(125, 525, 20, 20, arcade.color.EERIE_BLACK, 1)
arcade.draw_rectangle_outline(125, 375, 20, 20, arcade.color.EERIE_BLACK, 1)

# Draw the second building
arcade.draw_rectangle_filled(350, 350, 100, 300, arcade.color.CADET_GREY)

# Draw the roof of the building
arcade.draw_triangle_filled(300, 500, 350, 550, 400, 500, arcade.color.CADET_GREY)

# Draw the windows
arcade.draw_rectangle_outline(350, 450, 60, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(350, 400, 60, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(350, 350, 60, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(350, 300, 60, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(350, 250, 60, 30, arcade.color.BUBBLES, 3)
arcade.draw_rectangle_outline(350, 450, 60, 30, arcade.color.BLACK, 1)
arcade.draw_rectangle_outline(350, 400, 60, 30, arcade.color.BLACK, 1)
arcade.draw_rectangle_outline(350, 350, 60, 30, arcade.color.BLACK, 1)
arcade.draw_rectangle_outline(350, 300, 60, 30, arcade.color.BLACK, 1)
arcade.draw_rectangle_outline(350, 250, 60, 30, arcade.color.BLACK, 1)

# Draw birds
# first bird
arcade.draw_arc_outline(500, 500, 20, 20, arcade.color.BLACK, 0, 90)
arcade.draw_arc_outline(540, 500, 20, 20, arcade.color.BLACK, 90, 180)

# second bird
arcade.draw_arc_outline(550, 600, 20, 20, arcade.color.BLACK, 0, 90)
arcade.draw_arc_outline(590, 600, 20, 20, arcade.color.BLACK, 90, 180)

# third bird
arcade.draw_arc_outline(620, 550, 20, 20, arcade.color.BLACK, 0, 90)
arcade.draw_arc_outline(660, 550, 20, 20, arcade.color.BLACK, 90, 180)

# Draw a sun in the right corner
arcade.draw_arc_filled(700, 700, 100, 100, arcade.color.CHROME_YELLOW, 180, 270)

arcade.finish_render()

arcade.run()