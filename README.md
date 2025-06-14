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
| `/users/`                            | POST   | Create a new user                             |
| `/users/`                            | GET    | Get all users                                 |
| `/users/{user_id}`                   | GET    | Get user details by ID                        |
|`/users/{user_id}`                    | GET    | Update User details                           |
| `/users/{user_id}/deactivate`        | PATCH  | Deactivate a user                             |
| `/events/`                           | POST   | Create a new event                            |
| `/events/`                           | GET    | Get all events                                |
| `/events/{event_id`                  | GET    | Get event by ID                               |
| `/events/{event_id}`                 | PATCH  | Update event details                          |
| `/events/{event_id}/close`           | PATCH  | Close an event for new registrations          |
| `/speakers/`                         | GET    | List all speakers                             |
| `/speakers{speaker_id}/`             | GET    | Get speaker details by ID
| `/registrations/`                   | POST   | Register a user for an event                  |
| `/registrations/`                   | GET    | View all registrations                        |
| `/registrations/user/{user_id}`     | GET    | View registrations for a specific user        |
| `/registrations/{reg_id}/attend`    | PATCH  | Mark a registration as attended               |

---
##  **Example Responses**

### Successful User Registration (201)

```json
{
  "full_name": "Adepoju Mary",
  "email": "mary226@eyahoo.com",
  "id": 1,
  "is_active": true
}
```
### Error: Event Closed (400)

```json
{
  "detail": "Event closed"
}
```
### Registration Marked as Attended (200)

```json
{
  "id": 1,
  "user_id": 1,
  "event_id": 2,
  "registration_date": "2025-06-14T16:38:47.941311",
  "attended": true
}
```

---

## **Development Roadmap**

### Core Features

- [ ] User registration and deactivation
- [ ] Event CRUD and open/close registration
- [ ] Speaker assigning
- [ ] User registration and attendance tracking
- [ ] Add speaker assignment to events

### Improvements

- [ ] Enhanced error documentation
- [ ] Add pagination for user/event listings
- [ ] Integrate authentication for admin features

---
## **Team**

|  Name            |       ID                                   |
|------------------|--------------------------------------------|
|  Anataku Aaliyah |       ALT/SOE/024/4624                     |
