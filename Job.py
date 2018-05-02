#!/usr/bin/env
# -*-coding:utf-8-*-


class Job:
    _counter = 0

    def __init__(self, recruiter_id, job_description, min_salary, max_salary, location, catagory,
                 required_skill_set, company_name):
        self.job_id = self._counter
        self.recruiter_id = recruiter_id
        self.description = job_description
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.location = location
        self.catagory = catagory
        self.required_skill_set = required_skill_set
        self.company_name = company_name
        self._counter += 1

    