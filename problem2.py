def calculate_average(score1, score2, score3):
    return round(sum((score1, score2, score3))/3, 2)

def drop_lowest(score1, score2, score3):
    max_score = max(score1, score2, score3)
    min_score = min(score1, score2, score3)
    if score1 < max_score and score1 > min_score:
        medium_score = score1
    elif score2 < max_score and score2 > min_score:
        medium_score = score2
    elif score3 < max_score and score3 > min_score:
        medium_score = score3

    return round(sum((max_score, medium_score)) / 2, 2)

def calculate_weighted(assignments, midterm, final):
    weighted_assignments = assignments * 30/100
    weighted_midterm = midterm * 30 / 100
    weighted_final = final * 40 / 100
    return round(weighted_assignments, 2) + round(weighted_midterm, 2) + round(weighted_final, 2)

def determine_grade(average):
    if 100 >= average >= 90:
        return 'A'
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average < 60:
        return "F"

def needs_improvement(current_avg, target_grade):
    if target_grade == 'A':
        if current_avg < 90:
            return True
        else:
            return False
    elif target_grade == 'B':
        if current_avg < 80:
            return True
        else:
            return False
    elif target_grade == 'C':
        if current_avg < 70:
            return True
        else:
            return False
    elif target_grade == 'D':
        if current_avg < 60:
            return True
        else:
            return False
        
print("\n\nSTUDENT GRADE CALCULATOR")
print("========================================")
print(f"Assignment Scores: 85, 78, 92")
print("Midterm Score: 88\n"
"Final Score: 82\n"
"----------------------------------------")
average = calculate_average(85, 78, 92)
print(f"Regular Assignment Average: {average:.2f}")

average_with_drop = drop_lowest(85, 78, 92)
print(f"Average with Lowest Dropped: {average_with_drop:.2f}")
print(f"Using Better Average: {average_with_drop:.2f}\n")

weighted_course_average = calculate_weighted(average_with_drop, 88, 82)
print(f"Weighted Course Average: {weighted_course_average:.2f}")

letter_grade = determine_grade(weighted_course_average)
print(f"Letter Grade: {letter_grade}\n")

needs_improve = "Yes" if needs_improvement(weighted_course_average, 'A') else "No"
print(f"Needs improvement for an 'A': {needs_improve}")

points_needed = 90 - weighted_course_average if needs_improvement(weighted_course_average, 'A') else 0
print(f"Points needed: {points_needed:.2f}")

current_grade = determine_grade(weighted_course_average)
print(f"Already meets or exceeds '{current_grade}' grade requirement\n\n")
