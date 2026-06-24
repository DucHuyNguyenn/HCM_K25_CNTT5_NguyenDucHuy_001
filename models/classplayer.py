class ClassPlayer:
    def __init__(self,id,name,speed_score,technique_score,goal_score):
        self.id = id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score  = goal_score
        self.averange_score = self.calculate_averange()
        self.performance_type = self.classify_performance()

    def calculate_averange(self):
        return self.speed_score*0.3 + self.technique_score*0.4 + self.goal_score*0.3
    def classify_performance(self):
        if self.averange_score < 5:
            return "Dự bị yếu"
        if self.averange_score < 6.5:
            return "Trung bình"
        if self.averange_score < 8.0:
            return "Tốt"
        if self.averange_score > 8.0:
            return "Ngôi sao"