# creating random timestamps within the last 5 years
with open("/Users/pattaponpuapanichya/Documents/GitHub/Hack-The-Burgh-2023/resources/timestamps.txt") as file:
    timestamps = file.readlines()
    timestamps_int = []
    for time in timestamps:
        timestamps_int.append(int(time))
