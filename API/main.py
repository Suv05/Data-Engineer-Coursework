from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)

# for user in some_list:
#     print (user.get_full_name()," ",user.get_email())
    
def get_users():
    users=[]
    
    for user in some_list:
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
        
    return pd.DataFrame(users)
    
df1=get_users()
print(df1)

df1.to_csv("./API/users.csv")