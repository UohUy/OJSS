#!/usr/bin/env
# -*-coding:utf-8-*-
import time

application_status = ("waiting for response", "being reviewed", "invited to invitation")


class Application:
    def __init__(self, seeker_id, job_id, application_msg, status="waiting for Respond"):
        self.seeker_id = seeker_id
        self.job_id = job_id
        self.application_date = Application.date_from_system()
        self.application_status = status
        self.application_msg = application_msg

    @staticmethod
    def date_from_system():
        return time.strftime("%Y-%m-%d", time.localtime())

    def set_status(self, new_status):
        if new_status in application_status:
            self.application_status = new_status
            return True
        else:
            return False

