# --- Button A: Learning Mode ---
def on_button_pressed_a():
    # Tell the AI Lens to learn the current object and assign it to ID1
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID1)
    # Display "L1" on the micro:bit LED matrix to confirm learning
    basic.show_string("L1")
    # Set headlights to Blue to indicate the robot is in learning mode
    TPBot.headlight_color(0x0000ff)

input.on_button_pressed(Button.A, on_button_pressed_a)

# --- Button B: Manual Stop/Reset ---
def on_button_pressed_b():
    global isTracking
    isTracking = False # Stop the tracking logic
    TPBot.headlight_color(0x00ffff) # Cyan headlights
    basic.show_string("SUI") # Custom status message
    # Show a custom pattern on the LED grid
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . # #
        # # . . #
        . # # # .
        """)

input.on_button_pressed(Button.B, on_button_pressed_b)

# --- Logo: Clear Memory and Stop ---
def on_logo_pressed():
    global isTracking
    isTracking = False
    # Wipe the learned objects from the AI Lens memory
    PlanetX_AILens.clearlearn_object()
    TPBot.stop_car()
    TPBot.headlight_color(0x000000) # Turn off headlights
    basic.show_icon(IconNames.NO)
    basic.pause(500)
    basic.show_icon(IconNames.SAD)

input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# --- Initialization (Runs once at startup) ---
isTracking = False
PlanetX_AILens.init_module() # Wake up the AI Lens
# Set AI Lens to "Things" recognition mode
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.THINGS)
TPBot.stop_car()
TPBot.headlight_color(0x000000)
basic.show_icon(IconNames.SAD)

# --- Main Loop: Logic Controller ---
def on_forever():
    global isTracking
    
    # Mode 1: Searching for the learned object
    if not (isTracking):
        PlanetX_AILens.camera_image() # Refresh the camera feed
        # Check if the lens sees the object we labeled as ID1
        if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID1):
            isTracking = True # Object found! Switch to tracking mode
            basic.show_icon(IconNames.HAPPY)
        
        # Red headlights while searching
        TPBot.headlight_color(0xff0000)
    
    # Mode 2: Line Tracking (Only active after object is recognized)
    else:
        # Case: Both sensors on the line -> Move forward
        if TPBot.track_line(TPBot.TrackingState.L_R_LINE):
            TPBot.set_wheels(30, 30)
        
        # Case: Left sensor on line, right sensor off -> Turn left
        elif TPBot.track_line(TPBot.TrackingState.L_LINE_R_UNLINE):
            TPBot.set_wheels(0, 40)
        
        # Case: Right sensor on line, left sensor off -> Turn right
        elif TPBot.track_line(TPBot.TrackingState.L_UNLINE_R_LINE):
            TPBot.set_wheels(40, 0)
        
        # Case: Off the line entirely -> Stop and reset to searching
        else:
            TPBot.stop_car()
            isTracking = False
            basic.show_icon(IconNames.SAD)

basic.forever(on_forever)
