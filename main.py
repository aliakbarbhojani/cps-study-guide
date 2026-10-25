import cps_code
from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#Create an instance of the FastAPI application
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the study guide using our existing Python function
data = cps_code.load_json("cps213_study_guide.json")

# Homepage endpoint
@app.get("/")
def show_website(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.get("/topic/{topic_id}")
def show_topic(request: Request, topic_id: int):

    # Find the selected topic in our JSON data.
    selected_topic = None

    for topic in data["topics"]:
        if int(topic["id"]) == topic_id:
            selected_topic = topic
            break

    # If the topic doesn't exist, show an error.
    if selected_topic is None:
        return {"error": "Topic not found"}

    # Open the webpage with the selected topic's information.
    return templates.TemplateResponse(
        request=request,
        name="topic.html",
        context={"topic": selected_topic}
    )

# Endpoint to retrieve an individual topic
@app.get("/api/topics/{topic_id}")
def get_topic(topic_id: int):

    # Use the existing Topic class from cps_code.py
    topic = cps_code.Topic(
        None, None, None, None, None, None, None, None
    )

    # Retrieve the selected topic using your existing function
    selected_topic = topic.get_topic(data, topic_id)

    # Return an error if the topic does not exist
    if selected_topic is None:
        return {"error": "Topic not found"}

    # Return the topic information as a dictionary
    return {
        "id": selected_topic.id,
        "title": selected_topic.title,
        "summary": selected_topic.summary,
        "key_points": selected_topic.key_points,
        "worked_example": selected_topic.worked_example,
        "visual": selected_topic.visual,
        "study_tip": selected_topic.study_tip,
        "learn_more": selected_topic.learn_more
    }

# Endpoint to retrieve all topics
@app.get("/api/topics")
def get_topics():
    return data["topics"]