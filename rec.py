def explain_recursion(depth, current=1, story_type=1, visual_indent=True):
    """
    A function to demonstrate recursion with user-defined depth and story types.

    Args:
        depth (int): The total depth of recursion.
        current (int): The current recursion level (default is 1).
        story_type (int): The type of story to use for recursion (default is 1).
        visual_indent (bool): Whether to visually indent based on recursion depth.
    """
    indent = "  " * (current - 1) if visual_indent else ""

    if current > depth:
        if story_type == 1 or story_type == 4:
          return f"{indent}With those examples, I understand recursion.\n" * depth
        elif story_type == 2:
            return f"{indent}Now, the student understand recursion from the teacher\n" * depth
        elif story_type == 3:
            return f"{indent}Through asking, how to understand recursion is clear\n" * depth

    if story_type == 1:
        story = (
            f"{indent}What is recursion?\n"
            f"{indent}Recursion is just: \n"
        )
    elif story_type == 2:
        story = (
            f"{indent}There was a student who asked their teacher: What is recursion?\n"
            f"{indent}The teacher replied: Recursion is when: \n"
        )
    elif story_type == 3:
        story = (
            f"{indent}How do we understand recursion?\n"
            f"{indent}By asking ourselves again: \n"
        )
    else:
        story = (
            f"{indent}Custom recursion story: What happens next at level {current}?\n"
            f"{indent}What happens at level {current + 1}?\n"
        )

    return story + explain_recursion(depth, current + 1, story_type, visual_indent)

def main():
    print("Welcome to the Enhanced Recursion Explorer!")
    try:
        depth = int(input("Enter the number of recursion layers (1-50): "))
        if depth < 1 or depth > 50:
            print("Please enter a number between 1 and 50.")
            return

        print("\nChoose a story type:")
        print("1. The self-answering question")
        print("2. The teacher and student recursion tale")
        print("3. Exploring understanding through recursion")
        print("4. Custom story")

        story_type = int(input("Enter your choice (1-4): "))
        if story_type < 1 or story_type > 4:
            print("Invalid story type. Please enter a number between 1 and 4.")
            return

        if story_type == 4:
            custom_question = input("Enter your custom story question: ")
            custom_self_answer = input("Enter the self-answer for your custom story: ")
            custom_resolution = input("Enter the resolution for your custom story: ")

            def custom_recursion(depth, current=1, visual_indent=True):
                indent = "  " * (current - 1) if visual_indent else ""
                if current > depth:
                    return f"{indent}{custom_resolution}\n" * depth
                return (
                    f"{indent}{custom_question}\n"
                    f"{indent}{custom_self_answer}\n"
                    + custom_recursion(depth, current + 1, visual_indent)
                )

            global explain_recursion
            explain_recursion = custom_recursion

        visual_indent = input("Do you want visual indentation? (yes/no): ").strip().lower() == "yes"

        step_by_step = input("Do you want to explore recursion step-by-step? (yes/no): ").strip().lower() == "yes"

        print("\nRecursion starts here:\n")
        if step_by_step:
            for i in range(1, depth + 1):
                print(explain_recursion(i, story_type=story_type, visual_indent=visual_indent))
                input("Press Enter to continue...")
        else:
            output = explain_recursion(depth, story_type=story_type, visual_indent=visual_indent)
            print(output)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
