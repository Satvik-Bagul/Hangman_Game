# Hangman
<pre>
A terminal-based interactive Hangman game implemented in Python. This project demonstrates core computer science concepts such as modular programming, data structures, input validation, control flow, and algorithmic logic, while providing an engaging word-guessing experience.

Features:
  Random Phrase Selection:
    Reads phrases from a text file and selects a random phrase using Python’s random module.
    Gracefully handles missing or empty files with fallback phrases.
  
  Dynamic ASCII Gallows:
    Visually represents game progress using dynamically generated ASCII graphics.
    Updates in real-time based on incorrect guesses.
 
  User Input Validation:
    Robust input handling ensures only valid single letters are accepted.
    Prevents duplicate guesses and handles non-alphabetic input.

  Algorithmic Logic:
    Tracks guessed letters and calculates the revealed phrase dynamically.
    Determines game outcome with a Boolean check for completed phrases.

  Data Structures:
    Uses lists and strings to store guesses, track progress, and render the phrase.
    Employs control structures to update game state efficiently.

  Win/Loss Feedback:
    Displays a congratulatory message when the user guesses the phrase correctly.
    Reveals the solution upon exceeding the maximum number of allowed misses.

Core Concepts Demonstrated:
  Modular Functions: make_phrase, print_gallows, get_letter, won, play_game
  Error Handling: try/except blocks to manage file access and empty datasets
  Loops & Conditionals: Efficiently manage game state and user interactions
  String Manipulation: Dynamically reveal letters and format output
  Algorithmic Thinking: Implements game logic and win/loss conditions

How to Play:
  Ensure phrases.txt exists in the same folder with one phrase per line.
  Run the program
    Input one letter at a time to guess the phrase.
    The ASCII gallows updates with each incorrect guess (maximum 6 misses).
    Win by revealing the full phrase or lose if the gallows is complete.

Extensions:
  Add difficulty levels with longer phrases or fewer allowed misses
  Implement hint system using frequency analysis
  Track user statistics across multiple games
  Create a GUI version with Tkinter or PyGame
  Integrate unit testing for automated verification of game logic

Tech Stack & Concepts:
  Python 3.x
  File I/O & Exception Handling
  Lists, Strings, and Iteration
  Modular programming & function design
  Algorithmic problem solving & control flow
</pre>
