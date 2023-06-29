from gui import GUI
from CSV_reader import CSV
from EXCEL_missing_drawings import missing_drawings_from_excel
from EXCEL_missing_orders import EXCEL_missing_orders


# Choose separator for search
csv_sep = "|"


# run function - window with selection window
result = GUI.ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP",
        "Solid Works Files",
        "Braki rysunków w Excel",
        "Braki zamówień w Excel"],
    [";",
     ","],
    [3, 2, 1, 4, 5]
)

# CSV settings
csv_delimiter = str(result[1])
part_column = int(result[2]-1)


# EXCEL_missing_drawings
if result[0] == "Braki rysunków w Excel":
    missing_drawings_from_excel()

# EXCEL_missing_orders
elif result[0] == "Braki zamówień w Excel":
    EXCEL_missing_orders()


# CSV_reader
elif result[0] == "Solid Works Files" or result[0] == "Files with revision: PDF, DXF, STP":
    CSV.read_BOM_from_CSV(result, csv_delimiter, csv_sep, part_column)
