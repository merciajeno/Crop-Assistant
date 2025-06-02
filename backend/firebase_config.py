import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate(r"C:\Users\merci\WebstormProjects\CropAssistant\cropassistant-firebase-adminsdk-fbsvc-fa819d2e35.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client(app)
location = db.collection("location")
location.add({
    "latitude":"23",
    "longitude":"36"
})
print(location.count())