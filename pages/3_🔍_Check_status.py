import streamlit as st

st.set_page_config(page_title="Check Status", page_icon="🔍")

if "maintenance_requests" not in st.session_state:
    st.session_state.maintenance_requests = {}

st.markdown("# 🔍 Check Maintenance Request Status")

search_name = st.text_input("Enter your name to check request status")

if st.button("Check Status"):
    if search_name in st.session_state.maintenance_requests:
        request = st.session_state.maintenance_requests[search_name]
        st.write("Room Number:", request.room_number)
        st.write("Issue:", request.issue_type)
        st.write("Details:", request.details)
        st.write("Status:", request.get_status())
    else:
        st.error("No request found for this name.")
