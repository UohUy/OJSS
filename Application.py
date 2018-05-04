#!/usr/bin/env
# -*-coding:utf-8-*-
import time

APPLICATION_STATUS = ("waiting for response", "being reviewed", "invited to invitation")


class Application:
    def __init__(self, seeker_id, job_id, application_msg, status="waiting for Respond", date=None):
        self.seeker_id = seeker_id
        self.job_id = job_id
        if date is None:
            self.date = Application.date_from_system()
        else:
            self.date = date
        self.status = status
        self.msg = application_msg

    @staticmethod
    def date_from_system():
        return time.strftime("%Y-%m-%d", time.localtime())

    def set_status(self, new_status):
        if new_status in APPLICATION_STATUS:
            self.status = new_status
            return True
        else:
            return False

