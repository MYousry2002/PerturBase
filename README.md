# PerturBase
PerturBase is a web-based platform for exploring and querying metadata from Perturb-seq experiments. Designed to make functional genomics data more accessible, PerturBase parses .rds files generated in R, extracts rich metadata (e.g., gene perturbations, batch info, QC metrics), and presents it through a powerful API and interactive frontend — all without requiring users to know R or SQL.

The app is built using a full-stack architecture with Flask with Mariadb on the backend and React on the frontend. It empowers both computational and non-programming users to intuitively browse, filter, and visualize large-scale perturbation datasets.

## 🚀 Features
* 📦 Metadata Extraction
  
Automatically parses .rds files and extracts key cell-level metadata including gene perturbations, treatment conditions, QC metrics, and sequencing batch info.

* 🔎 Advanced Metadata Querying
  
Submit custom queries to explore experiment-level and cell-level metadata, such as:

What perturbation types exist in a dataset?
How many cells passed QC per batch?
What is the average mitochondrial content per experiment?

* 📊 Visualizations

View key experiment insights at a glance with: Bar charts (cells per perturbation type), Violin plots (QC metrics across experiments), Heatmaps (metadata completeness), Pie charts (published vs unpublished datasets), and Boxplots (cell count distribution)

* 💾 Downloadable Results
  
Export any metadata query result as a .csv, and download visualization images as .png.

* 🧠 Structured Relational Database
  
Uses MariaDB with SQLAlchemy to organize extracted metadata for fast and reliable querying.

* 🌐 User-Friendly Frontend
  
Built with React and Axios to provide a seamless, interactive user experience with support for navigation, help pages, and loading states.

* ⚙️ Future Extensibility
  
Designed to support more datasets and public deployment via cloud hosting.

## Usage: 

Watch this demo [here](www.google.com)

## Application Structure

```

PERTURBBASE/
├── backend/
│   ├── app.py                      # Main entry point for the Flask application
│   ├── config.py                   # Configuration settings (loads .env variables)
│   ├── requirements.txt            # Python dependencies for the backend
│   ├── .env                        # Environment variables (DB credentials, etc.)
│   ├── database/                   # Database-related code and SQL schema
│   │   ├── __init__.py             # Initializes the database package
│   │   ├── db_utils.py             # Contains the DB connection function (using plain SQL)
│   │   └── schema.sql              # SQL script to create the tables (Experiment, ChannelMetaData, etc.)
│   ├── routes/                     # API endpoints defined as Blueprints
│   │   ├── __init__.py             # Registers all route Blueprints
│   │   ├── experiments.py          # Endpoints for Experiment-related queries
│   │   ├── channels.py             # Endpoints for ChannelMetaData and ChannelCounts queries
│   │   └── raw_counts.py           # Endpoints for RawCounts queries
│   ├── scripts/                    # Data extraction and processing scripts
│   │   ├── load_data.py            # Python script to parse CSV/JSON and load data into MariaDB
│   │   └── rds_to_csv.R            # R script to convert RDS files to CSV/JSON (if needed)
│   └── tests/                      # Unit and integration tests for the backend
│
├── frontend/
│   ├── public/
│   │   └── index.html              # Root HTML file for the React app
│   ├── src/
│   │   ├── assets/                 # Static assets (images and global styles)
│   │   │   ├── images/             # Static images
│   │   │   └── styles/             # Global CSS files
│   │   ├── components/             # Reusable React components
│   │   │   ├── common/             # Common components (e.g., Navbar, Footer)
│   │   │   ├── forms/              # Form components (e.g., MetadataQueryForm)
│   │   │   ├── visualizations/     # Chart components (bar charts, heatmaps, etc.)
│   │   │   └── ExperimentList.js   # Component to display experiments
│   │   ├── pages/                  # Page components corresponding to app routes
│   │   │   ├── Home.js             # Landing page
│   │   │   ├── Dashboard.js        # Metadata summary and visualizations
│   │   │   └── Help.js             # Help/documentation page
│   │   ├── services/               # API service modules
│   │   │   └── api.js              # Axios wrapper for API calls
│   │   ├── App.js                  # Main React app layout with routing
│   │   ├── index.js                # App entry point that renders the App component
│   │   ├── App.css                 # Global or App-specific styles
│   │   ├── reportWebVitals.js      # (Optional) Web performance tracking
│   │   └── setupTests.js           # (Optional) Testing configuration
│   ├── package.json                # React dependencies and scripts
│   └── README.md                   # Frontend documentation
│
├── .gitignore
└── README.md                       # Project-level documentation

```

### Backend
The backend is built with Flask. It is structured to provide API endpoints for user authentication and CRUD operations for lists and tasks. It uses SQL with MariaDB for the database.

### Frontend
The frontend is created using React. It is composed of several components that work together to provide a seamless and dynamic user experience.


## Installation

1. Clone the repository

```bash
git clone https://github.com/MYousry2002/PerturBase.git
```

2. Backend setup

Navigate to the backend directory, install dependencies, and start the server

On Windows:
```bash
cd PerturBase/backend
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

On macOS:
```bash
cd PerturBase/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

3. Database Setup

* Ensure your .env file is correctly configured with your MariaDB credentials and the database name (for example, Team10).
* Use the provided SQL script to create the necessary tables.
* run the following command in terminal:

```bash
cd PerturBase/backend
mariadb -u <username> -p -h bioed-new.bu.edu Team10 < database/schema.sql
```

* you will be prompt to enter your mariadb password


4. Frontend Setup

In a new terminal, navigate to the frontend directory, install dependencies, and start the React application:
```bash
cd frontend
npm install
npm start
```

5. View the application 
Open http://localhost:3000 in your browser.


## Contribution
Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes.

## Licence
