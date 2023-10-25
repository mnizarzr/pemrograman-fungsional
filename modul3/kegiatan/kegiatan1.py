import re


def convert_weeks_to_minutes(weeks):
    def day(days):
        def hour(hours):
            def minute(minutes):
                total_minutes = (
                    (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
                )
                return total_minutes

            return minute

        return hour

    return day


data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]


result = [[int(match.group()) for match in re.finditer(r"\d+", week)] for week in data]

for v in result:
    week = v[0]
    day = v[1]
    hour = v[2]
    minute = v[3]
    print(convert_weeks_to_minutes(week)(day)(hour)(minute))
