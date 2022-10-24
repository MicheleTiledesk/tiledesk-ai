import asyncio
import logging
import uuid
import os
from functools import partial
from typing import Any, List, Optional, Text, Union, Dict



import tileai.shared.const
from tileai.core.http import server


from sanic import Sanic
from asyncio import AbstractEventLoop

logger = logging.getLogger()  # get the root logger




def configure_app(
    app : Sanic = None,
    cors: Optional[Union[Text, List[Text], None]] = None,
    auth_token: Optional[Text] = None,
    response_timeout: int = tileai.shared.const.DEFAULT_RESPONSE_TIMEOUT,
    port: int = tileai.shared.const.DEFAULT_SERVER_PORT,
    endpoints: Optional[Text] = None,
    log_file: Optional[Text] = None,
    request_timeout: Optional[int] = None,
) -> Sanic:
    """Run the agent."""
    #aggiunta del log per l'http server
   

    
    app = server.create_app(
        app = app,
        cors_origins=cors,
        auth_token=auth_token,
        response_timeout=response_timeout,
        endpoints=endpoints,
        )
    
    
   
  
    #Aggiungere la capacità di loggare vedi l'approccio di rasa
    
    

    return app


def serve_application(
    app : Sanic = None,
    model_path: Optional[Text] = None,
    endpoints: Optional[Text] = None,
    port: int = tileai.shared.const.DEFAULT_SERVER_PORT,
    cors: Optional[Union[Text, List[Text]]] = None,
    auth_token: Optional[Text] = None,
    response_timeout: int = tileai.shared.const.DEFAULT_RESPONSE_TIMEOUT,
    request_timeout: Optional[int] = None,
    
) -> None:
    
    #print(model_path)
    #app = configure_app(
    #    app,
    #    cors,
    #    auth_token,
    #    response_timeout,
    #    port=port,
    #    endpoints=endpoints,
    #    request_timeout=request_timeout,
    #)

    #app.register_listener(
    #    partial(load_agent_on_start, model_path, endpoints, remote_storage),
    #    "before_server_start",
    #)

    protocol = "http"
    interface = tileai.shared.const.DEFAULT_SERVER_INTERFACE

    print(f"Starting Tileai server on {protocol}://{interface}:{port}")

    # import multiprocessing
    # workers = multiprocessing.cpu_count()
    app.run(
        host=interface,
        port=port,
        debug=True,
        #dev=True,
        auto_reload=False,
        workers=4,
        single_process=False
       
    )


