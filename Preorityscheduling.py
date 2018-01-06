print("------------------------Priority Scheduling Non Preempting-------------------")
t_count = int(input("Enter Total Number of Process : -> "))
jobs = []


def take_input():
    for process in range(0, t_count):
        at = 0
        bt = 0
        job_attr = {"process_name": "None", "AT": 0, "BT": 0, "ST": 0, "FT": 0, "PT": 0}
        job_attr["process_name"] = process + 1
        job_attr["AT"] = int(input("Enter Arrival Time of Process %d : ->" % (process + 1)))
        job_attr["BT"] = int(input("Enter Burst Time of Process %d : ->" % (process + 1)))
        job_attr["PT"] = int(input("Enter Priority of Process %d : ->" % (process + 1)))
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
        if job["FT"] == 0:
            flag = True
            return flag
        else:
            flag = False
    return flag


def find_prioritized_job(jobs_array, arrived_job_count):
    prioritized = "None"
    if arrived_job_count == 1:
        if jobs_array[0]["FT"] == 0:
            prioritized = jobs_array[0]
        return prioritized
    for job in range(0, arrived_job_count-1):
        if job+1 < len(jobs_array):
            if jobs_array[job+1]["PT"] > jobs_array[job]["PT"]:
                if jobs_array[job]["FT"] == 0:
                    prioritized = jobs_array[job]
                else:
                    if jobs_array[job+1]["FT"] == 0:
                        prioritized = jobs_array[job+1]
            else:
                if jobs_array[job+1]["FT"] == 0:
                    prioritized = jobs_array[job+1]
                else:
                    if jobs_array[job]["FT"] == 0:
                        prioritized = jobs_array[job]
    return prioritized


def p_r_scheduling(jobs_array):
    current_time = 0
    while check_end(jobs_array):
        arrived_job_count = count_arrived_jobs(current_time, jobs_array)
        running_job = find_prioritized_job(jobs_array, arrived_job_count)
        running_job["ST"] = current_time
        current_time += running_job["BT"]
        running_job["FT"] = current_time
        if check_end(jobs_array) == False:
            return jobs_array


def display_result(jobs_array):
    print("\n\n\n-----------------------------------------------------------------------------------------")
    print("\t\t\t\t=process#=== A T ===== B T ===== S T ====== F T ====== W T =====  ")
    for job in jobs_array:
        print("\t\t\t\t==== ", job["process_name"], " ===== ", job["AT"], "=======", job["BT"], "=======", job["ST"], "=======", job["FT"], "========", job["ST"]-job["AT"])
    print("-----------------------------------------------------------------------------------------")
    return 0


def main():
    take_input()
    jobs_sorted = sort_jobs(jobs)
    copy_jobs_sorted = []
    # copying to preserve it
    for i in range(0, len(jobs)):
        job_attr = {"process_name": "None", "AT": 0, "BT": 0, "ST": 0, "FT": 0, "PT": 0}
        job_attr["process_name"] = jobs[i]["process_name"]
        job_attr["AT"] = jobs[i]["AT"]
        job_attr["BT"] = jobs[i]["BT"]
        job_attr["ST"] = jobs[i]["ST"]
        job_attr["FT"] = jobs[i]["FT"]
        job_attr["PT"] = jobs[i]["PT"]
        copy_jobs_sorted.append(job_attr)
    # copied and preserved as records
    display_result(p_r_scheduling(jobs_sorted))
main()
