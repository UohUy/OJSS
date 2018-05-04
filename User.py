#!/usr/bin/env
# -*-coding:utf-8-*-


class _User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.invitation_list = []


class Seeker(_User):
    __counter = 0

    def __init__(self, username, password, profile, invitation_list, application_list, seeker_id=None):
        _User.__init__(self, username, password)
        if seeker_id is None:
            self.id = self.__counter
            self.__counter += 1
        else:
            self.id = seeker_id
        self.profile = profile
        self.invitation_list = invitation_list
        self.application_list = application_list


class Recruiter(_User):
    __counter = 0

    def __init__(self, username, password, company_name, invitation_list, category_list, application_list,
                 recruiter_id=None):
        _User.__init__(self, username, password)
        if recruiter_id is None:
            self.id = self.__counter
            self.__counter += 1
        else:
            self.id = recruiter_id
        self.company_name = company_name
        self.invitation_list = invitation_list
        self.category_list = category_list
        self.application_list = application_list
