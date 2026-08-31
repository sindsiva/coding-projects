###################################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Student Names: Jiayi (Skyler) Du, Sindhu Sivasankar, Yang Xiu
# Student Numbers: 1009796419, 1009813686, 1011820077
# Supervisor: Dr. Maher Elshakankiri
#
# Final
# Purpose: This program simulates and animates a soccer match.
# Date Created: November 15, 2025
# Date Modified: December 4, 2025
###################################################################

# import modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import os
import pygame
import sys

################################################################################
# GLOBAL VARIABLES AND CONFIGURATION
################################################################################

# animation gifs mapping
animationGIFS = {
    "dribble_success": "Final_dribblesuccessGIF_DuSivasankarXiu.gif",
    "dribble_fail": "Final_dribblefailGIF_DuSivasankarXiu.gif",
    "pass_success": "Final_passsuccessGIF_DuSivasankarXiu.gif",
    "pass_fail": "Final_passfailGIF_DuSivasankarXiu.gif",
    "shoot_success": "Final_shootsuccessGIF_DuSivasankarXiu.gif",
    "shoot_fail": "Final_shootfailGIF_DuSivasankarXiu.gif"
}

# action buttons
dribbleBtn = None
passBtn = None
shootBtn = None
defendBtn = None

# commentary text box content
commentaryText = None

# joining python file with image files
folder = "FinalProject11"

pyfile = os.path.join(folder, "Final.py")
mainLogo = os.path.join(folder, "Final_mainIMG_DuSivasankarXiu.png")

# create window
window = Tk()
window.title("Soccer Game")
window.attributes('-fullscreen', True)

# define font variable
dyslexicStatus = BooleanVar(value=False)

# team list
teamList = ["Liverpool", "Manchester City", "Arsenal", "Chelsea",
            "Manchester United", "AC Milan", "Inter Milan", "Juventus",
            "Bayern Munich", "Dortmund", "Real Madrid", "Barcelona",
            "Atletico de Madrid", "Paris Saint-Germain", "Toronto FC"]

# game state variables
gameFrame = None
canvas = None
userPlayers = None
opponentPlayers = None
timerLabel = None
playsLeft = 90
score = {"user": 0, "opponent": 0}
currentPlayer = None
timeLeft = None
questionIndex = [0]
userTeam = None
opponentTeam = None
teamHasBall = None
playerHasBall = None
compAction = None
messageBox = None
scoreLabel = None

