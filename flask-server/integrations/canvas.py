from canvasapi import Canvas
from canvasapi.course import Course, Assignment
import datetime
import pytz
from time import perf_counter
import pandas as pd
from html2text import html2text
import os
from dotenv import load_dotenv

from integrations.bulletin import Bulletin

bp = Bulletin()

load_dotenv()

CANVAS_TOKEN = os.environ['CANVAS_TOKEN']

API_URL = 'https://psu.instructure.com/'

EST = pytz.timezone('US/Eastern')
CANVAS_DATE_FORMAT = r'%Y-%m-%dT%H:%M:%SZ'
OUTPUT_DATE_FORMAT = r'%a, %b %d at %I:%M %p'

class CanvasClass:
    def __init__(self):
        self.canvas = Canvas(API_URL, CANVAS_TOKEN)
        self.last_check_time = datetime.datetime.now()

    def _get_courses(self):
        classes = []
        ids = []
        courses = self.canvas.get_courses(enrollment_state="active")
        for course in courses:
            classes.append(course.course_code)
            ids.append(course.id)
        
        course_dict = {c: i for c, i in zip(classes, ids)}
        return course_dict
    
    def _get_assignments(self, course_partial):
        course_dict = self._get_courses()
        course_id = 0
        course_str =""

        for key in course_dict.keys():
            if course_partial in key:
                course_id = course_dict[key]
        
        
        try:
            course = self.canvas.get_course(course_id)
            sorted_assignments = sorted(course.get_assignments(),key = lambda a: a.due_at if a.due_at is not None else " ")
            current_time = datetime.datetime.now()
            
            assignment_index = 0
            while assignment_index < len(sorted_assignments) and (sorted_assignments[assignment_index].due_at is None or current_time > datetime.datetime.strptime(sorted_assignments[assignment_index].due_at, CANVAS_DATE_FORMAT)):
                assignment_index += 1

            upcoming_assignments = sorted_assignments[assignment_index:min(assignment_index+5,len(sorted_assignments))]

            course_str = f"The following assignment(s) are due for {course.name[:9]}:\n"

        except:
            pass
        
        course_name, bulletin_link = bp._get_classes(course_partial)


        if course_str == "":
            result_str = f"Information for {course_partial} ({course_name[11:-9]} - {course_name[-9:]}) can be found at: {bulletin_link}"
        else:
            result_str = f"Information for {course_partial} ({course_name[11:-9]} - {course_name[-9:]}) can be found at: {bulletin_link}\n\n" + course_str
        
        try:
            for assignment in upcoming_assignments:
                
                due_date = pytz.utc.localize(datetime.datetime.strptime(assignment.due_at, CANVAS_DATE_FORMAT))
                due_date_est = due_date.astimezone(EST)

                result_str += f"\t• {assignment.name} | Due on: {due_date_est.strftime(OUTPUT_DATE_FORMAT)}\n"
        except:
            pass

        return result_str
    
    def _get_all_assignments(self, course_partial):
        course_dict = self._get_courses()
        course_id = 0

        for key in course_dict.keys():
            if course_partial in key:
                course_id = course_dict[key]
                

        course = self.canvas.get_course(course_id)
        sorted_assignments = sorted(course.get_assignments(),key = lambda a: a.due_at if a.due_at is not None else " ")
        current_time = datetime.datetime.now()
        
        # print(sorted_assignments)

        assignment_index = 0
        while assignment_index < len(sorted_assignments) and (sorted_assignments[assignment_index].due_at is None or current_time > datetime.datetime.strptime(sorted_assignments[assignment_index].due_at, CANVAS_DATE_FORMAT)):
            assignment_index += 1

        # upcoming_assignments = sorted_assignments[assignment_index:min(assignment_index+5,len(sorted_assignments))]

        result_str = f"These are the due dates for the following {course.name[:9]} assignment(s):\n"
        for assignment in sorted_assignments:
            if assignment.due_at is not None:
                date_str = pytz.utc.localize(datetime.datetime.strptime(assignment.due_at, CANVAS_DATE_FORMAT)).astimezone(EST).strftime(OUTPUT_DATE_FORMAT)
            else:
                date_str = "No due date"

            result_str += f"\t• {assignment.name} | Due at: {date_str}\n"

        return result_str

    # def _get_syllabus(self, course_partial):
    #     course_dict = self._get_courses()
    #     course_id = 0

    #     for key in course_dict.keys():
    #         if course_partial in key:
    #             course_id = course_dict[key]
                
    #     try:
    #         course = self.canvas.get_course(course_id)
    #     except:
    #         return "Course not found or not currently enrolled"

    #     return 'dudes'