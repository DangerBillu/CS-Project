Event Management System
This is a web-based Event Management System designed as a 12th-grade Computer Science investigatory project. The system allows users to:

Create Events
Register for Events
View Upcoming Events (with the ability to view participants)
Manage Participants (edit or delete their details for each event)
🛠️ Features
Event Creation: Easily create new events.
Event Registration: Register for events with participant details.
Upcoming Events Section: Displays all events on the home page with links to view participants.
Event Pages: Each event has its own page for managing participant details.
📋 Technologies Used
Frontend
HTML: For structuring the user interface.
Tailwind CSS: For styling the application.
Backend
Python: Backend programming language.
Flask: Micro-framework for handling routes and server-side functionality.
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/event-management-system.git
cd event-management-system
2. Install Required Dependencies
Before proceeding, ensure you have Python and pip installed.

Install the required Python libraries:

bash
Copy code
pip install flask
3. Setting Up Tailwind CSS
Tailwind CSS is used to style the application. Follow these steps to set it up:

Install Node.js and npm (if not already installed):
Download from Node.js Official Site.

Install Tailwind CSS:
Inside your project directory, run:

bash
Copy code
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
Configure Tailwind:
Open the tailwind.config.js file and update it as needed:

javascript
Copy code
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {},
  },
  plugins: [],
}
Include Tailwind in Your CSS:
Create a CSS file (e.g., styles.css) in your project and add:

css
Copy code
@tailwind base;
@tailwind components;
@tailwind utilities;
Build Tailwind CSS:
Run this command to generate the final CSS file:

bash
Copy code
npx tailwindcss -i ./styles.css -o ./static/css/styles.css --watch
Include CSS in HTML:
Add this line in your <head> section of HTML:

html
Copy code
<link rel="stylesheet" href="/static/css/styles.css">
4. Run the Flask Application
Start the server by running the following command:

bash
Copy code
python app.py
Navigate to http://127.0.0.1:5000/ in your web browser to access the application.

🌟 Folder Structure
csharp
Copy code
event-management-system/
├── static/
│   └── css/
│       └── styles.css       # Tailwind-generated CSS
├── templates/
│   ├── base.html            # Base template for consistent layout
│   ├── index.html           # Home page with upcoming events
│   ├── event.html           # Individual event page
│   └── register.html        # Registration form
├── app.py                   # Flask application
├── requirements.txt         # Dependencies
├── tailwind.config.js       # Tailwind configuration
└── README.md                # Documentation
🤝 Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
