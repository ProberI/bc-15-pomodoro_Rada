from pygame import mixer
def format_time(t):
    minutes = int(t // 60)
    seconds_rem = int(t % 60)
    if seconds_rem < 10:
        return (str(minutes) + ':0' + str(seconds_rem))
    else:
        return  (str(minutes) + ':' + str(seconds_rem))

