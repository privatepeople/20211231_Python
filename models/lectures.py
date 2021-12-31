class Lectures():
    def __init__(self, info_dict):
        self.id = info_dict['id']
        self.name = info_dict['name']
        self.max_count = info_dict['max_count']
        self.campus = info_dict['campus']
    
    def lecture_inquiry(self):
        
        print(f"{self.id}.{self.name} (캠퍼스 : {self.campus})")
