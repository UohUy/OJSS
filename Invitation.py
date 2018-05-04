#!/usr/bin/env
# -*-coding:utf-8-*-

invitation_status = ("waiting for response", "being reviewed", "invited to invitation")


class Invitation:
    def __init__(self, invited_job, interview_date, seeker_id, recruiter_id, invitation_msg,
                 status="waiting for response"):
        self.invited_job = invited_job
        self.interview_date = interview_date
        self.seeker_id = seeker_id
        self.recruiter_id = recruiter_id
        self.status = status
        self.msg = invitation_msg

    def set_invitation_status(self, status):
        if status in invitation_status:
            self.status = status
            return True
        else:
            return False
