# My Water Tracker (Streamlit)

Track daily water intake with a progress ring, drink types, a log, 7-day insights,
a custom goal in litres, and on-screen reminders.

## Files
- `app.py` - Streamlit app (embeds the tracker page)
- `index.html` - the tracker itself
- `requirements.txt` - dependencies
- `.streamlit/config.toml` - dark teal theme

## Run locally
    pip install -r requirements.txt
    streamlit run app.py

## Publish on Streamlit Community Cloud
1. Create a GitHub repository and upload these files (keep `app.py` in the repo root).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "Create app", choose your repository and branch, and set the main file to `app.py`.
4. Click "Deploy". You get a public link.

## Notes
- Progress is stored in each visitor's browser (localStorage), per device.
- Reminders work only while the page is open.
