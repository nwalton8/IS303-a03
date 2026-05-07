'''
Noah Walton
IS303-A03

Grade Report:
Collects student scores and produces a grade summary

Inputs:
- Student name and list of their scores

Processes:
- Accumulator: Calculate total score
- Min/Max: Find highest and lowest scores
- Accumulator: Count scores above threshold
- Transform: Clean the input names (remove extra spaces, capitalize)

Outputs:
- Student name
- Total score
- Highest score
- Lowest score
- Count of scores above threshold
'''
# Input:

name = input("Enter student name: ").strip().title()
threshold = float(input("Enter the passing score threshold: "))    
scores = []
score = 0
test_num = 1
while score != "done":
    score = input(f"Enter score for {name}, test {test_num}, or 'done' to finish: ")
    if score.lower().strip() == "done":
        break
    elif not score.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a numeric value for the score, or 'done' to finish.")
    elif float(score) < 0 or float(score) > 100:
        print("Invalid score. Please enter a value between 0 and 100, or 'done' to finish.")
    else:
        scores.append(float(score))
        test_num += 1

# Process:
if not scores:
    print("No scores entered. Goodbye!")
    exit()
above_threshold_count = 0
highest_score = lowest_score = scores[0]  # Initialize to the first score of the student
amount_scores = len(scores)
total_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score
    if score >= threshold:
        above_threshold_count += 1
    total_score += score    
    
# Output:
print("\nGrade Report:")
print(f"Hello, {name}. Your total score is {total_score:.2f}.")
print(f"Your highest score is {highest_score:.2f} and your lowest score is {lowest_score:.2f}.")
print(f"You have {above_threshold_count} / {amount_scores} scores above or equal to the threshold of {threshold:.2f}.")

# End of program