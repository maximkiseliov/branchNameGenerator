import pyperclip


def get_story_number():
    return input("Story number: ")


def get_story_summary():
    return input("Story summary: ")


def format_story_summary(story_summary):
    formatted_summary = story_summary.title().replace(" ", "")
    return ''.join(e for e in formatted_summary if e.isalnum())


def create_branch_name(story_number, normalized_summary):
    return f'{story_number}_{normalized_summary}'


def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Branch name: '{text}' copied to clipboard\n")


def ask_for_another_branch():
    while True:
        one_more = input("One more branch name (Y/N)?: ").upper()
        if one_more == "Y":
            return True
        elif one_more == "N":
            return False


def branch_name_creator():
    story_number = get_story_number()
    story_summary = get_story_summary()
    normalized_summary = format_story_summary(story_summary)
    branch_name = create_branch_name(story_number, normalized_summary)
    copy_to_clipboard(branch_name)
    return ask_for_another_branch()


if __name__ == "__main__":
    while branch_name_creator():
        pass
