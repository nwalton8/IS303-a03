# Input:
students =[]
add_student = ""
above_threshold_count = 0
below_threshold_count = 0
threshold = float(input("Enter the passing score threshold: "))
num_tests = int(input("Enter the number of tests: "))
while add_student.lower() != "done":
    name = input("Enter student name (or 'done' to finish): ").strip().title()
    if name.lower() == "done":
        break
    scores = []
    i = 0
    while i < num_tests:
        score = float(input(f"Enter score for {name}, test {i + 1}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a value between 0 and 100.")
            score = float(input(f"Enter score for {name}, test {i + 1}: "))
        scores.append(score)
        i += 1
    students.append({'name': name, 'scores': scores})

# Process:
if not students:
    print("No students entered.")
    exit()
highest_score = students[0]['scores'][0]  # Initialize to the first score of the first student
lowest_score = highest_score   # Initialize to the first score of the first student

num_students = len(students)
i = 0
while i < num_students:
    total_score = 0
    final_score = 0
    total_score = sum(students[i]['scores'])
    final_score = total_score / num_tests
    students[i]['total'] = total_score
    students[i]['average'] = final_score
    for score in students[i]['scores']:
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score
        if score >= threshold:
            above_threshold_count += 1
        else:
            below_threshold_count += 1
    i += 1
    
# Output:
print("\nGrade Report:")
i = 0
while i < num_students:
    print(f"{students[i]['name']}: Total Score = {students[i]['total']:.2f}, Average Score = {students[i]['average']:.2f}")
    i += 1
print(f"\nHighest Score: {highest_score:.2f}")
print(f"Lowest Score: {lowest_score:.2f}")
print(f"Number of scores above or equal to {threshold}: {above_threshold_count}/{below_threshold_count + above_threshold_count}")

#end of program