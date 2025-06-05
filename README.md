# 🔍 LeadScrapeLite — Simple Lead Generation Tool

**LeadScrapeLite** is a lightweight web-based lead generation tool that combines the power of the **Google Custom Search API** and automatic **email scraping** from websites.
With an interactive interface powered by **Streamlit**, users only need to enter a keyword (e.g., *startup AI Indonesia*) — the app will search for relevant websites, extract contact emails from the homepage and contact page, then display the results visually and allow exporting.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/Streamlit-%E2%9C%85-red" />
  <img src="https://img.shields.io/badge/Scraping-BeautifulSoup-yellow" />
  <img src="https://img.shields.io/badge/API-Google%20CSE-blue" />
</p>

---

## 🚀 Key Features

* 🔍 **Google Search Integration** via Custom Search API
* 📬 **Email extraction** from homepage and `/contact` page
* 💾 **Automatic saving** of scraping results to SQLite database
* 🔄 **Interactive progress bar** during the scraping process
* 📋 **Filterable and expandable results table**
* 📊 **Data visualization**: pie charts, histograms, and word clouds
* 📤 **Export to CSV** for CRM or further use

---

## 🧪 Example Output

### 📋 Leads Table

* Shows URL, Title, Description, and Email
* Expandable rows for full details
* Button to open the site directly

### 📈 Visual Analysis

* Pie chart of email distribution by domain
* Histogram of email count per site
* Word cloud from the meta descriptions of search results

---

## 🧑‍💻 Live Demo (Optional)

[![Watch Demo Video](https://img.icons8.com/fluency/344/play-button-circled.png)](https://drive.google.com/file/d/1Ut5J01QZF8YotMQtCs7gJ6EOjdFfDl7F/view?usp=sharing)

---

## ⚙️ Tech Stack

| Category      | Technology / Library     |
| ------------- | ------------------------ |
| Web UI        | Streamlit                |
| Web Scraping  | BeautifulSoup, Requests  |
| Search API    | Google Custom Search API |
| Visualization | Matplotlib, WordCloud    |
| Data Handling | Pandas, SQLAlchemy       |
| Database      | SQLite (`leads.db`)      |

---

## 🔧 Installation Steps

### 1. Clone this repository

```bash
git clone https://github.com/your-username/LeadScrapeLite.git
cd LeadScrapeLite
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Google API credentials

Create a `.env` file or directly modify `app.py`:

```python
api_key = "YOUR_API_KEY"
search_engine_id = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
```

🔑 **How to get them:**

* Go to [Google Cloud Console](https://console.cloud.google.com/)
* Create a new project and enable **Custom Search API**
* Set up a custom search engine at [Google Programmable Search Engine](https://programmablesearchengine.google.com/)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open it in your browser: [http://localhost:8501](http://localhost:8501)

---

## 🗂 Project Structure

```
LeadScrapeLite/
├── app.py               # Main Streamlit app
├── leads.db             # SQLite database (auto-created)
├── requirements.txt     # List of Python dependencies
├── README.md            # Project documentation
```

---

## 📦 Key Dependencies

* **[Streamlit](https://streamlit.io/)** — Python-based UI framework
* **[Requests](https://docs.python-requests.org/)** — HTTP client for accessing the web
* **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** — HTML parser for scraping
* **[Pandas](https://pandas.pydata.org/)** — Data analysis and manipulation
* **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM for database operations
* **[WordCloud](https://amueller.github.io/word_cloud/)** — Word cloud text visualization
* **[Matplotlib](https://matplotlib.org/)** — Charts and visualizations

---

## ⚠️ Current Limitations

* ❗ Only works on static HTML pages (not compatible with JavaScript-rendered sites)
* ❗ Google API usage is limited by the **free-tier quota**
* ❗ No email validation yet (e.g., fake, disposable, or spam emails)

---

## 🌱 Future Improvements

* 🧠 Integrate AI models (LLM / NER) to prioritize important emails (e.g., HR, CEO)
* 📊 Domain quality scoring (e.g., domain authority)
* 📁 Export in standard CRM formats (with tags/categories)
* ☁️ Host the app on public platforms like Streamlit Cloud or Hugging Face Spaces
* 🔐 Add rate limiter and retry mechanism for stable scraping

---

## 🙋 About the Developer

**David Mario Yohanes Samosir**
💼 IT & Digital Services Enthusiast | Python Developer

* 🌐 [LinkedIn](https://www.linkedin.com/in/david-mario-yohanes-samosir/)
* 📧 [davidmario484@gmail.com](mailto:davidmario484@gmail.com)

---

> If you like this project, please give it a ⭐ on GitHub and share it with fellow lead gen or digital marketing practitioners!

---
