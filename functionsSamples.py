def money(*students: float) -> float:
    """
    Add together all the students' savings.

    Parameters:
        *students: Any number of savings amounts.

    Returns:
        The total amount saved.
    """
    result: float = 0
    for s in students:
        result += s
    return result


print("The students have saved", money(6, 8.5, 3, 9.25), "pounds")


def age() -> int:
    """
    Ask the user for their birth year and the current year.

    Returns:
        The user's age as an integer.
    """
    birth: int = int(input("What's your birth year? "))
    current: int = int(input("What is the current year? "))
    return current - birth


print("You will be", age(), "by the end of the year!")


def directions(light: str) -> None:
    """
    Print the correct action for a traffic light colour.

    Parameters:
        light: The traffic light colour ('red', 'yellow', or 'green').

    Returns:
        Nothing.
    """
    if light.lower() == "red":
        print("Stop")
    elif light.lower() == "yellow":
        print("Wait")
    elif light.lower() == "green":
        print("Go")
    else:
        print("Invalid colour")


colour: str = input("Enter a traffic light colour: ")
directions(colour)
