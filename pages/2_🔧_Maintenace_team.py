import streamlit as st
from model import MaintenanceRequest

st.set_page_config(page_title="Maintenance Team", page_icon="🔧")

if "maintenance_requests" not in st.session_state:
    st.session_state.maintenance_requests = {}

st.markdown("# 🔧 Maintenance Requests")

if not st.session_state.maintenance_requests:
    st.warning("No request has been sent yet.")

for student_name, request in st.session_state.maintenance_requests.items():
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
        scheduled_time = st.time_input(f"Choose scheduled time for {student_name}")
        if st.button(f"Update {student_name}"):
            request.update_status(new_status, scheduled_time)
            st.success(f"Status for {student_name} updated!")
    elif st.button(f"Mark {student_name}'s request as {new_status}"):
        request.update_status(new_status)
        st.success(f"Status for {student_name} updated!")
