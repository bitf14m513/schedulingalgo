print("------------------------S R T F-------------------")
t_count = int(input("Enter Total Number of Process : -> "))
jobs = []


def take_input():
    for process in range(0, t_count):
        at = 0
        bt = 0
        job_attr = {"process_name": "None", "AT": 0, "BT": 0, "ST": 0, "FT": 0}
        job_attr["process_name"] = process + 1
        job_attr["AT"] = int(input("Enter Arrival Time of Process %d : ->" % (process + 1)))
        job_attr["BT"] = int(input("Enter Burst Time of Process %d : ->" % (process + 1)))
        jobs.append(job_attr)
# _________________function to sort array   _________________________________________________________


def smallest(array_to_sort):
    smallest = array_to_sort[0]
    for process in range(0, len(array_to_sort)):
        if smallest["AT"] > array_to_sort[process]["AT"]:
            smallest = array_to_sort[process]
    return smallest


def sort_jobs(array_to_sort):
    sorted_array = []
    count = len(array_to_sort)
    for count in range(count):
        small = smallest(array_to_sort)
        sorted_array.append(small)
        array_to_sort.remove(small)
    return sorted_array
# __________________________________________________________________________________________________


def count_arrived_jobs(current_time, jobs_array):
    count = 0
    for job in jobs_array:
        if current_time >= job["AT"]:
                count = count + 1
    return count


def check_end(jobs_array):
    flag = False
    for job in jobs_array:
        if job["BT"] != 0:
            flag = True
            return flag
        else:
            flag = False
    return flag


def find_shortest_job(jobs_array, arrived_job_count):
    shortest = "None"
    if arrived_job_count == 1:
        if jobs_array[0]["BT"] > 0:
            shortest = jobs_array[0]
        return shortest
    for job in range(0, arrived_job_count-1):
        if job+1 < len(jobs_array):
            if jobs_array[job+1]["BT"] > jobs_array[job]["BT"]:
                if jobs_array[job]["BT"] > 0:
                    shortest = jobs_array[job]
                else:
                    if jobs_array[job+1]["BT"] > 0:
                        shortest = jobs_array[job+1]
            else:
                if jobs_array[job+1]["BT"] > 0:
                    shortest = jobs_array[job+1]
                else:
                    if jobs_array[job]["BT"] > 0:
                        shortest = jobs_array[job]
    return shortest


def s_r_t_f(jobs_array):
    current_time = 0
    arrived_job_count = count_arrived_jobs(current_time, jobs_array)
    running_process = find_shortest_job(jobs_array, arrived_job_count)  # for first process to run
    while running_process == "None":
        arrived_job_count = count_arrived_jobs(current_time, jobs_array)
        running_process = find_shortest_job(jobs_array, arrived_job_count)  # for first process to run
        current_time += 1
    current_time = int(running_process["AT"])   # shortest running job AT
    while check_end(jobs_array):
        current_running_job = jobs_array[jobs_array.index(running_process)]
        current_running_job["BT"] -= 1
        if current_running_job["ST"] == 0:
            if current_running_job["AT"] != 0:
                current_running_job["ST"] = current_time
        if current_running_job["BT"] == 0:
            current_running_job["FT"] = current_time + 1
        current_time += 1
        arrived_job_count = count_arrived_jobs(current_time, jobs_array)
        running_process = find_shortest_job(jobs_array, arrived_job_count)
        while running_process == "None":
            current_time += 1
            arrived_job_count = count_arrived_jobs(current_time, jobs_array)
            running_process = find_shortest_job(jobs_array, arrived_job_count)
            if check_end(jobs_array) == False:
                return jobs_array  # terminate
        print(jobs_array)


def display_result(jobs_array):
    print("\n\n\n-----------------------------------------------------------------------------------------")
    print("\t\t\t\t=process#=== A T ===== B T ===== S T ====== F T ====== W T =====  ")
    for job in jobs_array:
        print("\t\t\t\t==== ", job["process_name"], " ===== ", job["AT"], "=======", job["BT"], "=======", job["ST"], "=======", job["FT"], "========", job["FT"]-job["AT"]-job["BT"])
    print("-----------------------------------------------------------------------------------------")
    return 0


def combine_array(result_array, jobs_):
    for job in range(0, len(jobs_)):
        result_array[job]["BT"] = jobs_[job]["BT"]
    return result_array


def main():
    take_input()
    jobs_input = []
    jobs_temp = []
    for i in range(0, len(jobs)):
        job_attr = {"process_name": "None", "AT": 0, "BT": 0, "ST": 0, "FT": 0}
        job_attr["process_name"] = jobs[i]["process_name"]
        job_attr["AT"] = jobs[i]["AT"]
        job_attr["BT"] = jobs[i]["BT"]
        job_attr["ST"] = jobs[i]["ST"]
        job_attr["FT"] = jobs[i]["FT"]
        jobs_input.append(job_attr)

    for i in range(0, len(jobs)):
        jobs_temp.append(jobs[i])
    jobs_sorted = sort_jobs(jobs_temp)    # going to sort jobs according to there arrival time
    result_array = s_r_t_f(jobs_sorted)
    final_array = combine_array(result_array, sort_jobs(jobs_input))
    display_result(final_array)
main()
