# CPS Study Guide

A web-based study guide designed to help students review **CPS 213 computer systems and digital logic topics** through clear explanations, key points, worked examples, and visual learning materials.

This project is being developed as a learning project alongside my Computer Science studies at Toronto Metropolitan University.

## Features

* **40 study topics** covering CPS 213 concepts.
* **Topic explanations** to make difficult concepts easier to understand.
* **Key points** highlighting important information.
* **Worked examples** to support step-by-step learning.
* **Visual explanations** to make concepts easier to follow.
* **Study tips** for reviewing each topic.
* **Additional learning resources** for further study.
* **Interactive homepage** for browsing and selecting topics.

## Built With

* **Python** — application logic and topic handling.
* **FastAPI** — backend and API endpoints.
* **HTML** — webpage structure.
* **CSS** — styling and layout.
* **JavaScript** — interactive topic selection.
* **JSON** — storing study topics and their content.
* **Jinja2** — rendering dynamic HTML pages.

## Project Structure

```text
CPS Project/
├── main.py
├── cps_code.py
├── cps213_study_guide.json
├── requirements.txt
├── test_project.py
├── templates/
│   ├── index.html
│   └── topic.html
├── static/
│   ├── style.css
│   ├── script.js
│   └── visuals/
├── .gitignore
└── README.md
```

*The structure above is illustrative. Your actual folders and filenames may differ slightly.*

## Getting Started

### Prerequisites

* Python 3
* pip
* Git (optional, for version control)

### 1. Clone the Repository

```bash
git clone https://github.com/aliakbarbhojani/tmu-cps-project
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's URL.

Navigate into the project folder:

```bash
cd "CPS Project"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows — Command Prompt:**

```bash
venv\Scripts\activate
```

**Windows — PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

Open the following address in your browser:

http://127.0.0.1:8000

The application should now be running locally.

## API Endpoints

| Endpoint                 | Description                                |
| ------------------------ | ------------------------------------------ |
| `/`                      | Displays the homepage.                     |
| `/api/topics`            | Returns the list of study topics as JSON.  |
| `/api/topics/{topic_id}` | Returns an individual topic as JSON.       |
| `/topic/{topic_id}`      | Displays the webpage for a selected topic. |

## Learning Objectives

Through this project, I aim to strengthen my understanding of:

* Python programming and object-oriented programming.
* Building web applications with FastAPI.
* Connecting frontend pages to backend functionality.
* Working with JSON data.
* Using HTML, CSS, and JavaScript to create interactive websites.
* Organizing and testing a software project.
* Using Git and GitHub for version control.

## Future Improvements

Potential improvements as development continues:

* Improve the website's user interface and accessibility.
* Add more interactive visual explanations.
* Improve the organization and presentation of study material.
* Add further study and revision features.

## Disclaimer

This is an educational project created to support personal learning and revision. The material should be checked against official course notes and instructor-provided resources.

## Author

**Aliakbar Bhojani**

* GitHub: [Aliakbar Bhojani](https://github.com/aliakbarbhojani)
* LinkedIn: [Aliakbar Bhojani](https://www.linkedin.com/in/aliakbar-bhojani/)
