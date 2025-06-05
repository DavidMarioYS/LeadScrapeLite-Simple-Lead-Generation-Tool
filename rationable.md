

# 🛠 Project Rationale: LeadScrapeLite – Lightweight, Transparent Email Scraper for Lead Generation

## 👋 What Is This Project?

**LeadScrapeLite** is a fast, transparent, and beginner-friendly lead generation tool designed to help users find real business emails related to any niche.

In short, it:

* Uses the **Google Custom Search API** to get high-relevance websites.
* Scrapes **emails directly from those websites** using simple regex.
* Saves results into a **local database** and allows **CSV export**.
* Shows useful **visual breakdowns** (charts, domain stats, and word clouds).
* Runs fully locally using **Streamlit**, no need for server deployment.

🎯 Built in under **5 hours** for the *"Game Rules: Build a Better Lead Gen Tool"* challenge, the goal was to deliver something **lightweight, clean, and transparent** for users who just want **real, usable leads** — fast.

---

## 🧠 Why These Features?

These features were chosen to solve **real pain points** in most lead scraping tools: lack of control, limited feedback, and black-box behavior.

### 🔎 Google Custom Search API

Instead of scraping the entire web, this API returns **targeted websites** based on the user’s query (e.g., "digital agencies in Bali"), improving both **relevance and speed**.

* ✅ Focused results = better leads, fewer irrelevant pages.

### 📧 Email Scraping with Regex

Emails are extracted from the page source using a basic regular expression. It prioritizes content-rich pages (homepages, contact pages, etc.).

* ✅ No guessing. You get the actual email, from the actual URL.

### 🗂 SQLite Database (Bonus Feature)

Unlike some tools that only show temporary results or force you to export immediately, LeadScrapeLite **stores all emails and URLs locally** in a tiny database:

* Avoids duplicates across runs.
* Makes the data **persistently accessible**.
* Easier for users who want to re-query, explore, or extend the data later.

### 📊 Visual Analytics

Users don’t just get raw data — they also get insights:

* Pie charts for email domain breakdown (e.g., `gmail.com`, `company.com`)
* Bar charts for email count per site
* Word clouds for frequently used terms on the websites

> 📈 These help users **understand patterns**, not just collect contacts.

### 📤 CSV Download + Database Backup

While tools like SaasQuatchLeads also offer CSV exports, LeadScrapeLite goes further:

* Users can **download both the CSV and the full SQLite database**.
* This supports more advanced workflows like importing into analytics tools or CRM integrations.

---

## 🆚 Compared to SaasQuatchLeads

| Feature                  | SaasQuatchLeads          | **LeadScrapeLite**                    |
| ------------------------ | ------------------------ | ------------------------------------- |
| **Transparency**         | Unclear data source      | Shows exact URL + email scraped       |
| **Visual Feedback**      | None                     | Charts, domain stats, word cloud      |
| **Search Input Control** | Limited                  | Full custom search keyword input      |
| **Output Format**        | CSV download only        | CSV + full local database download    |
| **Setup & Access**       | Fully hosted (black-box) | Local app, easy to run, fully visible |

While both tools allow CSV downloads, **LeadScrapeLite offers a database-level export** for users who want deeper access or control over their collected data — no need to reverse-engineer the front-end.

---

## ⚙️ How It Works – Technical Overview

### Tools & Libraries

| Component        | Library/Tool                         |
| ---------------- | ------------------------------------ |
| UI Framework     | `streamlit`                          |
| HTTP & Parsing   | `requests`, `BeautifulSoup`, `re`    |
| Data Management  | `sqlite3`, `pandas`                  |
| Charts & Visuals | `matplotlib`, `seaborn`, `wordcloud` |
| Search Engine    | Google Programmable Search API       |

### Step-by-Step Flow

1. User enters a search keyword (e.g., `"event agencies Jakarta"`).
2. Tool sends a request to **Google Custom Search API**.
3. Gets a list of up to 20 website URLs based on the query.
4. Each URL is fetched using `requests`, then parsed using `BeautifulSoup`.
5. Emails are found via regex and saved into a **SQLite** database.
6. User sees the data in:

   * Table form
   * Charts (e.g., email domain stats)
   * Word clouds
7. On the sidebar, users can:

   * Refresh results
   * Export results to CSV or SQLite
   * Run a new search

---

## ⏱ Time Management Summary

| Task                            | Time Spent      |
| ------------------------------- | --------------- |
| Google API + Search Logic       | 1.5 hours       |
| Email Scraping + Regex          | 1 hour          |
| SQLite Database Integration     | 30 minutes      |
| Streamlit UI                    | 45 minutes      |
| Visualizations + Download Tools | 45 minutes      |
| Testing + Cleanup               | 30 minutes      |
| **Total**                       | **\~4.5–5 hrs** |

Everything was built **iteratively** with usability, performance, and extensibility in mind.

---

## 💡 Design Philosophy

LeadScrapeLite is built with the following goals:

* ⚡ **Speed**: Run a full query + scrape + export in under 30 seconds.
* 🧩 **Simplicity**: No bloated UIs or extra features — just useful ones.
* 🔍 **Transparency**: Users always know *where* the emails came from.
* 📦 **Portability**: Run locally, deploy online, or modify the codebase as needed.
* 🧠 **Extensibility**: Easy to expand — e.g., scrape phone numbers, LinkedIn profiles, or score leads.

---

## 🎯 Evaluation Criteria & How LeadScrapeLite Excels

### 1. Business Use Case Understanding (10 points)

* Demonstrates **strong alignment with sales outreach needs** by focusing on collecting **high-impact, real business leads**.
* Prioritizes **relevant websites** via Google Custom Search API, minimizing irrelevant data.
* Integrates with existing workflows by supporting **CSV export and database backup**.
* Creative use of data visualization offers actionable insights, going beyond mere scraping.

### 2. UX/UI (10 points)

* Clean, intuitive interface via Streamlit with **guided user flow**.
* Seamless navigation from input to output without unnecessary complexity.
* Clear data presentation with paginated tables and interactive charts.
* Minimal learning curve suited for non-technical marketers and freelancers.

### 3. Technicality (10 points)

* Robust use of APIs and scraping libraries to deliver **accurate, relevant data**.
* Handles real-world issues like duplicate data, variable HTML structures, and scalability.
* Local SQLite DB ensures persistent, manageable data storage.
* Flexibility to adapt or extend scraping logic to future data sources or formats.

### 4. Design (5 points)

* Professional, minimalist visual design emphasizing readability and usability.
* Thoughtful use of color, typography, and layout to support user tasks.
* Charts and word clouds improve data comprehension and engagement.
* Aligns with modern software aesthetic standards, balancing form and function.

---

## ✅ Final Thoughts

**LeadScrapeLite** is a powerful, lightweight tool designed to deliver **real, actionable leads** fast, transparently, and without hassle.

It’s ideal for:

* Freelancers and consultants searching for prospects
* Startup founders validating markets
* Marketing teams building targeted outreach campaigns
* Researchers studying web presence or digital marketing trends

> It addresses a real-world problem with **clarity, control, and speed** — no signup, no hidden fees, just data you can trust and use.

---