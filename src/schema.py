from pydantic import BaseModel


class ConfigurationSchema(BaseModel):
    firstName: str
    secondName: str
    ageInYears: int
    address: str
    creditScore: float