# define dictionary of all trivia questions and answers
triviaQuestions = [
{"question": "Which country won the first ever FIFA World Cup in 1930?",
     "options": ["Brazil", "Uruguay", "Germany", "Italy"], 
     "answer": 1},
    {"question": "Which player has won the most FIFA Ballon d’Or awards?",
     "options": ["Maradona", "Messi", "Pelé", "Ronaldo"], 
     "answer": 1},
    {"question": "Which team is known as the “Red Devils”?","options": ["Liverpool", "Crystal Palace", "Manchester United", "Arsenal"],
     "answer": 2},
    {"question": "Which country has won the most World Cups?",
     "options": ["France", "Argentina", "Brazil", "England"],
     "answer": 2},
    {"question": "What was Lionel Messi’s schoolboy team?",
    "options": ["Newell's Old Boys", "River Plate", "Boca Junios","Rosario Central"],
     "answer": 0},
    {"question": "How many laws of Association Football are there?",
     "options": ["17", "18", "19", "20"],
     "answer": 0},
    {"question": "Excluding the goalkeeper, what part of the body cannot touch the ball?",
      "options": ["Head", "Chest", "Arm", "Shoulder"], 
      "answer": 2},
    {"question": "The throw-in. In order to execute a proper throw-in, which conditions must be met by the player who is throwing it in?",
     "options": ["He must be in an upright position.", "His hands, holding the ball, must go all the way behind his head before he throws it. ", "Both feet must be on the ground when he throws it.", "All of the above."], 
     "answer": 3},
    {"question": "If the ball is kicked into the air, a player is allowed to use their hand to knock the ball back down to the ground.",
     "options": ["True", "false"], 
     "answer": 1},
     {"question": "What basic soccer skill is used when the ball goes out of bounds on the sideline?",
     "options": ["Throw in", "Bicycle", "Dribbling", "One Time Pass"], 
     "answer": 0},
    {"question": "It is best to pass with which part of the foot?",
     "options": ["Outside", "Top", "Inside", "Bottom"],
     "answer": 2},
    {"question": "If an offensive player is fouled in the box, the result is a _____ kick.",
     "options": ["Corner", "Direct", "Indirect", "penalty"],
     "answer": 3},
    {"question": "Which player IS allowed to touch the ball with her/his hands?",
     "options": ["The winger", "The goalie", "The sweeper", "The midfielder"],
     "answer": 1},
    {"question": "“Striker” is another name for which player?",
     "options": ["The team captain", "The highest-scoring player", "A forward", "A midfielder"],
     "answer": 2},
    {"question": "What does a yellow card signify?",
     "options": ["A caution", "An indirect free kick", "A time-out", "The need for video replay"],
     "answer": 0},
    {"question": "A soccer team on the field must consist of …","options": ["a goalkeeper, three defenders, and four offensive players", "a goalkeeper, five players on the right half, and five players on the left", "a goalkeeper, three defenders, three midfielders, and four forwards", "It depends; only the goalkeeper is mandatory"],"answer": 3},
    {"question": "How many kick-offs are there in a soccer game?","options": ["One", "Two", "Three", "It depends"],"answer": 3},
    {"question": "In an indirect free kick, the ball must do what before scoring a goal?","options": ["bounce off the goalie's body", "contact a player besides the kicker", "hit the ground once", "Travel more than 20 yards"],"answer": 1},
    {"question": "Who is the all-time leading scorer in the UEFA Champions League?","options": ["Cristiano Ronaldo", "Lionel Messi", "Robert Lewandowski", "Raul"],"answer": 0},
     {"question": "Anfield is the home of which English Premier League club?","options": ["West Ham United", " Manchester City", " Liverpool", " Everton"],"answer": 2},
    {"question": "In which year did the United States hold the FIFA World Cup?","options": ["1994", "1986", "2002", "2010"],"answer": 0},
    {"question": "Which of these players has never played for Manchester United?","options": ["Eric Cantona", " Bobby Charlton", " Ryan Giggs", " Bobby Moore"],"answer": 3},
    {"question": "What is the name of the stadium where FC Barcelona plays its home matches?","options": ["Santiago Bernabeu", " Camp Nou", " Old Trafford", " Allianz Arena"],"answer": 1},
    {"question": "Who holds the record as the youngest player to ever score in a World Cup finals match?","options": ["Pelé", " Diego Maradona", " Lionel Messi", " Michael Owen"],"answer": 0},
    {"question": "How long is a standard soccer field according to FIFA regulations?","options": ["90-100 yards", "110-120 yards", "120-130 yards", "100-110 yards"],"answer": 1},
    {"question": "Which player holds the record for receiving the most red cards in football history?","options": ["Sergio Ramos", " Gerardo Bedoya", " Paolo Maldini", " Cristiano Ronaldo"],"answer": 1},
    {"question": " What is the width of the penalty area in meters?","options": ["5.63 meters", "15.87 meters", "16.02 meters", "16.46 meters"],"answer": 3},
    {"question": "Which nation is often nicknamed “The Samba Kings” in World Cup context?","options": ["Spain", " Brazil", " Argentina", " Germany"],"answer": 1},
    {"question": "Which World Cup edition was the first to feature 32 teams?","options": ["2002", "2006", "2010", "1998"],"answer": 3},
    {"question": "What is the official trophy of the FIFA World Cup called?","options": ["Victory Cup", " FIFA World Cup Trophy", " Golden Cup", " Soccer Globe"],"answer": 1},
    {"question": "Who scored the fastest goal in World Cup history?","options": ["Cristiano", "Pelé", "Hakan Şükür", "Miroslav Klose"],"answer": 2},
    {"question": "Which African nation first qualified for the FIFA World Cup?","options": ["Cameroon", "Nigeria", "Egypt", "Morocco"],"answer": 2},
    {"question": "Which country ended a 24-year wait by winning the World Cup in 2014?","options": ["Spain", "Germany", "France", "Italy"],"answer": 1},
    {"question": "Which nation hosted the first World Cup in Asia?","options": ["Saudi Arabia", "Japan/South Korea in 2002", "Qatar", "China"],"answer": 1},
    {"question": "Who is Italy’s all-time top World Cup goal scorer?","options": ["Roberto Baggio", "Alessandro Del Piero", "Gigi Riva", "Paolo Rossi"],"answer": 2},
    {"question": "What is the fullback’s position?","options": ["Plays the defensive third of the field", "Is the primary scorer", "Defends the goal", "None of the above"],"answer": 0},
    {"question": "What is a soccer field called?","options": ["Court", "Pitch", "Paddock", "Box"],"answer": 1},
    {"question": "What was the fastest goal in World Cup history?","options": ["6.2 seconds", "10.8 seconds", "7 seconds", "18.3 seconds"],"answer": 1},
    {"question": "Which country won the first women’s World Cup?","options": ["United States", " Germany", " Norway", " Sweden"],"answer": 0},
    {"question": "What is the earliest known form of soccer?","options": ["Cuju", "Phaininda", "Episkyros", "Pila"],"answer": 0},
    {"question": "What was the fastest red card ever issued in a game?","options": ["16 seconds", "8 seconds", "4 seconds", "2 seconds"],"answer": 3},
    {"question": "What country was home to the world's first soccer league?","options": ["Scotland", "Brazil", "England", " Mexico"],"answer": 2},
    {"question": "What year were soccer rules codified?","options": ["1963", "1863", "1763", "1663"],"answer": 1},
    {"question": "Who was the youngest player ever named to the Canada National Women's Team?","options": ["Rebecca Quinn", " Kadeisha Buchanan", "Christine Sinclair", "Kara Lang"],"answer": 3},
    {"question": "Who has been named Chelsea's Player of the Year three different times?","options": ["Frank Lampard", "John Terry", "Didier Drogba", "Juan Mata"],"answer": 0},
    {"question": "What is the term for a situation where a player scores three goals in a single game?","options": ["Hat-trick", "Triple Play", "Super Strike", "Score Trio"],"answer": 0},
    {"question": "What is the maximum number of substitutions allowed in a standard soccer match?","options": ["2", "3", "4", "5"],"answer": 1},
    {"question": "What is the maximum number of yellow cards a player can receive before being ejected from a match?","options": ["1", "2", "3", "4"],"answer": 1},
    {"question": "What is the term for the area in front of the goal where the goalkeeper is the only player allowed to use their hands?","options": ["The Box", "The Net Zone", "The Goalie Zone", "The Penalty Area"],"answer": 3},
    {"question": "What is the term for a pass in which a player uses their head to direct the ball to a teammate?","options": ["Header", "Air Pass", "Crown Pass", "Skull Pass"],"answer": 0},
    {"question": "What is the term for a consecutive series of wins in soccer, where a team does not lose or tie any matches?","options": ["Winning streak", "Perfect season", "Undefeated run", "Golden run"],"answer": 0},
    {"question": "Which soccer player is renowned for his exceptional goal-scoring ability and is often referred to as the “Magician of the Ball?","options": ["Diego Maradona", "Lionel Messi", "Eric Cantona", "Frank Lampard"],"answer": 1},
    {"question": "When the ball completely crosses the goal line without a goal being scored by the attacking team, what restart is awarded?","options": ["Throw-in", "Corner kick", "Goal kick", "Indirect free kick"],"answer": 2},
    {"question": "What does the acronym UEFA stand for?","options": ["Universal European Football Agency", "United European Football Alliance", "Union of Elite Football Athletes", "Union of European Football Associations"],"answer": 3},
    {"question": "How many teams compete in the final tournament of the FIFA World Cup?","options": ["24", "28", "36", "32"],"answer": 3},
    {"question": "Which nation became the first to win back-to-back FIFA World Cup titles?","options": ["West Germany", "Italy", "Brazil", "Uruguayv"],"answer": 1},
    {"question": "Which non-European and non-South American team reached the World Cup semi-finals in 2002?","options": ["Cameroon", " South Korea", " Japan", " Morocco"],"answer": 1},
    {"question": "Who sang the official FIFA 2010 World Cup Song?","options": ["Shakira", "Michael Jackson", "Coldplay", "Arlindo Cruz"],"answer": 0},
    {"question": "Offside. If a player is offside, what action does the referee take?","options": ["Awards a direct free kick to the opposing team", "Gives the offending player a yellow card", "Does a drop-ball", "Awards an indirect free kick to the opposing team"],"answer": 0},
    {"question": "Free Kicks. What is the hand signal for an indirect free kick?","options": ["The referee points his/her arm in the direction that the kick is being taken", "The referee raises his/her arm in the air until the kick has been taken and has touched another player", "None listed", "There is no hand signal for an indirect free kick"],"answer": 1},
    {"question": "What is the technical area?","options": ["A designated area off of the field of play where players that have received red cards must stand or sit for the remainder of the game.", "A designated seating area off the field of play where the coach(es) and non-fielded players must sit or stand.", "A designated area off of the field of play where the game officials must sit or stand during halftime, and before the match.", "None of these."],"answer": 1},
    {"question": "The morning before the game, you look in the paper and see the other team's formation. It is a 4-3-3 formation. You can see the weakness in that formation immediately. What is the weakness and what formation would best exploit that weakness?","options": ["Too many up front, 2-5-3", "No wide players, 4-4-2", "Too much emphasis on defence, 4-3-3", "Too many in defence, 5-3-2"],"answer": 1},
    {"question": "The game has kicked off! Your ploy of playing with the wide players (4-4-2) against their 4-3-3 formation seems to be working, as you create chance after chance; but your team just can't seem to convert their opportunities into goals. You go close to scoring a few times. What do you do?","options": ["Leave the team as it is", "Change the formation to a more defensive style, as you obviously can't score", "Change both the strikers, they are obviously ineffective", "Play another striker up front"],"answer": 0},
    {"question": "The second spell of extra time ends. You have to pick your penalty shoot out teams. You have the five best players at taking penalties to choose from. What is the best order for them to kick?","options": ["3rd, 1st, 5th, 4th, 2nd ", "5th, 4th, 3rd, 2nd, 1st", "1st, 2nd, 3rd, 4th, 5th", "Who knows "],"answer": 0},
    {"question": "You're refereeing a game. Team A is playing against Team B. It is a nice day out and the park allows dogs, so a fan of Team A has brought their golden retriever. All of a sudden, the dog runs on to the field, steals the ball from a player, and moves it down the field until the ball goes out on the touchline. When the pooch has been removed, how do you restart the game?","options": ["Indirect free kick for Team", "Direct free kick for Team", "Dropped Ball", "Throw-in"],"answer": 2},
    {"question": "An attacking player (number 13) on team B didn't sleep well last night, and he's very tired. He's so tired that he curls up on the field near the corner arc and falls asleep in an offside position. A few minutes later, play returns to Team A's side of the field. A goal is scored, but the parents on Team A are screaming about an offside call. Do you make one?","options": ["No, because once offside is called, a goal cannot be scored", "Yes, you call an offside and allow Team A to take a free kick", "Number 13 was not involved in active play, so he is not offside d. Yes, you call offside", "Yes, you call offside. The assistant referee should have signalled for offsides the minute number 13 crossed behind the defender"],"answer": 2},
    {"question": "While walking on the field, you notice that you have dropped your whistle. Panicking, you stop the game and ask for help from the coaches. They are upset, but offer to help you look for your whistle. A minute later, with all the players searching, they can't find it anywhere. A fan from team B has a megaphone, and offers that instead. What do you do?","options": ["Keep searching until you find it. The referee needs a whistle!", "Take it. There's nowhere within the Laws that says that a whistle must be used", " Declare the game to be over. It would be unfair to both teams to ref without a whistle and looking for it would take too long ", "Talk to the coaches to see if they mind you just not calling anything"],"answer": 1},
    {"question": "A player takes a penalty kick and hits the crossbar of the goal and it rebounds to this player without touching anyone else. At the second attempt, this player puts the ball in the goal. How does the referee re-start play?","options": ["A kick- off from the centre of the field", "An indirect free kick to the defence", "A drop ball", "A re-taken penalty"],"answer": 1},
    {"question": " To replace a player with a substitute, how many conditions must be observed?","options": ["9", "8", "7", "6"],"answer": 2},
    {"question": "The assistant referee raised his flag in his right hand to signal a foul. However, he has to switch the flag into his other hand, which is the left one. How should he switch the flag into his left hand?","options": ["Switch the flag under the waist ", "Switch the flag in the air", "Don't switch hands", "Switch the flag behind your head"],"answer": 0},
    {"question": "Which of the following is required for a legal throw-in?","options": ["Heels on the ground", "Eyes closed", "Only using one arm", "Ball behind the head"],"answer": 3},
    {"question": "What is the largest size soccer ball that is manufactured?","options": ["None of these", "Size 6", "Size 10", "Size 4"],"answer": 0},
    {"question": "What is it called when a player, without the ball on the offensive team is behind the last defender, or fullback?","options": ["Dangerous Play", "Crowding the Goal", "Offside", "Loitering"],"answer": 2},
    {"question": "What is called when a player deliberately touches the ball with any part of their arm?","options": ["Breakaway", "Arm Ball", "Hand Ball", "Ball Touch"],"answer": 2},
    {"question": "How big is a regulation official soccer goal?","options": ["2.44m high, 7.32m wide", "3.11m high, 8.04m wide", "2.00m high, 7.00m wide", "1.67m high, 7.48m wide"],"answer": 0},
    {"question": "Is veterans' (persons aged over 35) football played by the same laws as Premiership football?","options": ["The laws state that they may be modified in certain ways for veterans' football", "There is a separate law book", "Yes", "Veterans' football can have variations in the laws relating to substitutions, but that is the only difference"],"answer": 0},
    {"question": "In which country, home to the SK Sturm Graz club, was there a stadium known as the Arnold Schwarzenegger Stadium before it changed its name in 2005?","options": ["United States", "Austria", "Germany", "Poland"],"answer": 1},
    {"question": "A quick boat across the North Sea and we are in the Faeroe Islands. These tiny islands most famous result was when they held Scotland to a 2-2 draw in 2002. In which town did the national side play its home games?","options": ["Toftir", "Sandur", "Klaksvik", "Torshavn"],"answer": 3},
    {"question": "Heading south and Scotland is where we land. Football here is dominated by two clubs; Rangers and Celtic, both Glasgow clubs. The national stadium is Hampden Park and is actually home to which Scottish club?","options": ["Queen of the South", "Queen’s Park", "Stenhousemuir", "Peterhead"],"answer": 1},
    {"question": "Which country has an 8,000 seater stadium, Rheinpark Stadium, that is home to the national squad?","options": ["Luxembourg", "Austria", "Switzerland", "Liechtenstein"],"answer": 3},
    {"question": "Where was the 2002 European Champions League Final held?","options": ["Nou Camp (Barcelona)", "Olimpico (Rome)", "Stade de France (St. Denis)", "Hampden Park (Glasgow)"],"answer": 3},
    {"question": "Christine Sinclair, a Canadian soccer superstar, is from what province in Canada?","options": ["Prince Edward Island", "Alberta", "Ontario", "British Columbia"],"answer": 3},
    {"question": "September 1989, Rio: In a game that didn't go the distance as Brazil's final World Cup qualifier at home to Chile, was abandoned after 65 minutes for reasons that sent shock waves through the footballing world. What happened?","options": ["Fans rioted after a refereeing decision went against their team", "The ball burst and they had no replacement", "The referee stopped the game after a fight broke out involving the two managers", "Chile's keeper was hit by a missile thrown by a fan and his teammates refused to play on"],"answer": 3},
    {"question": "The world's oldest football club still in existence was founded in 1857, but which English city does it call home?","options": ["Sheffield", "Manchester", "Nottingham", "Leicester"],"answer": 0},
    {"question": " In addition to the World Cup, each of the continental federations holds a tournament to crown its own local champion. Which continent's competition is the oldest?","options": ["South America", "Africa", "Europe", "Asia"],"answer": 0},
    {"question": "Which of these clubs does not have yellow on their home shirts?","options": ["Galatasaray", "ADO Den Haag", "Torquay United", "Dynamo Kiev"],"answer": 3},
    {"question": "Which Belgian player, whose career was cut short due to injury, has changed the face of football transfers forever?","options": ["Enzo Scifo", "Luc Nilis", "Jean-Marc Bosman", "Raymond Goethals"],"answer": 2},
    {"question": "If you went to see IA Akranes play - which country would you go to?","options": ["Latvia", "Finland", "Belarus", "Iceland"],"answer": 3},
    {"question": "Who won the European Championships, held in Sweden in 1992?","options": ["Sweden", "Holland", "Germany", "Denmark"],"answer": 3},
    {"question": "Who joined Germany, Spain, and South Korea in Group C at the 1994 World Cup finals?","options": ["Norway", "Iceland", "Bolivia", "Russia"],"answer": 3},
    {"question": "Which year was the first FA Cup live in color on TV?","options": ["1969", "1966", "1967", "1968"],"answer": 3},
]

