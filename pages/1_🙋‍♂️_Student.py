import streamlit as st
from model import MaintenanceRequest

st.set_page_config(page_title="Student", page_icon="🙋‍♂️")

if "maintenance_requests" not in st.session_state:
    st.session_state.maintenance_requests = {}

st.markdown("# ⚙️ Fill out the form")

student_name = st.text_input("Student name", value="")
room_number = st.number_input("Room number", min_value=0)
issue_type = st.selectbox("Select one of the options", ("Heat/AC", "Bathroom", "Furnitures", "Others"))
details = st.text_area("Give some details")
attachment = st.file_uploader("Additional attachments if needed", type=["jpg", "jpeg", "png"])

if st.button("Submit"):
    if student_name and room_number and issue_type and details:
        request = MaintenanceRequest(student_name, room_number, issue_type, details, attachment)
        st.session_state.maintenance_requests[student_name] = request
        st.success("Maintenance request submitted!")
    else:
        st.error("Please fill in all required fields.")
