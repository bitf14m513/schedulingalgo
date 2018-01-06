print("_______________    F C F S   _________________ ")
t_count = int(input("Enter Total processes :--> "))
arrival_time = [0 for i in range(t_count)]
burst_time = [0 for j in range(t_count)]
start_time = [0 for k in range(t_count)]
finish_time = [0 for f in range(t_count)]
wait_time = [0 for w in range(t_count)]
process_name = [0 for v in range(t_count)]


def take_input():
    for process in range(0, t_count):
        arrival_time[process] = int(input("Enter Arrival time of process %d :" %(process+1)))
        burst_time[process] = int(input("Enter Burst time of process %d :" %(process+1)))
# _________________function to sort array   _________________________________________________________


def smallest(array_to_sort):
    smallest = array_to_sort[0]
    for process in range(0, len(array_to_sort)):
        if smallest > array_to_sort [process]:
            smallest = array_to_sort[process]
    return smallest


def sort(array_to_sort):
    sorted_array = []
    count = len(array_to_sort)
    for count in range(count):
        small = smallest(array_to_sort)
        sorted_array.append(int(small))
        array_to_sort.remove(small)
    return sorted_array
#__________________________________________________________________________________________________


def main():
    take_input()
    arrival_time_temp = [0 for a in range(t_count)]
    for x in range(0, len(arrival_time)):
        arrival_time_temp[x] = arrival_time[x]
    arrival_time_sorted = sort(arrival_time)
    burst_time_sorted = []   # sorted corrspondingly arrival time
    for i in range(0, len(arrival_time_sorted)):
        for j in range(0, len(arrival_time_temp)):
            if arrival_time_temp[j] == arrival_time_sorted[i]:
                burst_time_sorted.append(burst_time[j])
                process_name[i] = j+1
# start time--------------------------------------------------------------------------------------------
    start_time[0] = arrival_time_sorted[0]
    for i in range(1, t_count):
        for j in range(0, i):
            start_time[i] = start_time[j] + burst_time_sorted[j]
        if arrival_time_sorted[i] > start_time[i]:
            start_time[i] += arrival_time_sorted[i] - start_time[i]
#======================================================================================================
# output session---------------------------------------------------------------------------------------
    print("\n\n\n-----------------------------------------------------------------------------------------")
    print("\t\t\t\t=process#===AT=====BT=====ST======FT======WT")
    for counter in range(0, t_count):
        print("\t\t\t\t====", process_name[counter], "====", arrival_time_sorted[counter], "====", burst_time_sorted[counter], "====", start_time[counter],"====" ,start_time[counter]+burst_time_sorted[counter],"====", start_time[counter]-arrival_time_sorted[counter])
    print("-----------------------------------------------------------------------------------------")
main()