################################################################################
# UTILITY FUNCTIONS
################################################################################

# This function adds contents to the commentary box
def appendComment(text):
    global commentaryText
    if commentaryText:
        commentaryText.insert(END, text + "\n")
        commentaryText.see(END)

# This function displays a dyslexic font option for accessibility
def toggleFont(frame):
    if dyslexicStatus.get():
        fontName = "OpenDyslexic"
        # Use smaller constant sizes for dyslexic font
        sizeMap = {36: 24, 26: 18, 22: 16, 20: 14, 16: 12, 14: 11, 12: 10}
    else:
        fontName = "Arial"
        sizeMap = {}
        
    for widget in frame.winfo_children():
        try:
            currentFont = widget.cget("font")
            size = 14  # default size
            weight = "normal"  # default weight
            
            # Preserve the original size and weight
            if isinstance(currentFont, tuple):
                if len(currentFont) > 1:
                    originalSize = currentFont[1]
                    # Map to smaller size if dyslexic font is enabled
                    size = sizeMap.get(originalSize, originalSize) if dyslexicStatus.get() else originalSize
                if len(currentFont) > 2:
                    weight = currentFont[2]
                widget.config(font=(fontName, size, weight))
            elif isinstance(currentFont, str):
                widget.config(font=(fontName, size))
            else:
                widget.config(font=(fontName, size))
        except:
            pass
        
        # Recursively apply to nested frames
        if isinstance(widget, Frame):
            toggleFont(widget)

