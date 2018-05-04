#!/usr/bin/env
# -*-coding:utf-8-*-

import json

from Application import Application
from Invitation import Invitation
from SeekerProfile import SeekerProfile
from User import Seeker, Recruiter


class UserManager:
    def __init__(self):
        self.seeker_list = []
        self.job_list = []
        self.recruiter_list = []
        self.keyword_list = []

    # TODO: Read and write data from and to files
    def load_user_data(self):
        try:
            user_file = open("user.json")
            data = json.load(user_file)

            # Load seekers' data
            seeker_data = data["seeker"]
            for seeker in seeker_data:
                # Read basic seeker data
                username = seeker["username"]
                password = seeker["password"]
                the_seeker_id = seeker["seekerId"]

                # Read and initialize profile data
                profile_data = seeker["profile"]
                name = profile_data["name"]
                gender = profile_data["gender"]
                mobile = profile_data["mobile"]
                email = profile_data["email"]
                education_level = profile_data["educationLevel"]
                work_year = profile_data["workYear"]
                skill_set = profile_data["skillset"]
                profile = SeekerProfile(seeker_id, name, gender, mobile, email, education_level, work_year, skill_set)

                # Read seekers' invitation list
                invitation_list = seeker["invitationList"]
                inv_list = []
                for invitation in invitation_list:
                    job_id = invitation["jobId"]
                    seeker_id = invitation["seekerId"]
                    interview_date = invitation["interviewDate"]
                    invitation_status = invitation["invitationStatus"]
                    invitation_message = invitation["invitationMessage"]
                    inv_list += Invitation(job_id, seeker_id, interview_date, invitation_message, invitation_status)

                # Read user's application list
                application_list = seeker["applicationList"]
                app_list = []
                for application in application_list:
                    job_id = application["jobId"]
                    seeker_id = application["seekerId"]
                    application_date = application["applicationDate"]
                    application_message = application["applicationMessage"]
                    application_status = application["applicationStatus"]
                    app_list += Application(seeker_id, job_id, application_message, application_status,
                                            application_date)

                # Initialize and save current seeker's data into list
                self.seeker_list += Seeker(username, password, profile, inv_list, app_list, the_seeker_id)

            # load Recruiters' data
            recruiter_data = data["recruiter"]
            for recruiter in recruiter_data:
                username = recruiter["username"]
                password = recruiter["password"]
                the_recruiter_id = recruiter["recruiterId"]
                company_name = recruiter["companyName"]
                category_list = recruiter["categoryList"]

                # Read recruiters' invitation list
                invitation_list = recruiter["invitationList"]
                inv_list = []
                for invitation in invitation_list:
                    job_id = invitation["jobId"]
                    seeker_id = invitation["seekerId"]
                    interview_date = invitation["interviewDate"]
                    invitation_status = invitation["invitationStatus"]
                    invitation_message = invitation["invitationMessage"]
                    inv_list += Invitation(job_id, seeker_id, interview_date, invitation_message, invitation_status)

                # Read user's application list
                application_list = recruiter["applicationList"]
                app_list = []
                for application in application_list:
                    job_id = application["jobId"]
                    seeker_id = application["seekerId"]
                    application_date = application["applicationDate"]
                    application_message = application["applicationMessage"]
                    application_status = application["applicationStatus"]
                    app_list += Application(seeker_id, job_id, application_message, application_status,
                                            application_date)

                # Initialize and save current seeker's data into list
                self.seeker_list += Recruiter(username, password, company_name, inv_list, category_list, app_list,
                                              the_recruiter_id)

        except FileNotFoundError:
            print("File not found, no data been loaded")
        except IOError:
            print("IO exception, data been wrongly inputted")

        finally:
            user_file.close()

    def restore_data(self):
        pass

    # TODO: Login and Account
    # If username and password is matched, then return the user. Else, return False to caller.
    def login(self, user_name, password):
        for user in self.seeker_list:
            if user.username == user_name and user.password == password:
                return user

        for user in self.recruiter_list:
            if user.username == user_name and user.password == password:
                return user

        return False

    def create_seeker_account(self, user_name, password):
        pass

    def create_recruiter_account(self, user_name, password):
        pass

    def verify_username(self, username):
        pass

    # TODO: Recommendation
    def recommendation_for_seeker(self,seeker_id):
        pass

    def recommendation_for_recruiter(self, recruiter_id):
        pass

    # TODO: Invitation
    def create_invitation(self):
        pass

    def check_invitation_status(self):
        pass

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

    # TODO Category
    def create_category(self):
        pass

    def modify_category(self):
        pass

    def delete_category(self):
        pass
