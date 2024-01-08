limit_bad_tries = int(input())
current_task_name = input()
bad_tries = 0
number_of_tasks = 0
total_score = 0
last_problem = ""
is_failed = True

while current_task_name != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_tries += 1
        if bad_tries == limit_bad_tries:
            is_failed = False
            break
    number_of_tasks += 1
    total_score += current_grade
    last_problem = current_task_name
    current_task_name = input()
if is_failed:
    average_score = total_score / number_of_tasks
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_tries} poor grades.")

