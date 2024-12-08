# Please Just Texting!
[image]   
A Slack plugin that simplifies Google Calendar mangement through text commands. No need to visit the Gogle Calnedar site. Just type your meeting details in Slack, and the plugin will automaticallyt manage your calendar.

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
| :------------------- | :----------------- |
|**Framework**         |FastAPI, Jinja2     |
|**Database**          |PostSQL, Alembic    |
|**Containerization**  |Docker              |
|**Data Validation**   |Pydantic            |
|**Code Quality**      |isort, black, flake8|

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
4. Delete Events
5. Google Account Authentication
6. Error handling
