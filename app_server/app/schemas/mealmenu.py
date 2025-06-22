from pydantic import BaseModel
from typing import Optional

class MealMenu(BaseModel):
    date: str
    timing: str
    ## Optional:空白でもOK(null許容)
    main_food: Optional[str]
    main_dish: Optional[str]
    side_dish: Optional[str]
    soup: Optional[str]
    others: Optional[str]