# Netta's Southern Flava

Welcome to **Netta's Southern Flava**! This full-stack application is designed to simplify and enhance the restaurant experience for both customers and staff. 
<!-- It features a modern, user-friendly interface and a robust backend to handle all restaurant-related operations efficiently. -->

## Features

- **Customer-facing Features**:
  - Browse the menu with categories.
  <!-- - Place orders online. -->
  <!-- - Track order status in real-time. -->
  - View restaurant information (hours, location, contact details).

<!-- - **Admin-facing Features**:
  - Manage menu items (add, edit, delete).
  - Track and update orders.
  - View analytics (e.g., sales, popular items). -->

## Tech Stack

### Frontend
- **Framework**: [React](https://reactjs.org/)
- **Styling**: CSS/SCSS or a component library (e.g., Material-UI, Tailwind CSS)
- **State Management**: Context API/Redux

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL/MySQL/SQLite <!-- Might not need this -->
<!-- - **Authentication**: JWT-based authentication -->
- **API Documentation**: Automatically generated with OpenAPI

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed
- [Python](https://www.python.org/) 3.9+ installed
<!-- - A database setup (e.g., PostgreSQL) -->

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:sariahadams/nettas-southern-flava.git
   cd nettas-southern-flava
   ```

2. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

3. Set up the backend:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Frontend: Add `.env` file in the `frontend` directory.
   - Backend: Add `.env` file in the `backend` directory.

5. Start the application:
   - Frontend:
     ```bash
     npm start
     ```
   - Backend:
     ```bash
     uvicorn main:app --reload
     ```

### Folder Structure

```plaintext
nettas-southern-flava/
├── frontend/        # React frontend application
├── backend/         # FastAPI backend application
├── database/        # Database initialization and migrations
└── README.md        # Project documentation
```

<!-- ## License

This project is licensed under the MIT License. See the LICENSE file for more details. -->

## Contact

For any inquiries, feel free to reach out:
- Sariah Adams
    - **Email**: [sariahcadams4@gmail.com](mailto:sariahcadams4@gmail.com)
    - **GitHub**: [sariahadams](https://github.com/sariahadams)
- Earl Tankard, Jr., Ph.D.
    - **Email**: [earl.tankard.jr@gmail.com](mailto:earl.tankard.jr@gmail.com)
    - **GitHub**: [primetimetank21](https://github.com/primetimetank21)
