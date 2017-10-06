"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
For Filling TimeSheet
Fill multiple time sheet in single click? DrawBack, No future Time sheet Scope
Change Tkinker name in Python 3

Author: Prajinkya Pimpalghare

Date: 10-October-2017
Version: 1.1
Input Variable: PS. No. & pass_word | No. of Hours for specific filed
Basic Requirement Selenium module, and Web driver for chrome
============================================================================"""
from __future__ import print_function
import time
from Tkinter import Frame, Tk, Label, Entry, E, Button, LEFT
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class LoginFrame(Frame, object):
    """
    For Creating login Frame
    """

    def __init__(self, master):
        """
        Initializing Variables for Creating GUI
        :rtype: object
        :param master:
        """
        super(LoginFrame, self).__init__(master)
        # ---------------------------------------------------------------------------
        # Initialization Of Basic Elements
        # ---------------------------------------------------------------------------
        # For Username And pass_word--------------------------------------------------
        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        # ----------------------------------------------------------------------------
        # For Filling No. Of Hours In Boxes-------------------------------------------
        self.heading1 = Label(self, text="Task/Items")
        self.entries = []
        self.box_value = []
        self.counter = []
        self.values = [entry.get() for entry in self.entries]
        self.box = [ent for ent in self.box_value]
        self.count = [cou for cou in self.counter]
        row, index_next, item_row_next, day_next = 5, 1, 0, 1
        for key, value in TIME_SHEET_FIELD_ITEMS.iteritems():
            if row == 27:
                row, index_next, item_row_next, day_next = 5, 10, 8, 10
                index, item_row = index_next, item_row_next
            else:
                index, item_row = index_next, item_row_next
            self.key_label = Label(self, text=key)
            for day_iter in DAYS:
                self.day = Label(self, text=day_iter)
                self.day.grid(row=4, column=index)
                self.item = Entry(self, width=5)
                self.entries.append(self.item)
                self.box_value.append(value)
                self.item.grid(row=row, column=index)
                self.counter.append(index - day_next)
                index += 1
            self.key_label.grid(row=row, column=item_row)
            row += 1
        self.log_button = Button(self, text="Submit Time Sheet",
                                 command=self._login_btn_clicked)
        self.log_button.grid(row=0, column=8)

        self.pack()

    # -----------------------------------------------------------------------------
    # Submit Button Function---------------------------------------------------------
    def _login_btn_clicked(self):
        """
        It will monitor the action of timesheet button
        """
        username = self.entry_1.get()
        pass_word = self.entry_2.get()
        self.values = [entry.get() for entry in self.entries]
        self.box = [ent for ent in self.box_value]
        self.count = [cou for cou in self.counter]
        # ----------------------------------------------------------------------------------
        # Main Code For Accessing Portal
        # ----------------------------------------------------------------------------------
        browser = webdriver.Chrome()
        browser.get(URL)
        login_area = browser.find_element_by_xpath("//div[@class='login_area']")
        login = login_area.find_element_by_name("loginId")
        password = login_area.find_element_by_name("password")
        login.send_keys(username)
        password.send_keys(pass_word)
        browser.find_element_by_id("QTP_LoginButton").click()
        try:
            browser.find_element_by_id("LOCK_Timesheet").click()
            browser.find_element_by_id("LOCK_Current_Week").click()
        except Exception as error:
            print("Unable To Login Please provide correct credentials")
            raise error
        browser.switch_to.frame(browser.find_element_by_id("contentframe"))

        def fill_time_sheet(field, num_of_hours, day):
            """
            Function to fill No. of Hours on specific day
            :rtype: None
            :param field:
            :param num_of_hours:
            :param day:
            """
            try:
                [browser.find_element_by_name(field + str(day)).send_keys(Keys.BACKSPACE)
                 for i in range(4)]
                browser.find_element_by_name(field +
                                             str(day)).send_keys(num_of_hours)
            except Exception as error:
                print('Cannot fill Time sheet for this day as future time sheet cannot be filled')
                raise error

        for value, box, count in zip(self.values, self.box, self.count):
            if value != '':
                fill_time_sheet(box, value, count)
        time.sleep(5)
        # browser.find_element_by_id("QTP_KEY_LABEL_Save").click()
        time.sleep(5)
        # browser.find_element_by_id("QTP_KEY_BUTTON_Route").click()


if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    # RequiredLists
    # -----------------------------------------------------------------------------
    URL = "https://example.yoururl.com"
    TIME_SHEET_FIELD_ITEMS = {'Projects Process definition': 'actualHoursSubmitted_0_0_',
                              'Project Management Plan preparation': 'actualHoursSubmitted_0_1_',
                              'Senior Management reviews': 'actualHoursSubmitted_0_2_',
                              'Risk Monitoring and Control': 'actualHoursSubmitted_0_3_',
                              'Project Management Plan tracking': 'actualHoursSubmitted_0_4_',
                              'Gather & Analyse Requirements': 'actualHoursSubmitted_0_5_',
                              'Review of RS': 'actualHoursSubmitted_0_6_',
                              'High level design': 'actualHoursSubmitted_0_7_',
                              'Review of High level Design': 'actualHoursSubmitted_0_8_',
                              'Detailed level design': 'actualHoursSubmitted_0_9_',
                              'Review of Detailed level Design': 'actualHoursSubmitted_0_10_',
                              'Coding in C': 'actualHoursSubmitted_0_11_',
                              'Formal Peer review of Code in C': 'actualHoursSubmitted_0_12_',
                              'Coding in C++': 'actualHoursSubmitted_0_13_',
                              'Formal Peer review of Code in C++': 'actualHoursSubmitted_0_14_',
                              'Coding in C#': 'actualHoursSubmitted_0_15_',
                              'Formal Peer review of Code in C#': 'actualHoursSubmitted_0_16_',
                              'Coding in Java': 'actualHoursSubmitted_0_17_',
                              'Formal Peer review of Code in Java': 'actualHoursSubmitted_0_18_',
                              'Coding in python': 'actualHoursSubmitted_0_19_',
                              'Formal Peer review of Code in Python': 'actualHoursSubmitted_0_20_',
                              'Coding in Matlab': 'actualHoursSubmitted_0_21_',
                              'Formal Peer review of Code in Matlab': 'actualHoursSubmitted_0_22_',
                              'Re-review of code in Matlab - CR': 'actualHoursSubmitted_0_23_',
                              'Re-work on review findings': 'actualHoursSubmitted_0_24_',
                              'Prepare Unit Test plan': 'actualHoursSubmitted_0_25_',
                              'Review of Unit Test plan': 'actualHoursSubmitted_0_26_',
                              'Setting up the Unit Test environment': 'actualHoursSubmitted_0_27_',
                              'Prepare Integration Test plan': 'actualHoursSubmitted_0_28_',
                              'Review of Integration Test plan': 'actualHoursSubmitted_0_29_',
                              'Prepare Validation Test plan': 'actualHoursSubmitted_0_30_',
                              'Review of Validation Test plan': 'actualHoursSubmitted_0_31_',
                              'Internal Training': 'actualHoursSubmitted_0_32_',
                              'External training': 'actualHoursSubmitted_0_33_',
                              'Process Handholding': 'actualHoursSubmitted_0_34_',
                              'Audits': 'actualHoursSubmitted_0_35_',
                              'Audit Tracking': 'actualHoursSubmitted_0_36_',
                              'Process Improvements': 'actualHoursSubmitted_0_37_',
                              'Release and Implementation': 'actualHoursSubmitted_0_38_',
                              'Internal POC': 'actualHoursSubmitted_0_39_',
                              'Supporting on RFQ & Proposals': 'actualHoursSubmitted_0_40_',
                              'Process Documentation': 'actualHoursSubmitted_0_41_',
                              'Formal review of code in C': 'actualHoursSubmitted_0_42_',
                              'Leave': 'actualHoursSubmitted_0_43_'}
    TIME_SHEET_FIELD_DAY = {'Monday': '0', 'Tuesday': '1', 'Wednesday': '2',
                            'Thursday': '3', 'Friday': '4', 'Saturday': '5',
                            'Sunday': '6'}
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # -------------------------------------------------------------------------------------
    # Main
    # -------------------------------------------------------------------------------------
    ROOT = Tk()
    LOGIN = LoginFrame(ROOT)
    LOGIN.pack(side=LEFT)
    ROOT.mainloop()
