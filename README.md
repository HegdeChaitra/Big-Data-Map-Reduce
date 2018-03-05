# Big-Data-Map-Reduce
Map reduce code for various tasks performed on parking violation data

Task 1
 Write a map-reduce job that finds all parking violations that have been paid, i.e., that do not
 occur in open-violations.csv.
 - Output: A key-value pair per line — use a “tab” to separate the key and the value, a comma
 and space between values — where
 
key = summons_number
values = plate_id, violation_precinct, violation_code, issue_date
Here’s a sample output with 1 key-value pair:
1307964308 GBH2444, 74, 46, 2016-03-07
- For generating output for the March 2016 data, run Hadoop using 2 reducers


Task 2
- Output: A key-value pair per line — use a “tab” to separate the key and the value — where key = violation_code
value = number of violations
Here’s a sample output with 1 key-value pair:
46 100 54 1000
- For generating output for the March 2016 data, run Hadoop using 2 reducers
 - Write a map-reduce job that finds all parking violations that have been paid, i.e., that do not
 occur in open-violations.csv.
 - Output: A key-value pair per line — use a “tab” to separate the key and the value, a comma
 and space between values — where
 
 - Write a map-reduce job that finds the distribution of the violation types in
 parking_violations.csv, i.e., for each violation code, the number of violations th
 
 
 Task 3
amount due in open violations for each
key = license_type
value = total, average
where total and average are rounded to 2 decimal places. Here’s a sample output with 1 key-value pair:
PAS 10000.00, 55.00
OMS 100000.00, 115.00
- For generating output for the March 2016 data, run Hadoop using 2 reducers ===================================================================


Task 4
- Write a map-reduce job that computes the total number of violations for vehicles registered in
 the state of NY and all other vehicles.
 - Output: 2 key-value pairs with one key-value pair per line — use a “tab” to separate the key
 and the value — following the key-value format below:
NY <total number>
- For generating output for the March 2016 data, run Hadoop using 2 reducers
 
 Task 5
 
  - Write a map-reduce job that finds the vehicle that has had the greatest number of violations
 (assume that plate_id and registration_state uniquely identify a vehicle).
 
 
 Task 6
 
 - Write a map-reduce job that
finds the top-20 vehicles
in terms of total violations (assume that
 plate id and registration state uniquely identify a vehicle)
 
 
 Task 7
  - In March 2016, the 5th, 6th, 12th, 13th, 19th, 20th, 26th, and 27th were weekend days (i.e.,
 Sat. and Sun.).
 Write a map-reduce job that, for each violation code, lists the average number of violations with
 that code issued per day on weekdays and weekend days. You may hardcode “8” as the
 number of weekend days and “23” as the number of weekdays in March 2016.
 
 Task 8
 - Write a map-reduce job that finds the distribution of terms for the Make and Color columns, i.e., for each value in those columns, how many times they appear in the column. Hint: you can use the wordcount algorithm we covered in class.
 
