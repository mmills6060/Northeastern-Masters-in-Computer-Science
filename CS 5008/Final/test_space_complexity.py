from memory_profiler import profile
import algorithms
import random

# Optimlal Total Storage -- the maximum total size of files that can be shared across all the 
# devices without exceeding any device's storage capacity. 
@profile
def allocate_files(files, devices):
    files.sort(reverse=True)  # Sort files in descending order
    devices.sort()  # Sort devices in ascending order

    allocation = [[] for _ in range(len(devices))]
    total_storage_used = [0] * len(devices)
    files_not_allocated = []

    for file_size in files:
        allocated = False
        for i, device_capacity in enumerate(devices):
            if device_capacity - total_storage_used[i] >= file_size:
                allocation[i].append(file_size)
                total_storage_used[i] += file_size
                allocated = True
                break
        if not allocated:
            files_not_allocated.append(file_size)
            print(f"Warning: File of size {file_size} cannot be allocated to any device.")

    return total_storage_used, allocation, files_not_allocated

@profile
def allocate_files_with_priority(files, devices, priority):
    files_with_priority = list(zip(files, priority))
    files_with_priority.sort(key=lambda x: x[1], reverse=True)

    devices.sort()

    allocation = [[] for _ in range(len(devices))]
    total_storage_used = [0] * len(devices)
    files_not_allocated = []

    for file_size, _ in files_with_priority:
        allocated = False
        for i, device_capacity in enumerate(devices):
            if device_capacity - total_storage_used[i] >= file_size:
                allocation[i].append(file_size)
                total_storage_used[i] += file_size
                allocated = True
                break
        if not allocated:
            files_not_allocated.append(file_size)
            print(f"Warning: File of size {file_size} cannot be allocated to any device.")

    return total_storage_used, allocation, files_not_allocated

@profile
def allocate_files_with_duplication(files, devices, duplication_factor):
    files_with_duplication = [(file_size, duplication_factor) for file_size in files]

    devices.sort()

    allocation = [[] for _ in range(len(devices))]
    total_storage_used = [0] * len(devices)
    files_not_allocated = []

    for file_size, duplication in files_with_duplication:
        allocated = False
        for _ in range(duplication):
            for i, device_capacity in enumerate(devices):
                if device_capacity - total_storage_used[i] >= file_size:
                    allocation[i].append(file_size)
                    total_storage_used[i] += file_size
                    allocated = True
                    break
            if allocated:
                break
        if not allocated:
            files_not_allocated.append(file_size)
            print(f"Warning: File of size {file_size} cannot be allocated to any device.")

    return total_storage_used, allocation, files_not_allocated

@profile
def allocate_files_with_file_sharing(files, devices, sharing_factor):
    files_with_sharing = [(file_size, sharing_factor) for file_size in files]

    devices.sort()

    allocation = [[] for _ in range(len(devices))]
    total_storage_used = [0] * len(devices)
    files_not_allocated = []

    for file_size, sharing in files_with_sharing:
        allocated = False
        for _ in range(sharing):
            for i, device_capacity in enumerate(devices):
                if device_capacity - total_storage_used[i] >= file_size:
                    allocation[i].append(file_size)
                    total_storage_used[i] += file_size
                    allocated = True
                    break
            if allocated:
                break
        if not allocated:
            files_not_allocated.append(file_size)
            print(f"Warning: File of size {file_size} cannot be allocated to any device.")

    return total_storage_used, allocation, files_not_allocated

@profile
def allocate_files_with_priority_duplication_file_sharing(files, devices, priority, duplication_factor, sharing_factor):
    files_with_priority = list(zip(files, priority))
    files_with_priority.sort(key=lambda x: x[1], reverse=True)

    devices.sort()

    allocation = [[] for _ in range(len(devices))]
    total_storage_used = [0] * len(devices)
    files_not_allocated = []

    for file_size, _ in files_with_priority:
        allocated = False
        for _ in range(duplication_factor):
            for _ in range(sharing_factor):
                for i, device_capacity in enumerate(devices):
                    if device_capacity - total_storage_used[i] >= file_size:
                        allocation[i].append(file_size)
                        total_storage_used[i] += file_size
                        allocated = True
                        break
                if allocated:
                    break
            if allocated:
                break
        if not allocated:
            files_not_allocated.append(file_size)
            print(f"Warning: File of size {file_size} cannot be allocated to any device.")

    return total_storage_used, allocation, files_not_allocated
@profile
def main():
    num_files = 100000
    file_sizes = [random.randint(1, 500) for _ in range(num_files)]
    num_devices = 10
    storage_sizes = [random.randint(250000, 10000000) for _ in range(num_devices)]
    duplication_factor = 2
    sharing_factor = 2
    priority = [random.randint(1, 1000000) for _ in range(num_files)]

    allocation1 = allocate_files(file_sizes, storage_sizes)
    allocation2 = allocate_files_with_duplication(file_sizes, storage_sizes, duplication_factor)
    allocation3 = allocate_files_with_file_sharing(file_sizes, storage_sizes, sharing_factor)
    allocation4 = allocate_files_with_priority(file_sizes, storage_sizes, priority)
    allocation5 = allocate_files_with_priority_duplication_file_sharing(file_sizes, storage_sizes, priority, duplication_factor, sharing_factor)


if __name__ == '__main__':
    main()
