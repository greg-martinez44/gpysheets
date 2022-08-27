from googleapiclient.errors import HttpError

try:
    from . import Connection
except ImportError:
    from Connection import Connection


class QuerySheet:
    """
    For reference docs, see https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.html
    """

    SERVICE = Connection().get_service()

    # This works by just making an arbitrarily large range to cover most sheets...
    # This should be updated to use the maximum dimensions of the sheet,
    # but the documentation isn't very clear.
    FULL_SHEET_RANGE = "A1:Z400000"

    @classmethod
    def query_sheet(cls, sheet_id, sheet_name=""):

        if sheet_name != "":
            range = f"{sheet_name}!{QuerySheet.FULL_SHEET_RANGE}"
        else:
            range = QuerySheet.FULL_SHEET_RANGE
        try:
            service = QuerySheet.SERVICE

            # Call the Sheets API
            sheet = service.spreadsheets()

            result = sheet.values().get(spreadsheetId=sheet_id,
                                        range=range).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            columns = []
            data = []
            columns = values[0]
            for row in values[1:]:
                data.append(row)
            return {
                "columns": columns,
                "data": data
            }
        except HttpError as err:
            print(err)
