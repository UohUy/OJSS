#!/usr/bin/env
# -*-coding:utf-8-*-
import time

application_status = ("waiting for response", "being reviewed", "invited to invitation")


class Application:
    def __init__(self, seeker_id, job_id, application_status="waiting for Respond"):
        self.seeker_id = seeker_id
        self.job_id = job_id
        self.application_date = Application.init_current_date_to_variable()
        self.application_status = application_status

    @staticmethod
    def init_current_date_to_variable():
        return time.strftime("%Y-%m-%d", time.localtime())

    def set_status(self, new_status):
        if new_status in application_status:
            self.application_status = new_status
            return True
        else:
            return False

