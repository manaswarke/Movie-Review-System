#wapp to store movie review

from pymongo import *

con = None
try:
      
       con = MongoClient("localhost", 27017)
       
       db = con["movie_review_3aug26"]
       coll = db["movie_review"]
       name = input("enter movie name ")
       review = input("Enter movie review ")
       doc = {"name":name, "review":review}
       coll.insert_one(doc)
       print("thank u for the review")
except Exception as e:
       print("issue ", e)
finally:
       if con != None:
              con.close()