import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("D:\D\suong\\app\db\credential.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'capstoneproject-ca420.appspot.com'
})

def download_audio(download_url, audio_name):
    response = requests.get(download_url)

    with open(audio_name, 'wb') as f:
        f.write(response.content)

def upload_audio(audio_name):
    bucket = storage.bucket()
    upload_path = f"/load/audios/{audio_name}"
    blob = bucket.blob(upload_path)
    blob.upload_from_filename("images/mountains.mp4")