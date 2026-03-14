from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_each_difficulty_uses_correct_range():
    # Bug: new game always used random.randint(1, 100) regardless of difficulty.
    # Fix: get_range_for_difficulty must return distinct ranges per difficulty.
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")

    assert easy_high == 20, f"Easy range should be 1-20, got 1-{easy_high}"
    assert normal_high == 50, f"Normal range should be 1-50, got 1-{normal_high}"
    assert hard_high == 100, f"Hard range should be 1-100, got 1-{hard_high}"