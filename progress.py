#!python
import re
import datetime
with open("Readme.md", "r") as f:
    readme = f.read()
durations = re.findall("\[\d{2}:\d{2}:\d{2}\]", readme)
seconds_tot = 0
for dur in durations:
    h = int(dur[1:3])
    m = int(dur[4:6])
    s = int(dur[7:9])
    seconds_tot += h * (60**2) + m * 60 + s

print("Total time duration:", datetime.timedelta(seconds=seconds_tot, ))
print("~~~~ Watched videos ~~~~")
completed_vids = [x.replace("~~", "") for x in re.findall("~~.*~~", readme)]
for vid in completed_vids:
    print(vid)

seconds_done = 0
for dur in durations[len(completed_vids):]:
    h = int(dur[1:3])
    m = int(dur[4:6])
    s = int(dur[7:9])
    seconds_done += h * (60**2) + m * 60 + s
print("Watched time duration:", datetime.timedelta(seconds=seconds_done))

print(f"Completion rate: {round( 100 * seconds_done / seconds_tot)}%")




