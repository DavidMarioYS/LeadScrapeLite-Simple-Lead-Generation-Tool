import streamlit as st
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
import re
from sqlalchemy import create_engine
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# =======================
# 🔍 GOOGLE SEARCH (API)
# =======================
def search_google_api(query, num_results=10):
    api_key = "AIzaSyBUR4Angg-c54uYWxx94wtLi2R8NILFHg4"
    search_engine_id = "e08a90b656cbb42c9"
    results = []

    try:
        for start in range(1, num_results + 1, 10):  # pagination
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": api_key,
                "cx": search_engine_id,
                "q": query,
                "start": start,
            }
            response = requests.get(url, params=params)
            data = response.json()

            if "error" in data:
                error_message = data["error"].get("message", "")
                if "quota" in error_message.lower():
                    st.error("🚫 Google API quota exceeded. Please try again later or use a different API key.")
                    break
                else:
                    st.error(f"Google API Error: {error_message}")
                    break

            items = data.get("items", [])
            for item in items:
                link = item.get("link")
                if link:
                    results.append(link)

            if len(results) >= num_results:
                break
    except Exception as e:
        st.error(f"Failed to fetch Google API results: {e}")

    return results[:num_results]


# =======================
# 📧 EMAIL EXTRACTOR
# =======================
def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return list(set(re.findall(email_pattern, text)))


