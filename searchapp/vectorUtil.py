from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone
import os

from  vectorsearch_app.settings import OPENAI_API,PINECONE_KEY

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API)


def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["property_url"] = record.get("property_url")
    metadata["primary_photo"] = record.get("primary_photo")
    metadata["status"] = record.get("status")
    metadata["style"] = record.get("style")
    metadata["street"] = record.get("street")
    metadata["bedroom"] = record.get("beds")
    metadata["sqft"] = record.get("sqft")
    metadata["list_price"] = record.get("list_price")
    metadata["sold_price"] = record.get("sold_price")
    metadata["stories"] = record.get("stories")
    metadata["price_per_sqft"] = record.get("price_per_sqft")
    metadata["year_built"] = record.get("year_built")
    metadata["city"] = record.get("city")
    metadata["state"] = record.get("state")
    metadata["zip_code"] = record.get("zip_code")
    metadata["full_baths"] = None if record.get("full_baths") == 'null' else record.get("full_baths") == None
    metadata["half_baths"] = None if record.get("half_baths") == 'null' else record.get("half_baths") == None

    return metadata

   

def load_document():
    
    loader = JSONLoader(
        file_path="property.json",
        jq_schema='.data[]',
        text_content=False,
        metadata_func=metadata_func,
        content_key='city'
    )
    
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    
    index_name = "property-search"

    Pinecone.from_documents(docs, embeddings, index_name=index_name)
    
   
    
  




def get_semilarity_search(query):
   
    text_field = "text"  # the metadata field that contains our text
    index = "property-search"
    # # # initialize the vector store object
    vectorstore = Pinecone(
        index_name=index, 
        embedding=embeddings,
        text_key=text_field,
        pinecone_api_key=PINECONE_KEY
    )
    
    response = vectorstore.similarity_search(
        query=query,
        k=4
        
    )
    
    real_estate_pro = [data.metadata for data in response ]
    
    #print(real_estate_pro)
    

    
    return real_estate_pro

#load_document()
#get_semilarity_search("2 bedroom san diago")
