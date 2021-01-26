from datetime import datetime
from typing import Optional, List

from app.db.utils import StatisticTypeEnum
from pydantic import BaseModel


class StatisticSchema(BaseModel):
    device_id: str
    datetime: datetime
    statistic_type: StatisticTypeEnum
    people_with_mask: int
    people_without_mask: int
    people_total: int

    class Config:
        orm_mode = True


class DeviceSchema(BaseModel):
    id: str
    description: Optional[str] = None
    file_server_address: Optional[str] = None
    statistics: List[StatisticSchema] = []

    class Config:
        orm_mode = True


class VideoFileSchema(BaseModel):
    device_id: str
    video_name: str

    class Config:
        orm_mode = True