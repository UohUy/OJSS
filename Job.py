#!/usr/bin/env
# -*-coding:utf-8-*-


class Job:
    __counter = 0

    def __init__(self, recruiter_id, job_description, min_salary, max_salary, location, category,
                 required_skill_set, company_name):
        self.job_id = self.__counter
        self.recruiter_id = recruiter_id
        self.description = job_description
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.location = location
        self.category = category
        self.required_skill_set = required_skill_set
        self.company_name = company_name
        self.__counter += 1