# This function returns the appropriate font based on dyslexic setting
def getFont(size, weight="normal"):
    fontName = "OpenDyslexic" if dyslexicStatus.get() else "Arial"
    # Use smaller constant sizes for dyslexic font
    if dyslexicStatus.get():
        sizeMap = {36: 24, 26: 18, 22: 16, 20: 14, 16: 12, 14: 11, 12: 10}
        size = sizeMap.get(size, size)
    
    if weight == "normal":
        return (fontName, size)
    else:
        return (fontName, size, weight)

# This function creates an animation for the starting screen
def animate(canvas, playerTag, ballTag, dx, dy):
    canvasWidth = canvas.winfo_width()
    
    playerCoords = canvas.bbox(playerTag)
    ballCoords = canvas.bbox(ballTag)
    
    if playerCoords and playerCoords[2] > canvasWidth:
        canvas.move(playerTag, -canvasWidth, 0)
    else:
        canvas.move(playerTag, dx, 0)
    
    if ballCoords and ballCoords[2] > canvasWidth:
        canvas.move(ballTag, -canvasWidth, 0)
    else:
        canvas.move(ballTag, dx, dy)
    
    canvas.after(50, lambda: animate(canvas, playerTag, ballTag, dx, dy))

# This function stops the music and exit the game if user clicks on exit
def stop_music_and_exit():
    pygame.mixer.music.stop()
    window.destroy()

