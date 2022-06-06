from sqlalchemy import create_engine,MetaData
from urllib.parse import quote 
engine = create_engine('mysql+pymysql://root:%s@localhost:3306/test' % quote('shraddha@123'))
meta =  MetaData()
conn = engine.connect()
