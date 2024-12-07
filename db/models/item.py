from sqlmodel import Field, SQLModel

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    section: str = Field(index=True, default='')
    archive_number: str = Field(index=True)
    amount: str = Field()
    description: str = Field(default='')
    origin: str = Field(default='')
    conservation_status: str = Field(default='')
    obs: str = Field(default='')