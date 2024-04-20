from sqlalchemy import Column, Integer, String

class TierList(Base):
    __tablename__ = "tier_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String, index=True)
    # ...