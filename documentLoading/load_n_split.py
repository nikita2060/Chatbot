# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
# from langchain_community.vectorstores import Chroma
#
#
# PDF_PATH = "../documents/Rich-Dad-Poor-Dad.pdf"
#
# # create loader
# loader = PyPDFLoader(PDF_PATH)
# # split document
# pages = loader.load_and_split()
#
# # embedding function
# embedding_func = SentenceTransformerEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )
#
# # create vector store
# vectordb = Chroma.from_documents(
#     documents=pages,
#     embedding=embedding_func,
#     persist_directory=f"../vector_db",
#     collection_name="rich_dad_poor_dad")
#
# # make vector store persistant
# vectordb.persist()
#
# import pandas as pd
# from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
# from langchain_community.vectorstores import Chroma
#
# # CSV path
# csv_path = "C:/Users/Asus/PycharmProjects/Fire_chatbot/fire-incidents_1 (1).csv"
#
# # Load CSV file
#
# # Extract text from CSV
# # pages = df[''].tolist()  # Replace 'text_column' with the appropriate column name containing text
#
#
# # Read the CSV data into a DataFrame
# data = pd.read_csv(csv_path)
#
# # Create a dictionary to store the knowledge base
# knowledge_base = {}
#
# # Extract relevant fields and populate the knowledge base
# for index, row in data.iterrows():
#     incident_number = row["incidentnum"]
#     alarm_time = row["alarmtime"]
#     year = row["year"]
#     nature_of_incident = row["incitypedesc"]  # Assuming "incitypedesc" describes the emergency
#     city = row["incity"]
#     mutual_aid = row["mutl_aid"]
#     station = row["station"]
#     shift = row["shift"]
#     current_district = row["current_district"]
#     current_fmx = row["current_fmz"]  # Assuming "current_fmz" refers to Fire Zone
#     latitude = row["latitude"]
#     longitude = row["longitude"]
#     additional_notes = row["geopoint"]  # Assuming "geopoint" contains additional notes
#
#     # Create a dictionary entry for each incident
#     knowledge_base[incident_number] = {
#         "alarm_time": alarm_time,
#         "year": year,
#         "nature_of_incident": nature_of_incident,
#         "city": city,
#         "mutual_aid": mutual_aid,
#         "station": station,
#         "shift": shift,
#         "current_district": current_district,
#         "current_fmx": current_fmx,
#         "latitude": latitude,
#         "longitude": longitude,
#         "additional_notes": additional_notes
#     }
#
# # Print a sample entry from the knowledge base (optional)
# print(knowledge_base[""])  # Replace with any incident number from your data
#
# # Embedding function
# embedding_func = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#
# # Create vector store
# vectordb = Chroma.from_documents(
#     documents=pages,
#     embedding=embedding_func,
#     persist_directory="../vector_db",
#     collection_name="knowledge_base"
# )
#
# # Make vector store persistent
# vectordb.persist()

import pandas as pd
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

# CSV path
csv_path = "C:/Users/Asus/PycharmProjects/Fire_chatbot/fire-incidents_1 (1).csv"


# Read the CSV data into a DataFrame
data = pd.read_csv(csv_path)

# Create a dictionary to store the knowledge base
knowledge_base = {}

# Extract relevant fields and populate the knowledge base
for index, row in data.iterrows():
    try:
        incident_number = row["incidentnum"]
        alarm_time = row["alarmtime"]
        year = row["year"]
        nature_of_incident = row["incitypedesc"]  # Assuming "incitypedesc" describes the emergency
        city = row["incity"]
        mutual_aid = row["mutl_aid"]
        station = row["station"]
        shift = row["shift"]
        current_district = row["current_district"]
        current_fmx = row["current_fmz"]  # Assuming "current_fmz" refers to Fire Zone
        latitude = row["latitude"]
        longitude = row["longitude"]
        additional_notes = row["geopoint"]  # Assuming "geopoint" contains additional notes

        # Create a dictionary entry for each incident
        knowledge_base[incident_number] = {
            "alarm_time": alarm_time,
            "year": year,
            "nature_of_incident": nature_of_incident,
            "city": city,
            "mutual_aid": mutual_aid,
            "station": station,
            "shift": shift,
            "current_district": current_district,
            "current_fmx": current_fmx,
            "latitude": latitude,
            "longitude": longitude,
            "additional_notes": additional_notes
        }
    except KeyError as e:
        print("Ignoring")


# Print a sample entry from the knowledge base (optional)


# Text extraction for embedding (Optional)
# Replace 'incitypedesc' with the column containing descriptions if needed
text_data = data["incitypedesc"]
pages = text_data.tolist()


# Embedding function (Optional)
embedding_func = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


# Create vector store (Optional)
if pages:  # Check if pages list is not empty
    vectordb = Chroma.from_documents(
        documents=pages,
        embedding=embedding_func,
        persist_directory="../vector_db",
        collection_name="knowledge_base"
    )
    vectordb.persist()

