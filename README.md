# AVEN — School Journey Visibility Platform

**AVEN** is a school journey visibility and monitoring platform designed to help parents and caregivers stay informed about children's journeys to and from school. It combines family management, journey tracking, route monitoring, safety alerts, and communication into one connected system.

The platform provides a backend for managing parent-child relationships, tracking devices, journey information, and notifications, with a focus on security, reliability, and children's privacy.

## 1. Overview

AVEN aims to improve the visibility of children's school journeys by connecting tracking devices, backend monitoring services, administrators, and parents or caregivers.

The platform supports a structured approach to family registration, journey management, route monitoring, and communication. Parents can receive relevant journey updates through supported messaging channels, while administrators manage family records and system operations.

## 2. Core Features

### Family and Child Management
- Register a parent and child together through a single administrative workflow.
- Associate each child with up to two authorized parents or caregivers.
- Maintain parent-child relationships and family records.
- Manage contact information, verification status, and notification preferences.
- Support secure administration of family records.

### Child Journey Tracking
- Receive GPS coordinates and telemetry from tracking devices.
- Record journey start times, progress, and completion.
- Associate tracking devices with registered children.
- Maintain journey history and relevant events.
- Support expected routes, destinations, and journey time windows.

### Route Monitoring and Safety Alerts
- Monitor journeys against configured routes and time windows.
- Detect deviations from expected journey patterns.
- Identify configured safety-related conditions.
- Generate timely alerts based on deterministic monitoring rules.
- Maintain event records for review and investigation.

### Parent Communication and Notifications
- Deliver journey updates through WhatsApp.
- Support SMS notifications for eligible phone numbers and devices.
- Share map links that allow authorized caregivers to view relevant journey information.
- Send important alerts through supported communication channels.
- Track notification delivery status and handle failed deliveries.
- Apply controlled fallback between communication channels while preventing duplicate alerts.

### Administrator Management
- Provide secure administrator authentication using JWT Bearer tokens.
- Protect administrative endpoints through authentication and authorization.
- Manage parent, child, device, and journey records.
- Support operational visibility into journey events and notification delivery.

### Security and Privacy
- Hash passwords securely.
- Store secrets and database credentials outside source code.
- Restrict access to sensitive family and location data.
- Verify contact details and respect notification consent.
- Use secure, time-limited location-sharing links.
- Apply appropriate access controls, data validation, and error handling.
- Design safety-critical alerts around deterministic rules rather than relying on AI alone.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| SQLAlchemy | Database ORM and persistence |
| PostgreSQL | Relational database |
| Neon | Hosted PostgreSQL database |
| Pydantic | Request validation and response schemas |
| PyJWT | JWT access-token handling |
| pwdlib with Argon2 | Password hashing and verification |
| Uvicorn | ASGI application server |
| Git and GitHub | Version control and source hosting |

## 4. System Architecture

AVEN follows a layered backend architecture that separates HTTP handling, business logic, database operations, and data validation.

- **Routers:** Define API endpoints, process requests, and return HTTP responses.
- **Services:** Implement business rules and coordinate workflows.
- **Repositories:** Encapsulate database queries and persistence operations.
- **Models:** Represent database entities and relationships.
- **Schemas:** Validate incoming requests and define response structures.
- **Core:** Contains application configuration and security dependencies.

This structure helps keep the backend modular, testable, maintainable, and easier to extend.

## 5. Project Structure

```text
Aven_project/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   └── services/
├── database.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

The application separates data models, database access, HTTP endpoints, validation schemas, and business services into dedicated modules.

## 6. Getting Started

### Prerequisites

- Python 3.12 or a compatible version.
- `uv` for Python environment and package management.
- A PostgreSQL database, such as a Neon development database.
- Git.

### Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Aven_project
```

Replace the placeholder with the URL of the AVEN repository.

### Create a Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Configure Environment Variables

Create a local `.env` file in the project root and configure the variables expected by `app/core/config.py`:

```dotenv
database_url=YOUR_DATABASE_URL
admin_username=YOUR_ADMIN_USERNAME
admin_password_hash=YOUR_PASSWORD_HASH
jwt_secret_key=YOUR_RANDOM_SECRET_KEY
```

These values are placeholders. Configure a valid database connection, generate a secure JWT signing key, and create a password hash using the application's password-hashing implementation.

**Never commit real credentials, passwords, signing keys, or the `.env` file to version control.**

### Run the Development Server

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

- API base URL: `http://127.0.0.1:8000`
- Interactive Swagger documentation: `http://127.0.0.1:8000/docs`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

The application uses SQLAlchemy to create missing tables during startup. Database schema evolution should be managed carefully with migrations as the system grows.

## 7. API Endpoints

The backend provides endpoints for administrator authentication, child listing, and combined family registration.

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/auth/login` | Authenticate the administrator and obtain an access token |
| `GET` | `/children/` | List registered children |
| `POST` | `/admin/registrations/` | Register a parent and child together |

Protected endpoints use Bearer-token authentication through the HTTP header:

```http
Authorization: Bearer <ACCESS_TOKEN>
```

Interactive API documentation is available through FastAPI Swagger UI at `/docs`.

## 8. Security and Privacy

Children's journeys and location records are sensitive. AVEN is designed with security and privacy as core requirements.

Key principles include:

- Secure password hashing and token-based authentication.
- Authentication and authorization for administrative operations.
- Protection of database credentials and signing keys.
- Verification of parent contact details.
- Consent-aware messaging and notification preferences.
- Restricted access to children's location and journey data.
- Secure, time-limited map links.
- Notification delivery tracking and duplicate prevention.
- Deterministic handling of safety-critical monitoring rules.
- Appropriate validation, logging, backups, and operational safeguards.

Before production use, all sensitive endpoints, authentication flows, database operations, and privacy controls must be thoroughly tested and reviewed.

## 9. Development and Maintenance

Development follows a modular approach:

1. Define database entities and relationships.
2. Create Pydantic schemas for request validation and responses.
3. Implement database operations in repositories.
4. Apply business rules in services.
5. Expose functionality through FastAPI routers.
6. Test success cases, validation errors, authorization failures, and database constraints.

This approach supports incremental development while keeping the codebase organized and maintainable.

## 10. Contributing

AVEN is under active development. Contributions should preserve the layered architecture, follow secure coding practices, and protect sensitive information.

Before submitting changes:

- Test affected endpoints.
- Avoid committing secrets or personal data.
- Document new environment variables and dependencies.
- Validate error handling and authorization.
- Add tests for new functionality and business rules.

## 11. License

A project license has not yet been selected. Until a license is added, permission to reuse, modify, or redistribute the project should not be assumed.