# PerturBase
PerturBase is a web-based portal for exploring metadata from Perturb-seq experiments. Built for usability, it enables researchers to browse, filter, and visualize large-scale screening datasets through an interactive interface — no coding required.

## ✨ Features

### 📊 Interactive Dashboard
High-level visualizations summarizing the dataset:
* Cell counts by experiment
* Feature distributions
* Mitochondrial/ribosomal content
* Experiment type breakdown
* ...and more!

### 📁 Experiment Explorer
* Browse all available Perturb-seq experiments.
* Filter by Keyword search, min cell count, treatment, publication, source, type, date range, and more.
* Sortable tables with experiment-level summaries.

### 🧪 Experiment Detail Views

Each experiment includes:
* **Metadata Tab**: Overview of experiment + channel summaries.
* **Visualization Tab**: Metrics, UMAP, top genes, and heatmaps displayed via a carousel with download options.
* **Download Tab**: Download raw .rds files and metadata CSVs.

## 🚀 Usage: 

Check PerturBase [here](https://bioed-new.bu.edu/students_25/Team10/PerturBase/main)

## 🏗️ Architecture

### 🔧 Backend (Flask + MariaDB)
* Framework: Built with Flask using an application factory pattern for modular development and cleaner deployment.
* Routing: RESTful API endpoints structured using Flask Blueprints (e.g., /api/experiments, /api/dashboard).
* Database: Uses MariaDB for relational storage. SQL is used to perform fast queries on experiment metadata and more.
* Deployment: Runs behind an Apache web server, hosted under a specific path (/students_25/Team10/PerturBase/main).
* Static Assets: Serves visualization images and downloadable files via Flask routes for experiment-specific content.

### 🎨 Frontend (React)
* Routing: Built with react-router-dom to enable smooth client-side navigation between pages like Home, Dashboard, Experiments, and Help.
* Component Design: Modular and reusable components structure the UI, including Navbar, Footer, ExperimentList, ImageCarousel, and ExperimentFilter for metadata querying.
* AJAX Requests: Uses Axios to perform asynchronous HTTP requests to the Flask backend, enabling real-time data loading for metadata, filters, and visualizations without full page reloads.
* Visualization: Incorporates Recharts for interactive Dashboard charts (bar, line, pie) and a custom image carousel for displaying experiment visualizations, complete with download functionality.
* Styling: Responsive and modern layout achieved through custom CSS and media queries, ensuring compatibility across different screen sizes.

### 🔁 Data Flow
* On startup, the app loads metadata pre-extracted from .rds files into MariaDB.
* React pages make Axios requests to Flask endpoints to dynamically fetch experiment metadata and visualization assets.
* All filtering, sorting, and pagination logic is handled server-side for efficiency, with client-side rendering of tables and charts.

```

PERTURBASE/
│ 
├── backend/                             # Backend root (Flask app)
│   ├── app.py                           # Entry point for the Flask app (factory function)
│   ├── config.py                        # Configuration handler (loads environment variables)
│   ├── requirements.txt                 # Backend Python dependencies
│   ├── .env                             # Local environment variables (not committed)
│   ├── database/                        # Database logic and schema
│   │   ├── create_database.sh           # Shell script to initialize schema
│   │   ├── db_utils.py                  # Database connection function (MariaDB, plain SQL)
│   │   ├── schema.sql                   # SQL schema (tables: Experiment, ChannelMetaData, etc.)
│   │   ├── countmatrix/                 # Placeholder or logic for raw matrix data
│   │   └── plots/                       # Static plot directory or plot handling logic
│   ├── routes/                          # All Flask API routes (organized as blueprints)
│   │   ├── __init__.py                  # Registers all route blueprints
│   │   ├── experiments.py               # Endpoints for experiments (summary, single, etc.)
│   │   ├── channels.py                  # Endpoints for metadata on channels (e.g., QC metrics)
│   │   ├── raw_counts.py                # Endpoints for low-level counts
│   │   ├── download.py                  # Endpoints for downloading .rds files and CSV exports
│   │   ├── dashboard.py                 # Endpoints for aggregated stats and dashboard visualizations
│   │   └── plots.py                     # Endpoints for plot preview/download
│   ├── scripts/                         # Utility scripts to extract, load, or transform data
│   │   ├── Load_Data_SQLs/              # Folder to hold logically split SQLs
│   │   ├── Meta_to_SQL.py               # Python version of metadata loader
│   │   ├── MetaData_to_SQL.R            # R-based version for metadata loading
│   │   ├── Seurat_to_SQL.py             # Python-based count matrix loader
│   │   ├── Seurat_to_SQL.R              # R-based count matrix loader
│   │   └── mdb_helper_functions.py      # Helper functions to format or clean data
│   └── tests/                           # Unit + integration tests for backend
│       ├── test_db_connection.py        # Test database connectivity
│       └── test_routes.py               # Test API endpoint responses
│ 
├── frontend/                            # React frontend
│   ├── public/                          # Static files + HTML entry point
│   │   ├── index.html                   # Root HTML for React DOM mount
│   │   ├── favicon.ico / logos          # Application favicons
│   │   └── api/                         # Static API references (if used)
│   ├── src/                             # All source code
│   │   ├── components/                  # Reusable UI components
│   │   │   ├── common/                  # Navbar, Footer, layout elements
│   │   │   ├── forms/                   # Form controls (e.g., filters)
│   │   │   ├── visualizations/          # Plot rendering components
│   │   │   └── ExperimentList.js        # Table component for experiment listings
│   │   ├── pages/                       # Page-level views
│   │   │   ├── Home.js                  # Welcome / about page
│   │   │   ├── Dashboard.js             # Summary statistics & visualizations
│   │   │   ├── Experiments.js           # Query and browse experiments
│   │   │   ├── Experiment.js            # Single experiment detail page
│   │   │   └── Help.js                  # Documentation / user guide page
│   │   ├── services/                    # API layer (Axios wrapper)
│   │   │   └── api.js                   # Base Axios instance and helpers
│   │   ├── App.js                       # Core router and layout
│   │   ├── index.js                     # React entry point
│   │   ├── App.css / index.css          # Global and page styles
│   │   ├── reportWebVitals.js           # (Optional) React perf tool
│   │   └── setupTests.js                # Jest test setup (optional)
│   ├── package.json                     # React dependencies and scripts
│   ├── package-lock.json                # Exact versions installed
│   └── README.md                        # Frontend-specific notes
│ 
├── app_mode.sh                          # Simple mode switcher script (development vs production)
├── main.py                              # Unified Flask app launcher with dual-mode support
├── .gitignore                           # Ignored files and folders
└── README.md                            # Project-wide documentation

```


## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/MYousry2002/PerturBase.git
```

### 2. Backend Setup

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
```

### 3. Database Setup

* Ensure your .env file is correctly configured with your MariaDB credentials and the database name (e.g., Team10).
* If starting with a fresh database, use the provided SQL script to create the necessary tables and initialize the schema.

### 4. Frontend Setup

```bash
cd ../frontend
npm install
npm run build
```
The React build will be served via Flask automatically when deployed.


### 5. Launch the App

* For development mode: 
```bash
cd ../backend
./run-app.sh development
cd ..
python main.py
```
Then open your browser to:  
`http://localhost:5000/students_25/Team10/PerturBase/main`

* For production mode:
```bash
cd ../backend
./run-app.sh production
cd ..
```
Then open your browser to (edit URL based on where the app is hosted):
http://bioed-new.bu.edu/students_25/Team10/PerturBase/main


## 📥 Contributions
Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes. Bug reports and feature ideas welcome!

## 📄 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
See the LICENSE file for full details.
