#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json

from fdk import response
#from langchain_community.llms import Cohere
#from langchain_community.embeddings import CohereEmbeddings
#from langchain_community.embeddings import SentenceTransformerEmbeddings
#import os
#from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.retrievers import ContextualCompressionRetriever
#from langchain.retrievers.document_compressors import LLMChainExtractor
#from langchain_community.vectorstores import Chroma
##import chromadb
##from chromadb.config import Settings
#from pprint import pprint
import cohere
import time

def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)

    print("Vale of name = ", name, flush=True)
    print("Exiting Python Hello World handler", flush=True)
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
