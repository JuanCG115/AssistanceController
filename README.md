Employee Facial Recognition System

This Python script is a basic facial recognition attendance system. It uses a webcam to capture a person's face and then identifies them by comparing it to a database of pre-registered employee photos. The system then logs the recognized employee's name and the current time into a CSV file named registro.csv. It's a great demonstration of applying computer vision libraries like OpenCV and face_recognition for a practical application.

Key Features

- Automated Recognition: Compares a live camera feed with a pre-existing image database to identify individuals.

- Database Management: It reads a folder of employee images (Empleados) and their names to create a facial "database." Each face is converted into a numerical encoding, or a unique digital signature.

- Attendance Logging: It records the name and time of entry for each recognized employee into a registro.csv file, avoiding duplicate entries for the same person.

- Visual Feedback: A box and the recognized employee's name are drawn around the detected face in the camera feed.

- Security Check: It uses a face distance threshold (0.6) to ensure the captured face is a good match for one in the database, preventing incorrect identifications. If the distance is too great, it correctly identifies the person as "not an employee."

How to Use

- Dependencies: You'll need Python 3 and the following libraries.

      Bash
      
      pip install opencv-python face_recognition numpy
  
- Setup Employee Database:

  - Create a folder named Empleados in the same directory as the script.

  - Place a photo of each employee in the Empleados folder.

  - Crucially, name each image file with the employee's name (e.g., Juan_Perez.jpg). The script uses this filename to get the employee's name.

- Run the Script:

      Bash
      
      python your_script_name.py
   
- Use: Your webcam will turn on automatically. Position your face in front of the camera, and the system will attempt to recognize you. Upon recognition, your name and the time will be logged in registro.csv, and the camera window will display a green box and your name. Press any key to close the window.