# =======================
# 🌐 WEBSITE SCRAPER
# =======================
def scrape_site_info(url):
    results = {
        "url": url,
        "title": "",
        "description": "",
        "emails": []
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        pages_to_check = [url, url.rstrip("/") + "/contact"]
        all_emails = []

        for page in pages_to_check:
            response = requests.get(page, headers=headers, timeout=5)

            if response.status_code != 200:
                st.text(f"Halaman {page} gagal diakses, status code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            if not results["title"]:
                results["title"] = soup.title.string.strip() if soup.title else ""

            if not results["description"]:
                meta = soup.find("meta", attrs={"name": "description"})
                results["description"] = meta["content"].strip() if meta and "content" in meta.attrs else ""

            emails_found = extract_emails(response.text)
            if emails_found:
                st.text(f"Found emails on {page}: {emails_found}")

            all_emails.extend(emails_found)

        results["emails"] = list(set(all_emails))
    except Exception as e:
        st.text(f"Gagal mengakses {url}: {e}")

    return results


# =======================
# 🚀 STREAMLIT UI & Custom CSS
# =======================

# Set Streamlit page configuration
st.set_page_config(page_title="LeadScrapeLite", page_icon="🔍", layout="wide")

# Inject custom CSS styles
st.markdown("""
    <style>
        body {
            background: 
            linear-gradient(135deg, 
                rgba(67, 206, 162, 0.4) 0%,    
                rgba(253, 216, 25, 0.3) 50%,   
                rgba(243, 144, 79, 0.4) 75%,   
                rgba(255, 255, 255, 1) 100%    
            );
            background-blend-mode: lighten;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow-x: hidden;
        }
        .stApp {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: transparent;
            padding: 1rem 2rem;
        }
        .title {
            font-size: 3em;
            color: #2b6777;
            font-weight: bold;
            margin-bottom: 0;
        }
        .stButton>button, .stDownloadButton>button {
            background-color: #2b6777;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            border: none;
            box-shadow: 0 4px 8px rgba(43, 103, 119, 0.4);
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #256363;
            color: #e0e0e0;
            box-shadow: 0 6px 12px rgba(37, 99, 99, 0.6);
        }
        .metric-label {
            font-weight: bold;
            color: #114b5f;
        }
        .expander .stExpanderHeader {
            font-weight: 600;
            color: #2b6777;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            border-radius: 6px;
            padding: 0.3rem 0.5rem;
            margin-bottom: 0.3rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-container">
    <img src="https://cdn.pixabay.com/photo/2016/11/29/09/32/robot-1867230_960_720.png" width="50" alt="Logo" />
    <div class="title">LeadScrapeLite</div>
</div>
""", unsafe_allow_html=True)

st.markdown("A Simple Lead Generation Tool to find websites and extract contact emails using Google API.")

tab_input, tab_output = st.tabs(["🔍 Input", "📊 Results"])

# Database engine
engine = create_engine("sqlite:///leads.db")

with tab_input:
    query = st.text_input("🎯 Keyword (e.g., startup AI Indonesia):")
    num_sites = st.slider("🔢 Number of websites to scrape:", 5, 20, 10)
    start_scrape = st.button("🚀 Start Scraping")

    if start_scrape:
        if not query:
            st.warning("Please enter a keyword first.")
        else:
            with st.spinner("Searching and scraping data... please wait a moment."):
                urls = search_google_api(query, num_sites)

                data = []
                progress_bar = st.progress(0)
                for idx, url in enumerate(urls):
                    st.text(f"🔄 {idx+1}/{len(urls)}: Scraping {url}")
                    info = scrape_site_info(url)
                    if info["emails"]:
                        data.append(info)
                    progress_bar.progress((idx + 1) / len(urls))
                    time.sleep(1)

            if data:
                df = pd.DataFrame(data)
                df['emails'] = df['emails'].apply(lambda x: ", ".join(x))

                # Save dataframe to session state for later use
                st.session_state['leads_df'] = df

                # Save to SQLite database, but don't trigger download automatically
                try:
                    df.to_sql("leads", engine, if_exists="append", index=False)
                    st.success("✅ Data successfully saved to SQLite database (leads.db)")
                except Exception as e:
                    st.error(f"Failed to save to SQLite database: {e}")
            else:
                st.warning("No emails found from the search results.")

with tab_output:
    if 'leads_df' in st.session_state and not st.session_state['leads_df'].empty:
        df = st.session_state['leads_df']

        search_filter = st.text_input("🔎 Filter results (title, URL, email):", key="filter_input")
        if search_filter:
            mask = df.apply(lambda row: row.astype(str).str.contains(search_filter, case=False).any(), axis=1)
            filtered_df = df[mask]
        else:
            filtered_df = df

        st.metric("🌐 Total Websites Found", len(filtered_df))
        unique_emails = set(", ".join(filtered_df['emails']).split(", "))
        st.metric("📧 Total Unique Emails", len(unique_emails))

        for idx, row in filtered_df.iterrows():
            icon = "📍" if row['emails'] else "🔒"
            with st.expander(f"{icon} {row['title'] if row['title'] else row['url']}"):
                st.write(f"**URL:** [{row['url']}]({row['url']})")
                st.write(f"**Description:** {row['description'] if row['description'] else '-'}")
                st.write(f"**Emails:** {row['emails']}")
                if st.button(f"🌐 Open Website {idx}", key=f"open_{idx}"):
                    st.write(f"[Click here to open {row['url']}]({row['url']})")

        # Download buttons
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="⬇️ Download Filtered CSV",
            data=csv,
            file_name="leads_filtered.csv",
            mime="text/csv"
        )

        # Download SQLite database file
        if os.path.exists("leads.db"):
            with open("leads.db", "rb") as f:
                db_data = f.read()
            st.download_button(
                label="⬇️ Download SQLite Database (leads.db)",
                data=db_data,
                file_name="leads.db",
                mime="application/x-sqlite3"
            )
        else:
            st.warning("SQLite database file (leads.db) not found.")

        st.subheader("📈 Visual Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📊 Distribution of Email Counts per Website")
            df['email_count'] = df['emails'].apply(lambda x: len(x.split(", ")) if x else 0)
            bins = [0, 1, 2, 4, float('inf')]
            labels = ['0 Emails', '1 Email', '2-3 Emails', '>3 Emails']
            df['email_bin'] = pd.cut(df['email_count'], bins=bins, labels=labels, right=False)
            pie_data = df['email_bin'].value_counts().reindex(labels).fillna(0)

            fig1, ax1 = plt.subplots()
            ax1.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140,
                    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
            ax1.axis('equal')
            st.pyplot(fig1)

        with col2:
            st.markdown("#### ☁️ Word Cloud of Email Domains")
            all_emails = ", ".join(df['emails'])
            domains = [email.split("@")[-1].lower() for email in all_emails.split(", ") if "@" in email]
            domain_text = " ".join(domains)

            if domain_text.strip():
                wordcloud = WordCloud(width=600, height=400, background_color="white").generate(domain_text)
                fig2, ax2 = plt.subplots()
                ax2.imshow(wordcloud, interpolation='bilinear')
                ax2.axis('off')
                st.pyplot(fig2)
            else:
                st.write("No emails found to generate word cloud.")

    else:
        st.info("No scraped data available. Please start scraping from the 'Input' tab.")