from typing import List
from datetime import timedelta # not familar with the api

"""
    question

    topic
     + sorting

    twist
     + merge intervals; but then get the inverse
     + time is in strings

     + can the duration will be in mins ?

    test
    + assert 

    brute-force
     # 0
     + reursive aproach that would
     consider all meeting times;
     then elimiate based on conditions
     + time-complexity: O(2^n)

    complexity-ladder
     + # 1
     + merge itervals
     + get inverse (space between meetings)
     + eliminate meeting less than duration
     + eliminate meetings outside of bounds
     + time-complexity: O(n)
     + space-complexity: O(n)

    code

    execute

"""

def abs_time(string) -> int:
    hrs, mins = string.split(":")
    return (int(hrs)*60)+int(mins)

def get_available_times(unavailable_times, start, end) -> List[int]:
    
    if not unavailable_times:
        return [[start, end]]
    
    start_time = abs_time(start)
    end_time = abs_time(end)
    
    result = []
    
    p1 = 0
    p2 = 1
    
    while p2 < len(unavailable_times):
        st = abs_time(unavailable_times[p1][1])
        s = unavailable_times[p1][1]
        e = unavailable_times[p2][0]
        et = abs_time(unavailable_times[p2][0])
        
        if start_time <= st < end_time and start_time < et <= end_time:
            result.append(
                [ s, e ]
            )
        
        p1 += 1
        p2 += 1
        
    print(result)
        
    if abs_time( unavailable_times[-1][1] ) < end_time:
        result.append( [ unavailable_times[-1][1], end ] )
    
    return result

def merge_calendars(calendar1, calendar2) -> List[int]:
    
    # merge sorted array
    p1 = 0
    p2 = 0
    result = []
    
    while p1 < len(calendar1) and p2 < len(calendar2):
        
        t1 = abs_time(calendar1[p1][0])
        t2 = abs_time(calendar2[p2][0])
        
        if t1 < t2:
            result.append( calendar1[p1] )
            p1 += 1
        elif t1 == t2:
            result.append( calendar1[p1] )
            result.append( calendar2[p2] )
            p1 += 1
            p2 += 1
        else:
            result.append( calendar2[p2] )
            p2 += 1
            
    result.extend(calendar1[p1:])
    result.extend(calendar2[p2:])
    
    print(result)
    print(" -- ")
    
    # merge intervals -- learned a lesson about m
    # erge interval...don't forget the max
    if result:
        merged = [ result[0] ]
        for i in range(1, len(result)):
            i_start = abs_time(result[i][0])
            last_end = abs_time(merged[-1][1])
            if i_start <= last_end:
                merged[-1][1] = max( merged[-1][1], result[i][1] )
            else:
                merged.append(result[i])
    else:
        merged = []
            
    print(merged)
    print(" ** ")
    
    return merged

def calendarMatching(
    calendar1, dailyBounds1,
    calendar2, dailyBounds2,
    duration
) -> List[List[int]]:
    
    start = max(dailyBounds1[0], dailyBounds2[0])
    end = min(dailyBounds1[1], dailyBounds2[1])
    
    unavailable_times = merge_calendars( calendar1, calendar2 )
    
    available_times = get_available_times(unavailable_times, start, end)
    
    before_meetings = []
    
    if calendar1 and calendar2:
        start1 = calendar1[0][0]
        start2 = calendar2[0][0]
        if abs_time(start) < abs_time(min(start1, start2, key=abs_time)):
            available_times = [
                [start, min(start1, start2, key=abs_time)]
            ] + available_times
    
    elif calendar1 and not calendar2:
        if abs_time(start) < abs_time(calendar1[0][0]):
            available_times = [ [start, calendar1[0][0]] ] + available_times

    elif not calendar1 and calendar2:
        if abs_time(start) < abs_time(calendar2[0][0]):
            available_times = [ [start, calendar2[0][0]] ]  + available_times
    else:
        pass
    
    print(available_times)
    
    matches = [ t for t in available_times
                if abs_time(t[1]) - abs_time(t[0]) >= duration ]
    
    return matches

