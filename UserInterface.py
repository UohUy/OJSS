#!/usr/bin/env
# -*-coding:utf-8-*-


class UserInterface:

    @staticmethod
    def home_page():
        while True:
            print("---------OJSS---------")
            print("1. Sign in")
            print("2. Sign up")
            print("3. Exit")
            print("Your choice: ")
            choice = input()
            if choice == 1:
                UserInterface.sign_in()
            elif choice == 2:
                UserInterface.sign_up()
            elif choice == 3:
                break
            else:
                print("Please try again.\n")

    @staticmethod
    def sign_in():
        while True:
            print("---------OJSS---------")
            print("1. Sign in with seeker account")
            print("2. Sign in with recruiter account")
            print("3. Back to previous page")
            print("Your choice: ")
            choice = input()
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                break
            else:
                print("Please try again.")

    @staticmethod
    def sign_up():
        while True:
            print("---------OJSS---------")
            print("1. Sign up with seeker account")
            print("2. Sign up with recruiter account")
            print("3. Back to previous page")
            print("Your choice: ")
            choice = input()
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                break
            else:
                print("Please try again.")

    @staticmethod
    def seeker_menu():
        pass

    @staticmethod
    def recruiter_menu():
        pass


if __name__ == '__main__':
    UserInterface.home_page()
