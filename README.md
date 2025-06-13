# Event_Planning_APP

A FastAPI backend for managing users, events, speakers, and registrations.

## Features
- User creation, registration and management (activate/deactivate)
- Event creation, updates, deletion and status toggling
- Event registration for users
- Mark user attendance
- View all registerations or by specific user
  
## Quick Start
### Prerequisites
- python 3.12
- Git
  
### Installation

1. Clone the repo:
   
   ```bash
   git clone https://github.com/leeyah-anas/Event_Planning_APP.git
   cd Event_planning_app_2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the server:
   ```bash
   uvicorn main:app --reload
  
   ```
4. Access interactive API docs at:
   ```bash
   http://localhost:8000/docs
   ```

---

## API Endpoints

| Endpoint                             | Method | Description                                   |
| ------------------------------------ | ------ | --------------------------------------------- |
| `/users/`                            | POST   | Register a new user                           |
| `/users/{user_id}`                   | GET    | Get user details by ID                        |
| `/users/{user_id}/deactivate`        | PATCH  | Deactivate a user                             |
| `/events/`                           | POST   | Create a new event                            |
| `/events/{event_id}`                 | PATCH  | Update event details                          |
| `/events/{event_id}/close`           | PATCH  | Close an event for new registrations          |
| `/speakers/`                         | GET    | List all speakers                             |
| `/speakers{speaker_id}/`             | GET    | Get speaker details by ID
| `/registrations/`                   | POST   | Register a user for an event                  |
| `/registrations/`                   | GET    | View all registrations                        |
| `/registrations/user/{user_id}`     | GET    | View registrations for a specific user        |
| `/registrations/{reg_id}/attend`    | PATCH  | Mark a registration as attended               |
  
