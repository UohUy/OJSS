#!/usr/bin/env
# -*-coding:utf-8-*-


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Seeker(User):
    __counter = 0

    def __init__(self, username, password, profile, invitation_list, application_list):
        User.__init__(self, username, password)
        self.seeker_id = self.__counter
        self.profile = profile
        self.invitation_list = invitation_list
        self.application_list = application_list
        self.__counter += 1


class Recruiter(User):
    def __init__(self, username, password, id, company_name, invitation_list, category_list, application_list):
        User.__init__(self, username, password)
        self.id = id
        self.company_name = company_name
        self.invitation_list = invitation_list
        self.category_list = category_list
        self.application_list = application_list
