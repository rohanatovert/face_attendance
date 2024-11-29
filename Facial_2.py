import cv2
import numpy as np
import face_recognition as face_rec
import os
import pandas as pd
from datetime import datetime
import winsound
import csv

# Initialize sound alert
sound_duration = 1000  # milliseconds
sound_frequency = 1000  # Hz
def main(video,table_A):
    def resize(img, size):
        width = int(img.shape[1]*size)
        height = int(img.shape[0] * size)
        dimension = (width, height)
        return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)


    path = 'Images_2'
    studentImg = []
    studentName = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            curimg = cv2.imread(os.path.join(subdir, file))
            studentImg.append(curimg)
            #studentName.append(subdir.split("/")[-1])
            studentName.append(os.path.basename(subdir))



    def findEncoding(images):
        imgEncodings = []
        for img in images:
            img = resize(img, 1.0)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_rec.face_encodings(img, num_jitters=10, model='arcface')
            if len(face_encodings) > 0:
                encodeimg = face_encodings[0]
                imgEncodings.append(encodeimg)
        return imgEncodings
    
    
    def MarkAttendance(name):
        # Create a folder for the person's attendance records
        person_folder_name = os.path.join('person_attendance', f'{name}')
        if not os.path.exists(person_folder_name):
            os.makedirs(person_folder_name)

        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        month_string = now.strftime('%Y-%m')
        dt_string = now.strftime('%H:%M:%S')
        present = 'Present'
        
        # Create a folder for the daily attendance
        daily_folder_name = 'daily_attendance'
        if not os.path.exists(daily_folder_name):
            os.makedirs(daily_folder_name)
        daily_file_name = os.path.join(daily_folder_name, f'attendance_daily_{date_string}.csv')
        
        # create a folder for the mothly attendance 
        monthly_folder_name = os.path.join('monthly_attendance', month_string)
        if not os.path.exists(monthly_folder_name):
            os.makedirs(monthly_folder_name)
        monthly_file_name = os.path.join(monthly_folder_name, f'{month_string}.csv')
        
        person_file_name = os.path.join(person_folder_name, f'{name}_{month_string}.csv')

        # Add column names as first line of file if file is empty
        if not os.path.exists(daily_file_name) or os.path.getsize(daily_file_name) == 0:
            with open(daily_file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Date', 'Time', 'Present'])

        if not os.path.exists(person_file_name) or os.path.getsize(person_file_name) == 0:
            with open(person_file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Date', 'Time', 'Present'])

        if not os.path.exists(monthly_file_name) or os.path.getsize(monthly_file_name) == 0:
            with open(monthly_file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Date', 'Time', 'Present'])

        # Check for existing records in daily file
        name_found = False
        with open(daily_file_name, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader) # skip the header row
            for row in reader:
                if row[0] == name and row[1] == date_string:
                    name_found = True
                    attendance_record = {
                        "Name": row[0],
                        "Date": row[1],
                        "Time": row[2],
                        "Present": row[3]
                    }
                    df = pd.DataFrame(attendance_record, index=[0])
                    table_A.dataframe(df)
                    break

            if not name_found:
                # Mark as present
                with open(daily_file_name, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, date_string, dt_string, present])
                    print(f"{name}, {date_string}, {dt_string}, {present}")
                    #table_A.add_row([name, date_string, dt_string, present])

        # Check for existing records in monthly file
        with open(monthly_file_name, 'a+') as f:
            f.seek(0)
            myDatalist = f.readlines()

            # Add column names as first line of file if file is empty
            if len(myDatalist) == 0:
                f.write('Name,Date,Time,Present\n')

            name_found = False
            for line in myDatalist:
                entry = line.strip().split(',')
                if entry[0] == name and entry[1] == date_string:
                    name_found = True
                    break

            if not name_found:
                # Mark as present
                with open(monthly_file_name, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, date_string, dt_string, present])



        # Check for existing records in person file
        with open(person_file_name, 'a+') as f:
            f.seek(0)
            myDatalist = f.readlines()


            # Add column names as first line of file if file is empty
            if len(myDatalist) == 0:
                f.write('Name,Date,Time,Present\n')

            name_found = False
            for line in myDatalist:
                entry = line.strip().split(',')
                if entry[0] == name and entry[1] == date_string:
                    name_found = True
                    break

            if not name_found:
                # Mark as present
                f.write(f'{name},{date_string},{dt_string},{present}\n')



    
    
    
    """def MarkAttendance(name):
        
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        month_string = now.strftime('%Y-%m')
        dtString = now.strftime('%H:%M:%S')
        present = 'Present'



        daily_file_name = f'attendance_daily_{date_string}.csv'
        monthly_file_name = f'attendance_{month_string}.csv'
        person_file_name = f'{name}_{month_string}.csv'

        # Add column names as first line of file if file is empty
        if not os.path.exists(daily_file_name):
            with open(daily_file_name, 'a+') as f:
                f.write('Name,Date,Time,Present\n')

        if not os.path.exists(person_file_name):
            with open(person_file_name, 'a+') as f:
                f.write('Name,Date,Time,Present\n')

        # Check for existing records in daily file
        name_found = False
        with open(daily_file_name, 'r+') as f:
            myDatalist = f.readlines()

            for line in myDatalist:
                entry = line.strip().split(',')
                if entry[0] == name and entry[1] == date_string:
                    name_found = True
                    attendance_record = {
                        "Name": entry[0],
                        "Date": entry[1],
                        "Time": entry[2],
                        "Present": entry[3]
                    }
                    df=pd.DataFrame(attendance_record,index=[0])
                    table_A.dataframe(df)
                    break

            if not name_found:
                # Mark as present
                with open(daily_file_name, 'a+') as f:
                    f.write(f'{name},{date_string},{dtString},{present}\n')
                    print(f"{name}, {date_string}, {dtString}, {present}")
                    #table_A.add_row([name, date_string, dtString, present])

        # Check for existing records in monthly file
        with open(monthly_file_name, 'a+') as f:
            f.seek(0)
            myDatalist = f.readlines()

            # Add column names as first line of file if file is empty
            if len(myDatalist) == 0:
                f.write('Name,Date,Time,Present\n')

            name_found = False
            for line in myDatalist:
                entry = line.strip().split(',')
                if entry[0] == name and entry[1] == date_string:
                    name_found = True
                    break

            if not name_found:
                # Mark as present
                f.write(f'{name},{date_string},{dtString},{present}\n')

        # Check for existing records in person file
        with open(person_file_name, 'a+') as f:
            f.seek(0)
            myDatalist = f.readlines()


            # Add column names as first line of file if file is empty
            if len(myDatalist) == 0:
                f.write('Name,Date,Time,Present\n')

            name_found = False
            for line in myDatalist:
                entry = line.strip().split(',')
                if entry[0] == name and entry[1] == date_string:
                    name_found = True
                    break

            if not name_found:
                # Mark as present
                f.write(f'{name},{date_string},{dtString},{present}\n')"""


    EncodeList = findEncoding(studentImg)
    #url="http://192.168.0.193:8080//video"
    vid = cv2.VideoCapture(0)
    #vid.open(url)
    while True:
        # Read a frame from the video capture
        success, frame = vid.read()

        # Resize the frame to a smaller size
        Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

        # Find all the faces and encode them
        facesInFrame = face_rec.face_locations(Smaller_frames)
        encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame, model='arcface')

        # Loop through each face in the frame
        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
            
            # Compare the face with the known faces
            matches = face_rec.compare_faces(EncodeList, encodeFace, tolerance=0.5)
            name = "Unknown"
            facedis = face_rec.face_distance(EncodeList, encodeFace)
            matchIndex = np.argmin(facedis)

            # If a match is found, mark attendance and display the name
            if matches[matchIndex]:
                name = studentName[matchIndex].upper()
                MarkAttendance(name)
                cv2.rectangle(frame, (faceloc[3]*4, faceloc[0]*4), (faceloc[1]*4, faceloc[2]*4), (0, 255, 0), 3)
                cv2.putText(frame, name, (faceloc[3]*4 + 6, faceloc[2]*4 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            else:
                cv2.rectangle(frame, (faceloc[3]*4, faceloc[0]*4), (faceloc[1]*4, faceloc[2]*4), (0, 0, 255), 3)
                cv2.putText(frame, name, (faceloc[3]*4 + 6, faceloc[2]*4 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                # Play sound alert for "Unknown" person
                winsound.Beep(sound_frequency, sound_duration)

            

            



        video.image(frame, channels="BGR")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
