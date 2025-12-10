minutes = int(input("Минуты: "))


def format_time(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"{hours}:{remaining_minutes:02d}")


format_time(minutes)
