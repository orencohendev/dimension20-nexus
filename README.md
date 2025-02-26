# Dimension 20 Nexus

Dimension 20 Nexus is an open-source resource that aggregates data about Dimension 20 campaigns, episodes, reviews, and more. Built with FastAPI for the backend and a modern React front-end, it provides developers and creators with a clean, structured API to integrate Dimension 20 data into their own applications—without the hassle of scraping the web.

## Features

- **Comprehensive API**  
  Built with FastAPI, offering endpoints such as:
  - `GET /api/campaigns` — List all campaigns.
  - `GET /api/campaigns/{id}` — Detailed info for a specific campaign (with reviews).
  - `GET /api/campaigns/{id}/episodes` — Episodes for a given campaign.
  
  API docs are available at `/api/docs` (Swagger UI) and the OpenAPI spec at `/api/openapi.json`.

- **Modern, Engaging Front-End**  
  A responsive React app built with Material‑UI (MUI) that lets users:
  - Explore campaigns via dynamic dropdowns.
  - View detailed campaign info (including clickable review links).
  - Select episodes to see full details with a “Watch Episode” link.

- **Seed Script & PostgreSQL**  
  The backend includes a seed script to initialize the database with JSON data and uses PostgreSQL for persistent storage with a simple, scalable schema.

- **Open Source & Community Driven**  
  Contributions are welcome! Future plans include a contribution system with user authentication and moderation, but the current focus is on providing a reliable, curated data resource.

## Getting Started

### Prerequisites

- Python 3.8+ (for the FastAPI backend)
- Node.js (for the React front-end)
- PostgreSQL (or a managed database service on Render)
- Poetry (for dependency management)

### Backend Setup

1. Clone the repository and navigate to the backend folder:  
   `git clone https://github.com/your-username/dimension20-nexus.git`  
   `cd dimension20-nexus/backend`

2. Install dependencies using Poetry:  
   `poetry install`

3. Set up environment variables:  
   Create a `.env` file (or configure your environment) with the required settings, for example:  
   - `DATABASE_URL` (e.g., `postgresql://user:password@localhost:5432/your_db`)  
   - Any other necessary secrets.

4. Seed the database:  
   `poetry run python -m app.scripts.seed`

5. Run the FastAPI app:  
   `poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000`

The API docs will be available at `http://localhost:8000/api/docs`.

### Frontend Setup

1. Navigate to the frontend directory:  
   `cd ../frontend`

2. Install dependencies:  
   `npm install`

3. Run the development server:  
   `npm start`

   The React app will open on `http://localhost:3000`.

4. Build for production:  
   `npm run build`

   Then integrate the build folder with your FastAPI app to serve static files.

### Deployment

- **Render Deployment:**  
  This project is designed to be deployed on Render. The FastAPI backend, PostgreSQL database, and static React front-end can all be managed from Render’s dashboard. Set your environment variables accordingly and update your start commands to include the seed script if needed.

- **Docker Deployment:**  
  Optionally, containerize the app with Docker. Ensure your Dockerfile copies the necessary files (including data and build folders) and sets the correct working directory.

## Contribution Guidelines

We welcome contributions! If you’d like to help:
- Fork the repository and create your feature branch.
- Follow coding standards and write tests where appropriate.
- Open issues to discuss changes or improvements.
- Submit a pull request with clear descriptions of your changes.

For security reasons, note that POST endpoints (for user contributions) are protected. Future enhancements may include a full contribution system with authentication and moderation.

## API Documentation

- Swagger UI: `http://localhost:8000/api/docs`
- OpenAPI JSON: `http://localhost:8000/api/openapi.json`

## Contact

For questions, suggestions, or to report issues, please contact:  
oren@geekpeek.blog
