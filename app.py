import streamlit as st
from planner import load_vendors, recommend_vendors, suggest_timeline

st.set_page_config(page_title="EventGenius-AI", page_icon="🎉")

st.title("🎉 EventGenius-AI: Your Smart Event Planner")

with st.sidebar:
    st.header("🛠️ Customize Event")
    event_type = st.selectbox("Event Type", ["Wedding", "Birthday", "Corporate"])
    city = st.selectbox("Event City", ["Chennai", "Bangalore", "Delhi", "Mumbai"])
    budget = st.slider("Budget (INR)", 10000, 200000, 50000, step=5000)
    vibe = st.selectbox("Preferred Vibe", ["Luxury", "Minimal", "Cultural", "Modern"])

vendors = load_vendors()
results = recommend_vendors(vendors, event_type, budget, city, vibe)

st.subheader("✨ Recommended Vendors")
st.dataframe(results[['name', 'type', 'cost', 'rating', 'vibe', 'score']].head(5))

st.subheader("🗓️ Suggested Planning Timeline")
timeline = suggest_timeline(event_type)
for item in timeline:
    st.markdown(f"✅ **{item}**")

st.success("You're all set to party! 🥳 Powered by EventGenius-AI.")
