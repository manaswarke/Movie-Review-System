#wapp to view movie reviews

from pymongo import *

con = None
try:
       con = MongoClient("localhost", 27017)
       db = con["movie_review_3aug26"]
       coll = db["movie_review"]
       data = coll.find() 
       for d in data:
                  print(d)
except Exception as e:
              print("issue ", e)
finally:
              if con != None:
                      con.close()