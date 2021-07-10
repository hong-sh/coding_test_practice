'''
https://programmers.co.kr/learn/courses/30/lessons/17683
'''

import re

def find_song(m:str, music_infos:list):
    answer = "(None)"

    # replace # melody
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")

    max_time = 0
    for i in range(len(music_infos)):
        music_info = music_infos[i].split(',')
        start_time, end_time, title, sheet = music_info[0], music_info[1], music_info[2], music_info[3]
        
        # compute play minute
        start_h, start_m , end_h, end_m = int(start_time[:2]), int(start_time[3:]), int(end_time[:2]), int(end_time[3:])
        play_minute = ((end_h * 60) + end_m) - ((start_h * 60) + start_m)
        
        # replace # melody
        sheet = sheet.replace("C#", "c")
        sheet = sheet.replace("D#", "d")
        sheet = sheet.replace("F#", "f")
        sheet = sheet.replace("G#", "g")
        sheet = sheet.replace("A#", "a")

        # get actual play sheet
        play_sheet = ""
        if play_minute < len(sheet):
            play_sheet += sheet[:play_minute]
        elif play_minute >= len(sheet):
            for _ in range(play_minute//len(sheet)):
                play_sheet += sheet
            play_sheet += sheet[:(play_minute%len(sheet))]
        
        # match m and play sheet, compare play minute
        if re.findall(m , play_sheet) and max_time < play_minute:
            max_time = play_minute
            answer = title
    
    return answer

if __name__ == "__main__":
    m = "ABCDEFG"
    music_infos = []
    music_infos.append("12:00,12:14,HELLO,CDEFGAB")
    music_infos.append("13:00,13:05,WORLD,ABCDEF")
    print(find_song(m, music_infos))


