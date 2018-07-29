# Spell Checker for ArcMap
This script will find and fix spelling errors in an ArcMap attribute tables. It will iterate through every word in every record of each string field until it comes to one that Enchant, a spellchecking library for Python, does not recognize. The user will then be asked if they would like to change the word to a suggested new one or keep as is. 

# Prerequistes
ArcMap 10.0+
<br>
Modules: arcpy, enchant

# Installing
1. Install modules listed above
2. Change Line #8 after 'arcpy.env.workspace =' to the address of the folder or gdb location where your dataset is located
3. Change Line #10 after 'fc =' to the address of your dataset

# Built With
Enchant: A spell-checking library for Python that finds misspelled words and offers suggestions for corrections: https://github.com/rfk/pyenchant

ArcGIS/ArcPy: https://www.esri.com/en-us/arcgis/about-arcgis/overview





