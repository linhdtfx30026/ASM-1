#Task 1:


def main():
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            with open(filename + ".txt", "r") as file:
                print(f"Successfully opened {filename}.txt")
                break
        except FileNotFoundError:
            print("File cannot be found.")

if __name__ == "__main__":
    main()

#Task 2:

def main():
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            with open(filename + ".txt", "r") as file:
                print(f"Successfully opened {filename}.txt")
                data = file.readlines()
                break
        except FileNotFoundError:
            print("File cannot be found.")
    
    print("**** ANALYZING ****")
    total_lines = len(data)
    invalid_lines = 0

    for line in data:
        line = line.strip()
        parts = line.split(',')
        
        # Kiểm tra xem 1 dòng có chứa danh sách 26 giá trị được phân tách bằng dấu phẩy không
        if len(parts) != 26:
            print(f"Invalid line of data: does not contain exactly 26 values:\n{line}")
            invalid_lines += 1
            continue
        
        # Kiểm tra xem giá trị đầu có hợp lệ (là StudentID hợp lệ hay k)
        student_id = parts[0]
        if not (student_id.startswith('N') and len(student_id) == 9 and student_id[1:].isdigit()):
            print(f"Invalid line of data: N# is invalid\n{line}")
            invalid_lines += 1
            continue
    
    valid_lines = total_lines - invalid_lines
    
    print("**** REPORT ****")
    print(f"Total valid lines of data: {valid_lines}")
    print(f"Total invalid lines of data: {invalid_lines}")

if __name__ == "__main__":
    main()

#Task 3:
def calculate_score(answer_key, student_answers):
    """Calculate the score based on the answer key and student answers."""
    score = 0
    for key, answer in zip(answer_key.split(','), student_answers):
        if answer == '':
            continue
        if answer == key:
            score += 4
        else:
            score -= 1
    return score

