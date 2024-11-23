class DVDPlayer:
    def on(self):
        print("DVD Player is ON")
    
    def play(self):
        print("Playing movie")

class Projector:
    def on(self):
        print("Projector is ON")
    
    def wide_screen_mode(self):
        print("Projector is in widescreen mode")

class SoundSystem:
    def on(self):
        print("Sound system is ON")
    
    def set_volume(self, level):
        print(f"Volume set to {level}")

class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
    
    def watch_movie(self):
        print("Get ready to watch a movie...")
        self.dvd_player.on()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.dvd_player.play()

dvd = DVDPlayer()
projector = Projector()
sound_system = SoundSystem()

home_theater = HomeTheaterFacade(dvd, projector, sound_system)
home_theater.watch_movie()
