# "Stopwatch: The Game"
# This game can be played @ the following url
# http://www.codeskulptor.org/#user12_pcFRXwm42U_3.py


import simplegui


# define global variables



# The string variable "time" is the textual time display

time = '0:00.0'

# t is the integar from which the time display will be derived
t = 0

number_of_games= 0
games_won = 0
game_state = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

    
def format(t):
    global time
    milli = t % 10
    sec = (t - milli) / 10
    minutes = sec // 60
    seconds = sec % 60
    if seconds >=10:
        time = str(minutes) + ':' + str(seconds) + '.' +str(milli)
    else:
        time = str(minutes) + ':0' + str(seconds) + '.' +str(milli)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"



def start_button():
    global game_state
    game_state = 1
    timer.start()
    
def stop_button():
    global number_of_games, games_won, game_state
    timer.stop()
    number_of_games = number_of_games+ game_state
    if time[-1] == '0' and game_state:
        games_won = games_won + 1
    game_state = 0
    
def reset_button():
    global t, time, number_of_games, games_won, game_state
    number_of_games = 0
    games_won = 0
    game_state = 0
    timer.stop()
    t = 0
    format(t)

    
    

# define event handler for timer with 0.1 sec interval



def timer_handler():
    global t
    t = t + 1
    format(t)




# define draw handler


def draw(canvas):
    canvas.draw_text(time, (100, 100), 40, "White")
    canvas.draw_text(str(games_won) + '/' + str(number_of_games),
                     (240, 25), 30, "Red")

    
# create frame

frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_canvas_background("Blue")


# register event handlers


timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Reset", reset_button, 100)


# start frame

frame.start()

# Please remember to review the grading rubric
# Test Line