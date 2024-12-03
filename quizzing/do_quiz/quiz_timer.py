import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.duration = 0

    def start_timer(self, duration): # set a timer for specific duration
        if self.start_time is not None:
            print('Quiz has already started!')
            return None
        print('------ Quiz Start ------')
        self.start_time = time.time()
        self.duration = duration

    def check_time_remaining(self):
        elapsed_time = time.time() - self.start_time # calculate the time left
        return max(0, self.duration - elapsed_time) # if time run out return 0

    def end_timer(self):
        if self.start_time is None:
            print('Quiz has already closed!')
            return None
        print('------ Quiz End ------')
        self.start_time = None #reset the start_time