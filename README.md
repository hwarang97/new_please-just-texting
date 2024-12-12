# Please Just Texting!
[image]   
A Slack plugin that simplifies Google Calendar mangement through text commands. No need to visit the Google Calnedar site. Just type your meeting details in Slack, and the plugin will automaticallyt manage your calendar.

## Architecture
[image]   

## Installation
TBD

## Object
- [ ] Manage Google Calendar by command in Slack
- [ ] Google account authentication by OAuth2
- [ ] Return response message

## Tech Stack
This project is built with:
|Category              |Technologies        |
| :------------------- | :-------------------- |
|**Framework**         |FastAPI, Jinja2        |
|**Database**          |PostgreSQL, Alembic    |
|**Containerization**  |Docker                 |
|**Data Validation**   |Pydantic               |
|**Code Quality**      |isort, black, flake8   |

## Requirements
1. Create Events
   - Input Example
     - /app text...
   - Process
     - Use OpenAI API to extract event details (date, time, title, location) from the text.
     - Add the extracted event to Google Calendar useing the Googld Calendar API.
   - Output
     - A confirmation message in Slack
     - "The event [Meeting name] has been created for [date] in the [location]"
2. Update Events
   - Input Example
      - /app text...
   - Process
      - Identify the event to be updated in Google Calendar.
      - Update the date, time, or other details based on the text input.
   - Output
      - A conformation message in Slack
      - "The event [Meeting name] has been updated"
3. Delete Events
   - Input Example
      - /app text...
   - Process
      - Identify the event to be removed in Google Calendar.
      - Remove the event based on the text input.
   - Output
      - A conformation message in Slack
      - "The event [Meeting name] has been deleted"
4. Google Account Authentication
   - Process
      - Use Google OAuth2 to autenticate users and link their Google Calendar account.
      - Store the OAuth2 token for API request.
   - Output
      - Provide a link in Slack for the user to authenticate with Google account.
      - "Please authenticate your Google Calendar account by clicking [link]"
5. Error handling
   - Invalid input
      - Example1: Input text doesn't have sufficient details.
   - Output
      - "Need more infomation for action"
