from gui import GUI
from CSV_reader import CSV
from EXCEL_missing_drawings import missing_drawings_from_excel
from EXCEL_missing_orders import mega_def


# Choose separator for search
csv_sep = " | "


# run function - window with selection window
result = GUI.ask_multiple_choice_question(
    "PDM search engine",
    ["Files with revision: PDF, DXF, STP - from CSV",
        "Solid Works Files - from CSV",
        "Braki rysunków w Excel",
        "Braki zamówień obróbki w Excel"],
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

# EXCEL_missing_orderss
elif result[0] == "Braki zamówień obróbki w Excel":
    mega_def([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16], 5)

elif result[0] == "Braki zamówień handlówki w Excel":
    mega_def([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16], 8)

# CSV_reader
elif result[0] == "Solid Works Files - from CSV" or result[0] == "Files with revision: PDF, DXF, STP - from CSV":
    CSV.read_BOM_from_CSV(result, csv_delimiter, csv_sep, part_column)
