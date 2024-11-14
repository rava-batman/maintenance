import streamlit as st
from datetime import datetime

class MaintenanceRequest:
    def __init__(self, student_name, room_number, issue_type, details, attachment=None):
        self.student_name = student_name
        self.room_number = room_number
        self.issue_type = issue_type
        self.details = details
        self.attachment = attachment
        self.status = "Pending"
        self.created_at = datetime.now()
        self.scheduled_time = None

    def update_status(self, new_status, scheduled_time=None):
        self.status = new_status
        self.scheduled_time = scheduled_time

    def get_status(self):
        if self.scheduled_time:
            return f"{self.status} at {self.scheduled_time.strftime('%I:%M %p')}"
        return self.status

maintenance_requests = {}
