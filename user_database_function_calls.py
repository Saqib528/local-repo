import user_database_with_functions

user_database_with_functions.database_tables()

user_database_with_functions.add_record('Saqib','Manzoor',1998,'Male','saqibmanzoor22@gmail.com')

nums=['Asma','Azam',2005,'Female','asma_azam@gmail.com']

user_database_with_functions.add_many_record(nums)

#user_database_with_functions.delete_record()
user_database_with_functions.show_all()

user_database_with_functions.where_clause('Hassan')

