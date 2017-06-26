from easygui import *
from lxml import html
import requests
page = requests.get('http://mangafox.me/manga/')
tree = html.fromstring(page.text)
namelist = tree.xpath('//div[@class="manga_list"]/ul/li/a/text()')
linklist = tree.xpath('//div[@class="manga_list"]/ul/li/a/@href')
TITLE = "QG Loader"
ind1 = 0 
#-----------------------------------------------------------------------
#          createCourse
#-----------------------------------------------------------------------
def createCourse():
    global connection, cursor, courseId, studentId

    msg = "Enter data about the new course"
    fieldNames = ["Course ID", "Course Name"]
    fieldValues = []

    while True:
        fieldValues = multenterbox(msg, TITLE, fieldNames, fieldValues)
        if fieldValues == None: return

        # make sure that none of the fields was left blank
        errors = 0
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                msgbox('"%s" is a required field.' % fieldNames[i])
                errors += 1
                break
        if errors > 0: continue

        newCourseId = fieldValues[0]
        newCourseId = "".join(newCourseId.split())  # remove all whitespace

        if existsCourse(newCourseId):
            msgbox("Course " + newCourseId + " already exists.", "Error")
            continue
        else:
            break

    newCourseId, courseName = fieldValues
    cursor.execute(
        'INSERT INTO courses '
        '(courseId, courseName) '
        'VALUES (?, ?)',
        (newCourseId, courseName)
    )
    connection.commit()
    courseId = newCourseId  # reset the global variable

    msg = "Course " + courseId + " (" + courseName + ") was created."
    msgbox(msg, TITLE)



#-----------------------------------------------------------------------
#          main
#-----------------------------------------------------------------------
def main():

        msg = "Selecione Um manga"
        choice = choicebox(msg, TITLE, namelist)
        while ind1 < len(namelist):
        	if choice == choice[ind1]:
        		createCourse()
        	ind1 += 1