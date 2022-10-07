from typing import Any, Text, Dict, Union, List, Optional, TYPE_CHECKING
import json
import shared.utils

if TYPE_CHECKING:
    from tileai.model_training import TrainingResult


def run(**kwargs: "Dict[Text, Any]") -> None:
    
    import tileai.http.httprun
 

    
    _endpoints = "0.0.0.0"
    
   
    kwargs = shared.utils.minimal_kwargs(
        kwargs, tileai.http.httprun.serve_application
    )
    tileai.http.httprun.serve_application(
        model_path="models/new",
        endpoints=_endpoints,
        #port=port,
        **kwargs
    )
    


def train(nlu:"Text",
          out:"Text")-> "TrainingResult":
    
    from tileai.model_training import train

    with open(nlu) as jsonFile:
       jsonObject = json.load(jsonFile)
       jsonFile.close()

    return train(jsonObject,out)

def query(model, query_text):
    from tileai.model_training import query
    return query(model, query_text)

