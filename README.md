# SolidWorks BOM.scv tool for fast search in PDM

ETL process with GUI which extracts data from .csv file and merge proper data from file to one string which can be used to search multiple files in File Explorer in one task.


<!--
<p align="center">
<img src="README_gif_kanban.gif" width="400" height="200">
</p>  
 algo tu dać gifa ;) -->

## Technologies
* Python 3.8
* CSV files

## Ghraphical Explanation of working
<!-- grafic_explain.png -->
<p align="center">
<img src="README_grafic_explain.png">
</p>

<p align="center">
1. Export BOM form SolidWorks to CSV file
</p>
<p align="center">
2. Select file type to search
</p>
<p align="center">
3. Select proper delimiter used in csv file
</p>
<p align="center">
4. Select the number of ID part column
</p>
<p align="center">
4. Accept settings  and select .csv file
</p>
<p align="center">
4. Merged data string copied to clipboard and ready for used
</p>


### Purpose of application
The application was developed to reduce the time of searching drawing documentation in SolidWorks/PDM and to improve the quality of exchange of documents between departments in the company.
### Achievements
1. Saves for every employees at least eight hour in every project in my company for searching files to let in on production.
2. Files are not manually selected for production, reducing human errors and the cost of mistakes.
### Note
The application was design to cooperate with Bills of materials exported from SolidWorks  designed specifically for a specific company.

