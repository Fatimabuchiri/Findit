import pickle

# Open the .pkl file in binary read mode
with open('Findit/data/database.pkl', 'rb') as file:
   
   data = pickle.load(file)

print(data)

 
 #path to your database.pkl file
#database_path = 'Findit/data/database.pkl'

# Empty dictionary
#empty_database = {}

# Open the file in write-binary mode and overwrite with the empty dictionary
#with open(database_path, 'wb') as f:
    #pickle.dump(empty_database, f)

#print("Database has been emptied.")


