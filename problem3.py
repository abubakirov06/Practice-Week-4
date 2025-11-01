def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60

def total_seconds(hours, minutes, seconds):
    hour_to_minute = hours * 60
    total_minutes = minutes + hour_to_minute
    seconds_total = total_minutes * 60 + seconds
    return seconds_total

def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} hours and {minutes} minutes"

def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes = available_hours * 60
    total_task_minutes = task_hours * 60 + task_minutes
    if total_task_minutes <= available_minutes:
        return True
    else:
        return False
    
def schedule_summary(task_name, hours, minutes):
    total_time_minutes = hours * 60 + minutes
    total_time_seconds = total_time_minutes * 60
    print(f"Task: {task_name}")
    print(f"  Duration: {hours} hours, {minutes} minutes")
    if hours > 0:
        print(f"  Total Minutes: {total_time_minutes:.1f}")
        print(f"  Total Seconds: {total_time_seconds:.1f}\n")
    else:
        print(f"  Total Minutes: {total_time_minutes:.0f}")
        print(f"  Total Seconds: {total_time_seconds:.0f}\n")

print("\n\nTIME CONVERTER AND SCHEDULER\n"
"========================================")
hours = 2.5
hours_in_minutes = hours_to_minutes(hours)
print(f"Converting {hours} hours to minutes: {hours_in_minutes:.1f} minutes\n")

hours, minutes, seconds = 1, 45, 30
total_second = total_seconds(hours, minutes, seconds) 
print(f"Total seconds for {hours} hour, {minutes} minutes, {seconds} seconds: {total_second} seconds\n")

format_minutes = 200
formatted_time = format_time(total_minutes = format_minutes)
print(f"Formatting {format_minutes} minutes: {formatted_time}\n")

available_hours, task_hours, task_minutes = 3.5, 3, 20
print(f"Can a {task_hours} hour {task_minutes} minute task fit in {available_hours} hours?")
print(f"{"  Yes, the task fits!" if can_fit_task(available_hours, task_hours, task_minutes) else "  No, the task doesn't fit!"}")

print("\nSCHEDULE SUMMARIES:\n"
"------------------------------")

schedule_summary(task_name = "Study", hours = 2, minutes = 30)
schedule_summary(task_name = "Exercise", hours = 0, minutes = 45)

