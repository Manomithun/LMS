import frappe
import requests
from frappe import _


@frappe.whitelist()
def create_google_event(meeting_name):
    # Get the Meeting document
    print("Meeting Name:", meeting_name)
    meeting = frappe.get_doc("Meeting", meeting_name)

    # Get the Google Calendar account of the current user
    google_calendar = frappe.get_doc(
        "Google Calendar",
        {"user": frappe.session.user}
    )

    # Get a valid Google access token
    # Frappe's Google Calendar integration handles refreshing
    # the token using the stored refresh token.
    access_token = google_calendar.get_access_token()

    if not access_token:
        frappe.throw(
            _("Unable to get Google access token. Please connect Google Calendar again.")
        )

    # Google Calendar API endpoint
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"

    # Event data
    data = {
        "summary": meeting.subject,
        "description": meeting.description or "",
        "start": {
            "dateTime": meeting.start_datetime.isoformat(),
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": meeting.end_datetime.isoformat(),
            "timeZone": "Asia/Kolkata"
        }
    }

    # Create event in Google Calendar
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json=data
    )

    # Handle Google API errors
    if response.status_code not in (200, 201):
        frappe.throw(
            _("Google Calendar error: {0}").format(response.text)
        )

    # Convert Google response to Python dictionary
    google_event = response.json()

    # Store Google Event ID in Frappe
    meeting.db_set(
        "google_event_id",
        google_event["id"]
    )
    print("Google Event ID:", google_event["id"])
    return {
        "success": True,
        "google_event_id": google_event["id"],
        "google_event_url": google_event.get("htmlLink")
    }

# code for backup 
# import os
# import frappe
# import requests
# from frappe import _


# def upload_to_google_drive(file_path, access_token, folder_id):
#     file_name = os.path.basename(file_path)

#     metadata = {
#         "name": file_name,
#         "parents": [folder_id],
#     }

#     with open(file_path, "rb") as file:
#         response = requests.post(
#             "https://www.googleapis.com/upload/drive/v3/files",
#             params={
#                 "uploadType": "multipart"
#             },
#             headers={
#                 "Authorization": f"Bearer {access_token}",
#             },
#             files={
#                 "metadata": (
#                     None,
#                     frappe.as_json(metadata),
#                     "application/json; charset=UTF-8"
#                 ),
#                 "file": (
#                     file_name,
#                     file,
#                     "application/octet-stream"
#                 ),
#             },
#         )

#     if response.status_code not in (200, 201):
#         frappe.throw(
#             _("Google Drive upload failed: {0}")
#             .format(response.text)
#         )

#     return response.json()

# scheduler_events = {
#     "daily": [
#         "library_management.api.backup_to_google_drive"
#     ]
# }