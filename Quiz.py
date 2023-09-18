def create_quiz():
    quiz = {}
    num_questions = int(input("Enter the number of questions: "))

    for _ in range(num_questions):
        question = input("Enter a question: ")
        answer = input("Enter the answer: ")
        quiz[question] = answer

    return quiz

def take_quiz(quiz):
    score = 0

    for question, answer in quiz.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)

    print("Quiz complete! You scored", score, "out of", len(quiz))

if __name__ == "__main__":
    print("Welcome to the Quiz Program!")

    option = input("Would you like to create a quiz (c) or take a quiz (t)? ")

    if option.lower() == "c":
        quiz = create_quiz()
    elif option.lower() == "t":
        quiz = {
            "What is the capital of France?": "Paris",
            "Which planet is known as the Red Planet?": "Mars",
            "What is 7 times 8?": "56"
        }
    else:
        print("Invalid option. Exiting.")
        exit()

    take_quiz(quiz)
