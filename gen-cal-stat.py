import requests
import json
import datetime
import csv

# Set the API endpoint and the time range for which to retrieve calendar data
api_endpoint = "https://graph.microsoft.com/v1.0/me/calendarview"
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

# Set the authentication headers with your access token
headers = {
    "Authorization": "Bearer <YOUR_ACCESS_TOKEN_HERE>",
    "Content-Type": "application/json"
}

# Iterate through each month in the time range
while start_date <= end_date:
    month = start_date.month
    year = start_date.year
    
    # Set the start and end dates for the current month
    month_start_date = start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    month_end_date = (start_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1, hour=0, minute=0, second=0).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Set the query parameters to retrieve calendar data for the current month
    query_params = {
        "startDateTime": month_start_date,
        "endDateTime": month_end_date,
        "$select": "subject,isAllDay,organizer,start,end,responseStatus"
    }
    
    # Send a GET request to the API endpoint with the query parameters and headers
    response = requests.get(api_endpoint, headers=headers, params=query_params)
    
    # Parse the response data as JSON and summarize the meetings for the current month
    num_meetings = 0
    num_required_meetings = 0
    num_optional_meetings = 0
    total_required_time = 0
    total_optional_time = 0
    
    if response.status_code == 200:
        data = json.loads(response.text)
        for event in data["value"]:
            is_all_day = event.get('isAllDay', False)
            if not is_all_day:
                num_meetings += 1
                response_status = event['responseStatus']['response']
                start_time = datetime.datetime.fromisoformat(event['start']['dateTime']).timestamp()
                end_time = datetime.datetime.fromisoformat(event['end']['dateTime']).timestamp()
                duration = end_time - start_time

                if response_status == 'organizer':
                    num_required_meetings += 1
                    total_required_time += duration
                elif response_status == 'tentativelyAccepted':
                    num_optional_meetings += 1
                    total_optional_time += duration
    
    # Write the summary to a CSV file for the current month
    with open(f'meeting_summary_{year}_{month}.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Total Meetings', 'Required Meetings', 'Optional Meetings', 'Total Required Time (hrs)', 'Total Optional Time (hrs)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Total Meetings': num_meetings,
                         'Required Meetings': num_required_meetings,
                         'Optional Meetings': num_optional_meetings,
                         'Total Required Time (hrs)': round(total_required_time / 3600, 2),
                         'Total Optional Time (hrs)': round(total_optional_time / 3600, 2)})
