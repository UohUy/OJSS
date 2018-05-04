#!/usr/bin/env
# -*-coding:utf-8-*-

import Application
import Dictionary
import Invitation
import Job
import SeekerProfile
from User import Seeker, Recruiter


class OJSSHandler:
    def __init__(self):
        self.user_list = []
        self.seeker_list = []
        self.job_list = []
        self.profile_list = []
        self.recruiter_list = []
        self.invitation_list = []
        self.keyword_list = []
        self.recommendation_list_for_recruiter = []

    # TODO: Read and write data from and to files
    def load_data(self):
        pass

    def restore_data(self):
        pass

    # TODO: Login and Account
    def login(self, user_name, password):
        pass

    def create_seeker_account(self, user_name, password):
        pass

    def create_recruiter_account(self, user_name, password):
        pass

    # TODO: Recommendation
    def recommendation_for_seeker(self,seeker_id):
        pass

    def recommendation_for_recruiter(self, recruitera_id):
        pass

    # TODO: Invitation
    def reply_to_invitation(self):
        pass

    # TODO: Profile Management
    def create_profile(self):
        pass

    def modify_profile(self):
        pass

    def delete_profile_from_list(self):
        pass

    # TODO: Job Management
    def create_job(self, recruiter_id):
        pass

    def add_job_into_list(self, job):
        pass

    def modify_job(self, job_id):
        pass

    def delete_job(self, job_id):
        pass

    def search_jobs(self):
        pass

    def apply_for_job(self):
        pass

