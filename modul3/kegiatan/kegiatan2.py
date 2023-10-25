import re

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

result = [list(map(int, filter(str.isdigit, week.split()))) for week in data]

print(result)
