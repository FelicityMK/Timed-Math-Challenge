import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    if operator == "+":
        answer = left + right
    elif operator == "-":
        answer = left - right
    else:  # operator == "*"
        answer = left * right

    expression = f"{left} {operator} {right}"
    return expression, answer

def main():
    num_wrong = 0
    print("Welcome to the Timed Math Challenge!")
    print("You will be given 10 math problems. Try to solve them as fast and accurately as you can.")
    input("Press Enter to start!")
    print("-" * 30)

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, correct_answer = generate_problem()
        while True:
            try:
                user_input = input(f"Problem #{i + 1}: {expr} = ")
                if int(user_input) == correct_answer:
                    print("Correct!\n")
                    break
                else:
                    print(" Wrong. Try again.")
                    num_wrong += 1
            except ValueError:
                print(" Please enter a valid number.")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("-" * 30)
    print(f" Well done! You finished in {total_time} seconds.")
    print(f"You made {num_wrong} wrong attempt(s).")
    print(f"Your final score: {TOTAL_PROBLEMS - num_wrong}/{TOTAL_PROBLEMS + num_wrong}")

if __name__ == "__main__":
    main()


