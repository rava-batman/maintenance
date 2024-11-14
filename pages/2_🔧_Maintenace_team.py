import streamlit as st
from model import maintenance_requests

st.set_page_config(page_title="Maintenance Team", page_icon="🔧")

st.markdown("# 🔧 Maintenance Requests")

if not maintenance_requests.items():
    st.warning("No request has been sent yet")

for student_name, request in maintenance_requests.items():
    st.subheader(f"Request from {request.student_name}")
    st.write("Room Number:", request.room_number)
    st.write("Issue:", request.issue_type)
    st.write("Details:", request.details)
    st.write("Status:", request.get_status())

    new_status = st.selectbox(
        f"Update status for {request.student_name}",
        ["Pending", "Scheduled", "Done"]
    )

    if new_status == "Scheduled":
        scheduled_time = st.time_input("Choose scheduled time")
        if st.button(f"Update {student_name}"):
            request.update_status(new_status, scheduled_time)
            st.success("Status updated!")
    elif st.button(f"Mark {student_name}'s request as {new_status}"):
        request.update_status(new_status)
        st.success("Status updated!")
