from classes.FreeUser import FreeUser
class PaidUser(FreeUser):
    def __init__(self, first_name, last_name, email, password, membership_plan):
        super().__init__(first_name, last_name, email, password)
        self.membership_plan = membership_plan

