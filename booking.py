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

#app class
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cinema Booking')
        self.createWidgets()

    def updateMovies(self, event=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]

    def createWidgets(self):
        """Create all widgets to be initialized"""
        headingLabel = tk.Label(self, text='Cinema Seat Booking', font='Arial 12 bold')
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='w')
        tkinter.ttk.Separator(self, orient='Horizontal').grid(row=1, column=0, columnspan=5, sticky='w')

        day = tk.Frame(self)
        tk.Label(day, text='________').pack()
        tk.Label(day, text='Today', font='Arial 10 underlined').pack()
        tk.Label(day, text='').pack()
        day.grid(row=2, column=0, padx=10)

app = Application()
app.mainloop()