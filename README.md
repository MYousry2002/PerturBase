# PerturBase
PerturBase is a web-based platform for exploring and querying metadata from Perturb-seq experiments. Designed to make functional genomics data more accessible, PerturBase parses .rds files generated in R, extracts rich metadata (e.g., gene perturbations, batch info, QC metrics), and presents it through a powerful API and interactive frontend — all without requiring users to know R or SQL.

The app is built using a full-stack architecture with Flask on the backend and React on the frontend. It empowers both computational and non-programming users to intuitively browse, filter, and visualize large-scale perturbation datasets.

## 🚀 Features
* 📦 Metadata Extraction
  
Automatically parses .rds files and extracts key cell-level metadata including gene perturbations, treatment conditions, QC metrics, and sequencing batch info.

* 🔎 Advanced Metadata Querying
  
Submit custom queries to explore experiment-level and cell-level metadata, such as:

	* What perturbation types exist in a dataset?
	* How many cells passed QC per batch?
	* What is the average mitochondrial content per experiment?

* 📊 Visualizations

View key experiment insights at a glance with:
	* Bar charts (cells per perturbation type)
	* Violin plots (QC metrics across experiments)
	* Heatmaps (metadata completeness)
	* Pie charts (published vs unpublished datasets)
	* Boxplots (cell count distribution)

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

### Backend
The backend is built with Flask. It is structured to provide API endpoints for user authentication and CRUD operations for lists and tasks. It uses MariaDB with SQLAlchemy for the database.

### Frontend
The frontend is created using React. It is composed of several components that work together to provide a seamless and dynamic user experience.

```graphql
PERTURBBASE/
├── backend/
│   ├── app/
│   │   ├── __init__.py                # App factory
│   │   ├── models.py                  # SQLAlchemy DB models
│   │   ├── utils.py                   # Helpers (e.g., RDS parsing, CSV export)
│   │   └── routes/
│   │       ├── experiment_routes.py   # Routes to handle experiment queries
│   │       ├── metadata_routes.py     # Routes to query metadata
│   │       └── download_routes.py     # Routes for CSV/image downloads
│   ├── instance/                      # Local database instance
│   ├── migrations/                    # Flask-Migrate auto-generated DB migrations
│   ├── requirements.txt               # Python dependencies
│   └── app.py                         # Entry point to run the Flask server
│
├── frontend/
│   ├── public/
│   │   └── index.html                 # React root HTML
│   ├── src/
│   │   ├── components/
│   │   │   ├── ExperimentList.js      # Displays list of experiments
│   │   │   ├── MetadataQueryForm.js   # Form to search metadata
│   │   │   └── Visualizations/        # Chart components (bar, heatmap, violin, etc.)
│   │   ├── pages/
│   │   │   ├── Home.js                # Landing page
│   │   │   ├── Dashboard.js           # Metadata summary + visualizations
│   │   │   └── Help.js                # Docs/help for how to use the tool
│   │   ├── services/
│   │   │   └── api.js                 # Axios wrapper for API calls
│   │   ├── App.js                     # Main React app layout
│   │   ├── index.js                   # App entry point
│   │   ├── App.css / index.css        # Styling
│   │   ├── reportWebVitals.js         # (optional) Web performance tracking
│   │   └── setupTests.js              # (Optional) for React testing
│   ├── package.json                   # React dependencies + scripts
│   └── README.md
│
├── .gitignore
└── README.md                         # Project documentation

```

## Installation

1. Clone the repository

```bash
git clone https://github.com/MYousry2002/hierarchical-todo-list-web-app.git
```

2. Navigate to the backend directory, install dependencies, and start the server

On Windows:
```bash
cd backend
python3 -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
python3 app.py
```

On macOS:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

3. In a new terminal, navigate to the frontend directory, install dependencies, and start the React application:
```bash
cd frontend
npm install
npm start
```

4. Open http://localhost:3000 in your browser to view the application.


## Contribution
Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes.

## Licence