def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            with open(filename + ".txt", "r") as file:
                print(f"Successfully opened {filename}.txt")
                data = file.readlines()
                break
        except FileNotFoundError:
            print("File cannot be found.")
    
    print("**** ANALYZING ****")
    
    scores = []
    question_skipped = [0] * 25
    question_incorrect = [0] * 25
    total_lines = len(data)
    invalid_lines = 0

    for line in data:
        line = line.strip()
        parts = line.split(',')
        
        # Check if the line has exactly 26 values
        if len(parts) != 26:
            print(f"Invalid line of data: does not contain exactly 26 values:\n{line}")
            invalid_lines += 1
            continue
        
        # Check if the first value is a valid student ID
        student_id = parts[0]
        if not (student_id.startswith('N') and len(student_id) == 9 and student_id[1:].isdigit()):
            print(f"Invalid line of data: N# is invalid\n{line}")
            invalid_lines += 1
            continue
        
        # Calculate the score for the valid line
        student_answers = parts[1:]
        score = calculate_score(answer_key, student_answers)
        scores.append(score)
        
        # Update question statistics
        for i, (key, answer) in enumerate(zip(answer_key.split(','), student_answers)):
            if answer == '':
                question_skipped[i] += 1
            elif answer != key:
                question_incorrect[i] += 1

    # Report statistics
    valid_lines = total_lines - invalid_lines
    if valid_lines > 0:
        scores.sort()
        highest_score = scores[-1]
        lowest_score = scores[0]
        score_range = highest_score - lowest_score
        mean_score = round(sum(scores) / valid_lines, 2)
        median_score = round((scores[valid_lines // 2] + scores[(valid_lines - 1) // 2]) / 2, 2) if valid_lines % 2 == 0 else round(scores[valid_lines // 2], 2)
        high_scorers = sum(1 for score in scores if score > 80)
        
        # Report the results
        print("**** REPORT ****")
        print(f"Total valid lines of data: {valid_lines}")
        print(f"Total invalid lines of data: {invalid_lines}")
        print(f"Total student of high scores: {high_scorers}")
        print(f"Mean (average) score: {mean_score:.2f}")
        print(f"Highest score: {highest_score}")
        print(f"Lowest score: {lowest_score}")
        print(f"Range of scores: {score_range}")
        print(f"Median score: {median_score}")
        
        # Calculate and report questions skipped the most
        max_skipped = max(question_skipped)
        skipped_report = [f"{i + 1} - {question_skipped[i]} - {round(question_skipped[i] / valid_lines, 3)}" for i in range(25) if question_skipped[i] == max_skipped]
        print(f"Question that most people skip: {', '.join(skipped_report)}")
        
        # Calculate and report questions answered incorrectly the most
        max_incorrect = max(question_incorrect)
        incorrect_report = [f"{i + 1} - {question_incorrect[i]} - {round(question_incorrect[i] / valid_lines, 3)}" for i in range(25) if question_incorrect[i] == max_incorrect]
        print(f"Question that most people answer incorrectly: {', '.join(incorrect_report)}")
    else:
        print("No valid data to analyze.")

if __name__ == "__main__":
    main()

#Task 4:

def calculate_score(answer_key, student_answers):
    """Calculate the score based on the answer key and student answers."""
    score = 0
    for key, answer in zip(answer_key.split(','), student_answers):
        if answer == '':
            continue
        if answer == key:
            score += 4
        else:
            score -= 1
    return score

def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            with open(filename + ".txt", "r") as file:
                print(f"Successfully opened {filename}.txt")
                data = file.readlines()
                break
        except FileNotFoundError:
            print("File cannot be found.")
    
    print("**** ANALYZING ****")
    
    scores = []
    results = []
    question_skipped = [0] * 25
    question_incorrect = [0] * 25
    total_lines = len(data)
    invalid_lines = 0

    for line in data:
        line = line.strip()
        parts = line.split(',')
        
        # Check if the line has exactly 26 values
        if len(parts) != 26:
            print(f"Invalid line of data: does not contain exactly 26 values:\n{line}")
            invalid_lines += 1
            continue
        
        # Check if the first value is a valid student ID
        student_id = parts[0]
        if not (student_id.startswith('N') and len(student_id) == 9 and student_id[1:].isdigit()):
            print(f"Invalid line of data: N# is invalid\n{line}")
            invalid_lines += 1
            continue
        
        # Calculate the score for the valid line
        student_answers = parts[1:]
        score = calculate_score(answer_key, student_answers)
        scores.append(score)
        results.append((student_id, score))
        
        # Update question statistics
        for i, (key, answer) in enumerate(zip(answer_key.split(','), student_answers)):
            if answer == '':
                question_skipped[i] += 1
            elif answer != key:
                question_incorrect[i] += 1

    # Report statistics
    valid_lines = total_lines - invalid_lines
    if valid_lines > 0:
        scores.sort()
        highest_score = scores[-1]
        lowest_score = scores[0]
        score_range = highest_score - lowest_score
        mean_score = round(sum(scores) / valid_lines, 2)
        median_score = round((scores[valid_lines // 2] + scores[(valid_lines - 1) // 2]) / 2, 2) if valid_lines % 2 == 0 else round(scores[valid_lines // 2], 2)
        high_scorers = sum(1 for score in scores if score > 80)
        
        # Report the results
        print("**** REPORT ****")
        print(f"Total valid lines of data: {valid_lines}")
        print(f"Total invalid lines of data: {invalid_lines}")
        print(f"Total student of high scores: {high_scorers}")
        print(f"Mean (average) score: {mean_score:.2f}")
        print(f"Highest score: {highest_score}")
        print(f"Lowest score: {lowest_score}")
        print(f"Range of scores: {score_range}")
        print(f"Median score: {median_score}")
        
        # Calculate and report questions skipped the most
        max_skipped = max(question_skipped)
        skipped_report = [f"{i + 1} - {question_skipped[i]} - {round(question_skipped[i] / valid_lines, 3)}" for i in range(25) if question_skipped[i] == max_skipped]
        print(f"Question that most people skip: {', '.join(skipped_report)}")
        
        # Calculate and report questions answered incorrectly the most
        max_incorrect = max(question_incorrect)
        incorrect_report = [f"{i + 1} - {question_incorrect[i]} - {round(question_incorrect[i] / valid_lines, 3)}" for i in range(25) if question_incorrect[i] == max_incorrect]
        print(f"Question that most people answer incorrectly: {', '.join(incorrect_report)}")
    else:
        print("No valid data to analyze.")
    
    # Write results to file
    output_filename = f"{filename}_grades.txt"
    with open(output_filename, "w") as output_file:
        for student_id, score in results:
            output_file.write(f"{student_id},{score}\n")
    print(f"Results written to {output_filename}")

if __name__ == "__main__":
    main()

