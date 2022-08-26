from gpysheets import QuerySheet

SAMPLE_SHEET_ID = "1otGm8lRfXGOX5WbOEZx4S-swLQesn9PkQnGKxe89eFw"
SAMPLE_SHEET_NAME = "game_results"


def test_query_sheet_gets_correct_column_names():
    query_result_map = QuerySheet.query_sheet(
        SAMPLE_SHEET_ID, SAMPLE_SHEET_NAME)
    expected_columns = ["date", "wordle_number", "correct_word", "guesses"]
    actual_columns = query_result_map["columns"]
    assert(expected_columns == actual_columns)


def test_query_sheet_gets_the_correct_data():
    query_result_map = QuerySheet.query_sheet(
        SAMPLE_SHEET_ID,
        "guesses"
    )
    expected_data = [
        ["08/26/2022", "1", "TRUCE", "gray", "green", "gray", "gray", "gray", "0"],
        ["08/26/2022", "2", "BRAIN", "gray", "green",
            "gray", "yellow", "yellow", "0"],
        ["08/26/2022", "3", "IRONY", "green",
            "green", "green", "green", "green", "1"]
    ]
    actual_data = query_result_map["data"]
    assert(expected_data == actual_data)
