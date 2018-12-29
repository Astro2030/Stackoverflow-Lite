from stack.app.v1.models.data1 import question_list
class questions():
    def __init__(self):
        self.question_list = [
                                {  
                                    'question_id':1,
                                    'description' : 'When was the last time you kissed someone?',
                                    'timeposted' : '2300hrs',
                                    'author' : 'geofrey',
                                },
                                {   
                                    'question_id':2,
                                    'description':'When was the last time you kissed someone?',
                                    'timeposted':'2300hrs',
                                    'author':'Caleb',
                                },

                                {   
                                    'question_id':3,
                                    'description':'When was the last time you kissed someone?',
                                    'timeposted':'2300hrs',
                                    'author':'Vincent',
                                },

                                {   
                                    'question_id':4,
                                    'description':'When was the last time you kissed someone?',
                                    'timeposted':'2300hrs',
                                    'author':'geofrey',
                                }
                    ]
        self.answer_list = [
            {
                'author':'James',
                'description':'It was the day I went shopping.',
                'timeposted':'1200hrs',
                'question_id': 1,
                'answer_id': 1
            },
            {
                'author':'James',
                'description':'It was the day I went shopping.',
                'timeposted':'1200hrs',
                'question_id': 3,
                'answer_id': 2
            }
        ]

    def get_questions(self):
        return self.question_list

    def get_answers(self,question_id):
        return self.answer_list


    def delete_question(self, question_id):
        """delete question by question_id"""
        return self.question_list.pop(question_id)['question_id']

questions = questions()

