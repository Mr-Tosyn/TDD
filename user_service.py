class UserServices:
    def get_users_from_db(self):
        return [
            {'username':'Ade'},
            {'username':'Bolasss'},
        ]
        
user_services = UserServices()

# users = user_services.get_users_from_db()
# print(users)