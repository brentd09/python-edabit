def interview(list_of_times,total_time):
    max_times = [5,5,10,10,15,15,20,20]
    if len(list_of_times) != 8 or total_time > 120:
        return 'Disqualified'
    for indx in range(8):
        if list_of_times[indx] > max_times[indx]:
            return 'Disqualified'
    return 'Qualified'        

            

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))