

def test_evaluations_are_chronological(evaluation_history_page):
    evaluation_entries = evaluation_history_page.get_evaluation_entries()
    assert evaluation_history_page.evaluations_are_chronological(
        evaluation_entries), "Evaluations are not displayed in chronological order."


def test_search_currently_cycle(navigate_and_search_history):
    evaluation_history_page, cycle_date = navigate_and_search_history
    evaluation_entries = evaluation_history_page.get_evaluation_entries()
    assert evaluation_entries, f"No evaluation entries found for the cycle '{cycle_date}'."


def test_view_closed_evaluation_by_date(navigate_and_search_history):
    evaluation_history_page, cycle_date = navigate_and_search_history
    is_viewed = evaluation_history_page.view_evaluation_entry_by_date(cycle_date)
    assert is_viewed, "No closed evaluation entry was found or the 'View' button was not clickable."
