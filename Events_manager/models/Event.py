import typing
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Event:
    """
    Vamos a definir los campos de la tabla eventos

    Se van a definir los metodos, agregar, eliminar, actualizar, filtrar,etc
    """
    title: str
    description: str
    date: str
    time: Optional[datetime] = None
    location: Optional[str] = None
    priority: Optional[int] = None
    id_user: Optional[int] = None

    
    classmethod
    def add_event(self, title:str , 
                  description:str, 
                  date:str, 
                  time:Optional[datetime] = None, 
                  location:Optional[str] = None, 
                  priority:Optional[int] = None, 
                  id_user:Optional[int] = None):
        ...
    
    @classmethod
    def remove_event (self, id_event:int, event_name:str):
        ...
    
    @classmethod
    def update_event(self, id_event:int, event_name:str):
        ...

    @classmethod
    def filter_event_by_name(self, id_event:int, event_name:str):
        ...
    

    @classmethod
    def filter_event_by_date(self, id_event:int, date: datetime):
        ...