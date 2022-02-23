import tkinter as tk
import tkinter.ttk

# adding the screens
screens = [
    'Screen 1', 'Screen 2', 'Screen 3',
    'Screen 1', 'Screen 2', 'Screen 3',
    'Screen 1', 'Screen 2', 'Screen 3',
]

# adding the movies
movies = {
    'Horror': [
        'Hereditary', 
        'A Quiet Place', 
        'The Conjuring 2', 
        'The Grudge',
        'Anabelle Comes Home'
    ],
    'Action': [
        'Avengers End Game',
        'John Wick Chapter 3',
        'Aquaman',
        'Black Panther',
        'Mission Impossible'
    ],
    'Drama': [
        'Joker',
        'Spotlight',
        'Little Women',
        'The Irishman',
        'A Star is Born'
    ],
    'Comedy': [
        'Step Brothers',
        'BookSmart',
        'Horrible Bosses',
        'The Other Guys',
        'SuperBad'
    ],
    'Sci-Fi': [
        'The Fault in our Stars',
        'The Notebook',
        'The Tourist',
        'Titanic',
        'Crazy Rich Asians'
    ]
}

# adding the times
times = [
    '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00',
]

# seats
seatList = []
seatSelected = []