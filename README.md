# URLResponseTime
Getting url response 

In this project we are fetching url responding time from config.json file and saving response time with Url in another json file.
To run or test
first, create the object of the class, then call the function accordingly.
res = ResponseTime() #creating object

There are two function is their in class:
1 - One is for gettting response time only for one time and save the data into response_time json file.
res.get_response()  #calling function for one time response of all urls

2 - Second is for gettting response time multiple times and save the data into multi_response json file.
res.multiple_response(3) #calling function for multiple time response of all urls
while calling the second function pass the number to get the response that numbers of time.



