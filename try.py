import face_recognition
image = face_recognition.load_image_file("obama.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)

face_landmarks_list=face_recognition.face_landmarks(image)
print(face_landmarks_list)