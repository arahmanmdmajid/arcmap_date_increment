# arcmap_date_increment
A script for calculating date at an increment of a day in ArcMap field calculator
Procedure
1. Create a new Date field.
2. Right-click the new field and select Field Calculator.
3. Set the Parser to Python.
4. Check the check box for Show Codeblock.
5. Copy and paste the script.py code the Pre-Logic Script Code
6. Paste the following code in the smaller box below the Pre-Logic Script Code:
      autoIncrement()
7. Click OK.


You can further filter the date as follows for each months,


All points -> "date_time" >= date '2022-01-17' AND "date_time" <= date '2022-06-17'

JAN -> "date_time" <= date '2022-01-31'

FEB -> "date_time" > date '2022-01-31' AND "date_time" <= date '2022-02-28'

MAR -> "date_time" > date '2022-02-28' AND "date_time" <= date '2022-03-31'

APR -> "date_time" > date '2022-03-31' AND "date_time" <= date '2022-04-30'

MAY -> "date_time" > date '2022-04-30' AND "date_time" <= date '2022-05-31'


To understand the increment code, here is a short sample
https://support.esri.com/en/technical-article/000011137
