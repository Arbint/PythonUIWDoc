def GetPlayerInput(**kwargs) -> str:
    """Get player input from a selection of Options

    Args:
        message (str): the message to print out when asking
        options (list[str]): the list of options

    Returns:
        str: the option the player picked
    """
    
    msg = kwargs["message"]
    options = kwargs["options"]

    if not options:
        raise ValueError("Options list cannot be empty")

    playerInput = input(f"{msg}\n{options}:\n>>>")
    while playerInput not in options:
        print("invalid input!")
        playerInput = input(f"{msg}\n{options}:\n>>>")

    return playerInput