# This function draws a soccer field
def drawField(canvas):
    canvas.create_rectangle(50, 50, 850, 450, outline="white", width=3)
    canvas.create_line(450, 50, 450, 450, fill="white", width=3)
    canvas.create_oval(410, 210, 490, 290, outline="white", width=3)
    canvas.create_oval(445, 245, 455, 255, fill="white")
    canvas.create_rectangle(50, 150, 150, 350, outline="white", width=3)
    canvas.create_rectangle(750, 150, 850, 350, outline="white", width=3)
    canvas.create_rectangle(50, 200, 100, 300, outline="white", width=3)
    canvas.create_rectangle(800, 200, 850, 300, outline="white", width=3)

# This function shows a non-blocking floating message
def showFloatingMessage(text, color="yellow"):
    popup = Toplevel(window)
    popup.overrideredirect(True)
    popup.config(bg="black")
    popup.lift()
    popup.attributes("-topmost", True)
    popup.after_idle(popup.lift)

    popup.update_idletasks()
    x = window.winfo_x() + window.winfo_width()//2 - 150
    y = window.winfo_y() + window.winfo_height()//2 - 100
    popup.geometry(f"300x60+{x}+{y}")

    Label(
        popup,
        text=text,
        font=("Arial", 20, "bold"),
        fg=color,
        bg="black"
    ).pack(expand=True)

    popup.after(1000, popup.destroy)

################################################################################
# SCREEN 1: WELCOME SCREEN
################################################################################

# This function displays a welcome/starting screen with animation
def showWelcomeScreen():
    startFrame = Frame(window, bg="green")
    startFrame.pack(fill=BOTH, expand=True)
    
    Label(startFrame, text="Welcome to the Soccer Game!",
          font=("Arial", 36, "bold"), fg="white", 
          bg="green").pack(pady=50)
    
    Checkbutton(startFrame, text="Use Dyslexic-Friendly Font", 
                variable=dyslexicStatus,
                command=lambda: toggleFont(startFrame),
                font=("Arial", 14), bg="green", fg="white").pack()
    
    canvas = Canvas(startFrame, width=800, height=400, bg="green")
    canvas.pack()
    
    try:
        logo_path = os.path.join(os.getcwd(), "Final_mainIMG_DuSivasankarXiu.png")
        logo = Image.open(logo_path).resize((360, 220))
        logo = ImageTk.PhotoImage(logo)
        canvas.logo = logo
        canvas.create_image(400, 270, image=logo, anchor="center")
    except:
        print("Error with main image file.")
        sys.exit(1)

    # Create animated player
    head = canvas.create_oval(80, 30, 100, 50, fill="blue")
    torso = canvas.create_rectangle(85, 50, 95, 90, fill="blue")
    leftArm = canvas.create_rectangle(75, 50, 85, 70, fill="blue")
    rightArm = canvas.create_rectangle(95, 50, 105, 70, fill="blue")
    leftLeg = canvas.create_rectangle(85, 90, 90, 120, fill="blue")
    rightLeg = canvas.create_rectangle(90, 90, 95, 120, fill="blue")
    for part in [head, torso, leftArm, rightArm, leftLeg, rightLeg]:
        canvas.itemconfig(part, tags="player")
    
    canvas.create_oval(90, 130, 110, 150, fill="red", tags="ball")
    animate(canvas, "player", "ball", 5, 0)
    
    Button(startFrame, text="Start Game", font=("Arial", 20),
           command=lambda: transitionToTeamSelection(startFrame)).pack(pady=30)

    # Load and start playing music
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("Final_musicMP3_DuSivasankarXiu.mp3")
    except:
        print("Error with music file")
        sys.exit(1)
    pygame.mixer.music.play()

    Button(startFrame, text="Exit", font=("Arial", 16), 
           command=stop_music_and_exit).pack(pady=10)
    
    window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

# This function transitions from welcome screen to team selection
def transitionToTeamSelection(startFrame):
    startFrame.pack_forget()
    startFrame.destroy()
    showTeamSelectionScreen()

################################################################################
# SCREEN 2: USER TEAM SELECTION
################################################################################

# This function adds the selected team into the entry box
def onTeamSelect(event, listbox, userInput):
    selected = listbox.curselection()
    if selected:
        team = listbox.get(selected[0])
        userInput.delete(0, END)
        userInput.insert(0, team)
        
