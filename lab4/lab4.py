import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Draw the water
def draw_water():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3.5, 0, arcade.color.BLEU_DE_FRANCE)

boat = [0, 0]
# Draw the boat
def draw_boat(x, y):
    arcade.draw_polygon_filled([
        [400 + x , 130 + y], [420 + x, 100 + y], [470 + x, 100 + y],
        [490 + x, 130 + y]], arcade.color.COFFEE
    )
    arcade.draw_line(445 + x, 130 + y, 445 + x, 190 + y, 
    arcade.color.BLACK_OLIVE
    )
    arcade.draw_arc_filled(445 + x, 135 + y, 35, 55, arcade.color.BABY_POWDER, 0, 90, 0, 128)

# Draw the first building on the left
def draw_left_building():
    arcade.draw_rectangle_filled(120, 450, 150, 500, arcade.color.CHARCOAL)

# windows left building
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
def draw_second_building():
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
def draw_first_bird():
    arcade.draw_arc_outline(500, 500, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(540, 500, 20, 20, arcade.color.BLACK, 90, 180)

def draw_second_bird():
    arcade.draw_arc_outline(550, 600, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(590, 600, 20, 20, arcade.color.BLACK, 90, 180)

def draw_third_bird():
    arcade.draw_arc_outline(620, 550, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(660, 550, 20, 20, arcade.color.BLACK, 90, 180)


def on_draw(delta_time):
    arcade.start_render()

    draw_water()
    x, y = boat
    draw_boat(x, y)
    x += 1
    boat[0] = x
    draw_left_building()
    draw_second_building()
    draw_first_bird()
    draw_second_bird()
    draw_third_bird()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.COLUMBIA_BLUE)

    # Draw a sun in the right corner
    arcade.draw_arc_filled(700, 700, 100, 100, arcade.color.CHROME_YELLOW, 180, 270)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()