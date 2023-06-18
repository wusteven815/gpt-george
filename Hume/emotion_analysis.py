from utilities import get_emotions
from hume import HumeBatchClient
from hume.models.config import ProsodyConfig
from api_keys import HUME_API_KEY

def get_emotion(file):
    client = HumeBatchClient(HUME_API_KEY)

    files = [file]
    prosody_config = ProsodyConfig()
    callback_url = "https://mockbin.org/bin/08d1f920-801c-4de1-9622-8c7b39658009"
    job = client.submit_job(urls=[], configs=[prosody_config], callback_url=callback_url, files=files)

    print("Running...", job)
    job.await_complete()
    print("Job completed with status: ", job.get_status())

    full_predictions = job.get_predictions()
    return(get_emotions(full_predictions))