# This function displays the user team selection screen
def showTeamSelectionScreen():
    mainFrame = Frame(window)
    mainFrame.pack(fill=BOTH, expand=True)
    mainFrame.update_idletasks()
    
    Label(mainFrame, text="List of Soccer Teams:", 
          font=getFont(20)).pack(pady=20)

    lbFrame = Frame(mainFrame)
    lbFrame.pack()

    scrollbar = Scrollbar(lbFrame, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(lbFrame, height=10, font=getFont(16), 
                     yscrollcommand=scrollbar.set)
    for team in teamList:
        listbox.insert(END, team)
    listbox.pack(side=LEFT, fill=BOTH)
    listbox.update()

    scrollbar.config(command=listbox.yview)
           
    userInput = Entry(mainFrame, font=getFont(16))
    userInput.pack(pady=10)
    
    listbox.bind("<<ListboxSelect>>", 
                lambda event: onTeamSelect(event, listbox, userInput))
    
    resultLabel = Label(mainFrame, 
                       text="Please select your team.\nYou can also type in a team that isn't on the list.\nClick \"Random Team\" if you want to be assigned a random team.", 
                       font=getFont(16))
    resultLabel.pack(pady=10)

    def randomTeam():
        team = random.choice(teamList)
        userInput.delete(0, END)
        userInput.insert(0, team)
        
    Button(mainFrame, text="Random Team", font=getFont(16), 
          bg="lightblue", highlightbackground="lightblue", command=randomTeam).pack(pady=10)
    
    Button(mainFrame, text="Submit Team", font=getFont(16), 
          command=lambda: submitUserTeam(userInput, resultLabel, mainFrame)).pack(pady=10)

    Checkbutton(mainFrame, text="Use Dyslexic-Friendly Font", 
               variable=dyslexicStatus, 
               command=lambda: toggleFont(mainFrame), 
               font=getFont(14)).pack()
    
    Button(mainFrame, text="Exit", font=getFont(16), 
          command=stop_music_and_exit).pack(pady=10)

# This function handles user team submission and transitions to opponent selection
def submitUserTeam(userInput, resultLabel, mainFrame):
    userTeam = userInput.get().strip()
    
    if userTeam:
        resultLabel.config(text=f"You selected: {userTeam}")
        mainFrame.pack_forget()
        mainFrame.destroy()
        showOpponentSelectionScreen(userTeam)

################################################################################
# SCREEN 3: OPPONENT TEAM SELECTION
################################################################################

# This function displays the opponent team selection screen
def showOpponentSelectionScreen(userTeamRef):
    opponentFrame = Frame(window)
    opponentFrame.pack(fill=BOTH, expand=True)
    opponentFrame.update_idletasks()
    
    Label(opponentFrame, text=f"Choose an opponent for {userTeamRef}:", 
          font=getFont(20)).pack(pady=20)

    opFrame = Frame(opponentFrame)
    opFrame.pack()

    opScroll = Scrollbar(opFrame, orient="vertical")
    opScroll.pack(side=RIGHT, fill=Y)

    listbox = Listbox(opFrame, height=10, font=getFont(16), 
                     yscrollcommand=opScroll.set)

    for team in teamList:
        if team != userTeamRef:
            listbox.insert(END, team)
            
    listbox.pack(side=LEFT, fill=BOTH)
    opScroll.config(command=listbox.yview)
    opponentFrame.update_idletasks()
    
    opponentInput = Entry(opponentFrame, font=getFont(16))
    opponentInput.pack(pady=10)
    opponentInput.update_idletasks()
    
    listbox.bind("<<ListboxSelect>>", 
                lambda event: onTeamSelect(event, listbox, opponentInput))

    resultLabel = Label(opponentFrame, 
                       text="Please select your opponent.\nYou can also type in a team that isn't on the list\nClick \"Random Opponent\" to be random assigned a team.", 
                       font=getFont(16))
    resultLabel.pack(pady=10)

    def randomOpponent():
        validTeams = [t for t in teamList if t != userTeamRef]
        team = random.choice(validTeams)
        opponentInput.delete(0, END)
        opponentInput.insert(0, team)
        
    Button(opponentFrame, text="Random Opponent", font=getFont(16), 
          bg="lightblue", highlightbackground="lightblue", command=randomOpponent).pack(pady=10)

    def validateOpponent():
        opponentTeam = opponentInput.get().strip()
        if not opponentTeam:
            return
        opponentFrame.pack_forget()
        opponentFrame.destroy()
        showGameplayScreen(userTeamRef, opponentTeam)

    Button(opponentFrame, text="Submit Opponent", font=getFont(16), 
          command=validateOpponent).pack(pady=10)
               
    Checkbutton(opponentFrame, text="Use Dyslexic-Friendly Font", 
               variable=dyslexicStatus, 
               command=lambda: toggleFont(opponentFrame),
               font=getFont(14)).pack()
    
    Button(opponentFrame, text="Exit", font=getFont(16), 
          command=stop_music_and_exit).pack(pady=10)

################################################################################
# SCREEN 4: GAMEPLAY SCREEN
################################################################################

# This function shows the gameplay screen
def showGameplayScreen(userTeamRef, opponentTeamRef):
    global gameFrame, canvas, userPlayers, opponentPlayers, timerLabel
    global playsLeft, score, userTeam, opponentTeam
    global teamHasBall, playerHasBall, messageBox, commentaryText, scoreLabel
    global dribbleBtn, passBtn, shootBtn, defendBtn
        
    playsLeft = 90
    userTeam = userTeamRef
    opponentTeam = opponentTeamRef
        
    userTeamPlayers = list(range(1, 12))
    opponentTeamPlayers = list(range(1, 12))
        
    teamHasBall = random.choice([userTeam, opponentTeam])
    if teamHasBall == userTeam:
        playerHasBall = userTeamPlayers[8]
    else:
        playerHasBall = opponentTeamPlayers[8]
        
    # main container
    gameFrame = Frame(window, bg="green")
    gameFrame.pack(fill=BOTH, expand=True)
        
    # top section
    topFrame = Frame(gameFrame, bg="green")
    topFrame.pack(side=TOP, fill=X, pady=5)
        
    timerLabel = Label(topFrame, text=f"Time Left: {playsLeft} Minutes",
                               font=("Arial", 20), bg="green", fg="white")
    timerLabel.pack(side=LEFT, padx=20)
        
    score = {"user": 0, "opponent": 0}
    scoreLabel = Label(topFrame,
                            text=f"Score: {userTeam} (User) {score['user']} - {opponentTeam} (Computer) {score['opponent']}",
                            font=("Arial", 20), bg="green", fg="white")
    scoreLabel.pack(side=RIGHT, padx=20)
        
    # middle section
    canvas = Canvas(gameFrame, width=900, height=500, bg="green")
    canvas.pack(pady=10)
    drawField(canvas)
        
    # message box
    messageBox = canvas.create_text(450, 250, text="", fill="white",
                                            font=("Arial", 24, "bold"),
                                            width=500, justify="center")
        
    # action buttons
    actionFrame = Frame(gameFrame, bg="green")
    actionFrame.pack(pady=10)
        
    dribbleBtn = Button(actionFrame, text="Dribble", font=("Arial", 16),
                                command=lambda: askTrivia("Dribble"))
    dribbleBtn.pack(side=LEFT, padx=10)
        
    passBtn = Button(actionFrame, text="Pass", font=("Arial", 16),
                             command=lambda: askTrivia("Pass"))
    passBtn.pack(side=LEFT, padx=10)
        
    shootBtn = Button(actionFrame, text="Shoot", font=("Arial", 16),
                              command=lambda: askTrivia("Shoot"))
    shootBtn.pack(side=LEFT, padx=10)
        
    defendBtn = Button(actionFrame, text="Defend", font=("Arial", 16),
                               command=lambda: askTrivia("Defend"))
    defendBtn.pack(side=LEFT, padx=10)
        
    # commentary frame
    commentaryFrame = Frame(gameFrame, bg="green")
    commentaryFrame.pack(pady=5)
        
    controlsFrame = Frame(commentaryFrame, bg="green")
    controlsFrame.pack(side=LEFT, padx=10, anchor="n")
        
    Checkbutton(controlsFrame, text="Use Dyslexic-Friendly Font",
                        variable=dyslexicStatus,
                        command=lambda: toggleFont(gameFrame),
                        font=("Arial", 14), bg="green", fg="white").pack(pady=5)
        
    Button(controlsFrame, text="Exit", font=("Arial", 16),
                   command=earlyExit).pack(pady=10)
        
    textFrame = Frame(commentaryFrame, bg="green")
    textFrame.pack(side=LEFT, padx=20)
        
    scrollbar = Scrollbar(textFrame)
    scrollbar.pack(side=RIGHT, fill=Y)
        
    commentaryText = Text(textFrame, width=80, height=15,
                                  font=("Arial", 12), wrap="word",
                                  yscrollcommand=scrollbar.set)
    commentaryText.pack(side=LEFT)
        
    scrollbar.config(command=commentaryText.yview)
        
    # intial commentary
    appendComment("Welcome to the exciting soccer match!\n")
    appendComment(f"Great! You have picked {userTeam} as your team! You will play against {opponentTeam}.\n")
    appendComment(f"The match between {userTeam} (User) and {opponentTeam} (Computer) is about to start!\n")
    appendComment(f"Captains of {userTeam} (User) and {opponentTeam} (Computer) are in the coin toss to decide who kicks off!\n")
    appendComment(f"The coin toss decides that {teamHasBall} {'(User)' if teamHasBall == userTeam else '(Computer)'} will take the kick-off!\n")
    appendComment("The match starts!!!\n")
    appendComment("===================================================================================================\n")
        
    # player formations
    userPlayers = []
    opponentPlayers = []
        
    userFormation = [(80, 240), (200, 130), (200, 200), (200, 270),
                             (200, 340), (300, 130), (300, 200), (300, 270),
                             (300, 340), (400, 190), (400, 310)]
        
    for (x, y) in userFormation:
        player = canvas.create_oval(x, y, x + 30, y + 30, fill="blue", tags="user")
        userPlayers.append(player)
        
    opponentFormation = [(780, 240), (700, 130), (700, 200), (700, 270),
                                 (700, 340), (600, 130), (600, 200), (600, 270),
                                 (600, 340), (475, 190), (475, 310)]
        
    for (x, y) in opponentFormation:
        player = canvas.create_oval(x, y, x + 30, y + 30, fill="red", tags="opponent")
        opponentPlayers.append(player)
        
    updateScore()
    announceMinute()

################################################################################
# GAME LOGIC FUNCTIONS
################################################################################

# This function updates the score display
def updateScore():
    scoreLabel.config(
        text=f"Score: {userTeam} (User) {score['user']} - {opponentTeam} (Computer) {score['opponent']}"
    )

# This function adds commentary for each play/minute
def announceMinute():
    global playsLeft, teamHasBall, userTeam, opponentTeam, playerHasBall

    minute = 90 - playsLeft + 1
    appendComment(f"Minute {minute}:\n")
    appendComment(f"No.{playerHasBall} of {teamHasBall} "
                  f"{'(User)' if teamHasBall == userTeam else '(Computer)'} has the ball.")

    if teamHasBall == userTeam:
        appendComment('Your turn to attack. Click "Dribble", "Pass" or "Shoot".')
        setButtonState(True)
    else:
        computerMove()
        appendComment(f"{opponentTeam} (Computer) attacking! Click \"Defend\" when ready.")
        setButtonState(False)

# This function enables necessary buttons depending on user team status
def setButtonState(userTurn):
    if dribbleBtn:
        dribbleBtn.config(state="normal" if userTurn else "disabled")
        passBtn.config(state="normal" if userTurn else "disabled")
        shootBtn.config(state="normal" if userTurn else "disabled")
        defendBtn.config(state="disabled" if userTurn else "normal")

# This function handles the case that a computer team makes an attack move
def computerMove():
    global teamHasBall, playerHasBall, opponentTeam, compAction

    if teamHasBall != opponentTeam:
        return

    compAction = random.choice(["Dribble", "Pass", "Shoot"])
    appendComment(f"No.{playerHasBall} of {opponentTeam} chooses to {compAction.lower()}.")
    appendComment("Click Defend first, then answer the trivia question!")

    setButtonState(False)

# This function adds commentary when the user team is about to attack
def announceUserAttack():
    appendComment("Your turn to attack. Please click Dribble, Pass, or Shoot.")

# This function adds commentary when the user team is about to defend
def announceUserDefend():
    appendComment("Your turn to defend. Click Defend.")

# This function asks the user a trivia question to determine a successful play
def askTrivia(action):
    question = random.choice(triviaQuestions)
    triviaQuestions.remove(question)
    
    popup = Toplevel(window)
    popup.title("Answer for a successful play!")
    popup.geometry("500x300")
    popup.grab_set()

    fontName = "OpenDyslexic" if dyslexicStatus.get() else "Arial"

    label_font = (fontName, 16)
    
    Label(popup, text=question["question"], font=label_font, 
          wraplength=450).pack(pady=10)
    
    var = IntVar(value=-1)
    for i, opt in enumerate(question["options"]):
        Radiobutton(popup, text=opt, variable=var, value=i, 
                   font=label_font).pack(anchor="w", padx=20)

    def submit():
        selected = var.get()
        
        if selected == -1:
            messagebox.showwarning("No Selection", 
                                 "Please select an answer before submitting.")
            return

        success = (selected == question["answer"])

        if action == "Dribble":
            dribble(success)
        elif action == "Pass":
            passBall(success)
        elif action == "Shoot":
            shoot(success)
        elif action == "Defend":
            defend(success)
               
        if success:
            showFloatingMessage(f"{action} successful!", color="lime")
        else:
            showFloatingMessage(f"{action} failed!", color="red")

        updateScore()

        global playsLeft

        appendComment(f"After Minute {90 - playsLeft + 1}, the score is {userTeam} (User) {score['user']} - {opponentTeam} (Computer) {score['opponent']}")
        appendComment("===============================================================================================")

        playsLeft -= 1
        timerLabel.config(text=f"Minutes left: {playsLeft}")

        if playsLeft <= 0:
            popup.destroy()
            showEndScreen()
            return

        announceMinute()
        popup.destroy()

    Button(popup, text="Submit", font=getFont(14), command=submit).pack(pady=15)

# This function simulates the dribble action
def dribble(success):
    global teamHasBall, playerHasBall, score

    if not success:
        if teamHasBall == userTeam:
            teamHasBall = opponentTeam
            playerHasBall = random.randint(1, 11)
            appendComment("Dribble intercepted!")
            showAnimation("dribble_fail")
            return
        else:
            teamHasBall = userTeam
            appendComment("Opponent dribble intercepted!")
            showAnimation("dribble_fail")  
            return

    appendComment("Dribble success!")
    showAnimation("dribble_success")

# This function simulates the pass action
def passBall(success):
    global teamHasBall, playerHasBall, score

    if success:
        teammates = list(range(1, 12))
        teammates.remove(playerHasBall)
        playerHasBall = random.choice(teammates)
        appendComment("Pass completed!")
        showAnimation("pass_success")
        announceUserAttack()
    else:
        if teamHasBall == userTeam:
            appendComment("Pass intercepted!")
            showAnimation("pass_fail")
            teamHasBall = opponentTeam
            playerHasBall = random.randint(1, 11)
            return
        else:
            appendComment("Opponent pass intercepted!")
            showAnimation("pass_fail")
            teamHasBall = userTeam
            playerHasBall = random.randint(1, 11)

# This function simulates the shoot action
def shoot(success):
    global teamHasBall, playerHasBall, score

    if success:
        if teamHasBall == userTeam:
            appendComment(f"GOAL for {userTeam} (User)!!! {opponentTeam} (Computer) will kick off.")
            showAnimation("shoot_success")
            score["user"] += 1
            teamHasBall = opponentTeam
        else:
            appendComment(f"GOAL for {opponentTeam} (Computer)!!! {userTeam} (User) will kick off.")
            showAnimation("shoot_success")
            score["opponent"] += 1
            teamHasBall = userTeam
        
        playerHasBall = 9
        return

    appendComment("Shot saved.")
    showAnimation("shoot_fail")

    teamHasBall = random.choice([userTeam, opponentTeam])
    playerHasBall = random.randint(1, 11)

# This function simulates the defend action
def defend(success):
    global teamHasBall, playerHasBall, score, compAction

    if success:
        if compAction == "Dribble":
            appendComment(f"What a defensive play! {userTeam} (User) now has the ball!")
            showAnimation("dribble_fail")
        elif compAction == "Pass":
            appendComment(f"What a defensive play! {userTeam} (User) now has the ball!")
            showAnimation("pass_fail")
        else:
            appendComment(f"What a save! {userTeam} (User)'s goalkeeper saves the shot!")
            showAnimation("shoot_fail")
            
        teamHasBall = userTeam
        playerHasBall = random.randint(1, 11)
        return

    appendComment("Defense failed.")

    if compAction == "Shoot":
        score["opponent"] += 1
        appendComment("Computer scored!")
        showAnimation("shoot_success")
        teamHasBall = userTeam
        playerHasBall = 9

    elif compAction == "Pass":
        appendComment("Opponent pass completed!")
        showAnimation("pass_success")
        playerHasBall = random.randint(1, 11)

    else: 
        appendComment("Opponent dribble successful!")
        showAnimation("dribble_success")

# This function shows popup GIF animation based on action results
def showAnimation(resultType):
    gifPath = animationGIFS.get(resultType)
    if not gifPath:
        return

    popup = Toplevel(window)
    popup.title("Animation")
    popup.geometry("500x400")
    popup.resizable(False, False)
    popup.attributes("-topmost", True)

    canvas = Canvas(popup, width=500, height=400, bg="black")
    canvas.pack()

    frames = []
    try:
        gif = Image.open(gifPath)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_img = ImageTk.PhotoImage(gif.copy().resize((450, 350)))
            frames.append(frame_img)
    except:
        popup.destroy()
        return

    total_frames = len(frames)

    def animate(i=0):
        if i >= total_frames:
            popup.after(200, popup.destroy)
            return

        canvas.delete("all")
        canvas.create_image(250, 200, image=frames[i])
        popup.after(60, animate, i + 1)

    animate()

# This function deals with an early exit when Exit button is clicked during the match
def earlyExit():
    showEndScreen()

################################################################################
# SCREEN 5: END SCREEN
################################################################################

# This function shows the ending screen of the game and draws a scoreboard
def showEndScreen():
    global score, userTeam, opponentTeam, gameFrame

    gameFrame.pack_forget()
    gameFrame.destroy()

    scoreFrame = Frame(window, bg="green")
    scoreFrame.pack(fill=BOTH, expand=True)

    scoreCanvas = Canvas(scoreFrame, width=900, height=500, bg="green")
    scoreCanvas.pack(pady=20)

    drawField(scoreCanvas)

    scoreCanvas.create_rectangle(250, 150, 650, 350, outline="white", width=4)
    scoreCanvas.create_text(450, 175, text="FINAL SCORE", fill="white", 
                          font=("Arial", 26, "bold"))
    scoreCanvas.create_text(450, 235, text=f"{userTeam} (User): {score['user']}", 
                          fill="blue", font=("Arial", 22, "bold"))
    scoreCanvas.create_text(450, 295, text=f"{opponentTeam} (Computer):   {score['opponent']}", 
                          fill="red", font=("Arial", 22, "bold"))

    Button(scoreFrame, text="Exit Game", font=("Arial", 20), 
          command=window.destroy).pack(pady=30)
    
    Checkbutton(scoreFrame, text="Use Dyslexic-Friendly Font", 
               variable=dyslexicStatus, 
               command=lambda: toggleFont(scoreFrame),
               font=getFont(14)).pack()    

################################################################################
# MAIN FUNCTION
################################################################################

def main():
    # Screen 1: Welcome Screen
    showWelcomeScreen()
    
    # The following screens are called through user interaction:
    # Screen 2: Team Selection (called from showWelcomeScreen)
    # Screen 3: Opponent Selection (called from showTeamSelectionScreen)
    # Screen 4: Gameplay (called from showOpponentSelectionScreen)
    # Screen 5: End Screen (called when game ends)
    
    window.mainloop()

main()
