# Repo Name: team-rotating-schedule
* A simple python program that generates daily rotating schedule for a team.
* Most parts of the program are generated by chatGPT.

# General
This program uses the calendar, holidays, and csv modules to get the number of days in the month of February 2023, the day of the week for each day, a list of holidays in Canada, and the staff members who are taking planned vacations. The planned vacations are stored in a CSV file, with the date and person in separate columns. The is_vacation function checks if a person is on vacation for a specific day. It then creates a schedule by assigning each team member to a day in a round-robin fashion, where each team member is assigned to a day before the next team member, but skips over weekends, and holidays in Canada. The schedule is then printed out, showing which team member is on business for each week day.

# Additional 1
This program is similar to the previous program, but now it writes the generated schedule to a CSV file named "schedule.csv". The first row of the file contains the header "Date" and "Person". Each subsequent row contains the date and the person assigned to that date. After the schedule is written to the file, the program prints a message indicating that the schedule has been printed to the file.

# Additional 2
This program is similar to the previous program, but instead of defining the team list directly in the code, it reads the list of team members from a text file named "team.txt". Each line in the file should contain the name of a team member. After reading the list of team members, the program proceeds with generating the schedule in the same manner as the previous program. Finally, the schedule is written to a CSV file named "schedule.csv".

# Additional 3
Please print the generated schedule to a CSV file named "schedule.csv".
Please read team from a text file named "team.txt".
This program  reads additional holidays from a text file named "additional_holidays.txt". Each line in the file should contain a date in the format "YYYY-MM-DD".
This program also writes the output to a SQLite database file named "schedule.db". The SQLite database is created using the sqlite3 module, and the schedule is stored in a table named "schedule". The table is created if it does not already exist, and the schedule is inserted as records into the table. 

# License: GNU GPL v3

