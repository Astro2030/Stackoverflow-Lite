import datetime
from stack.app.v1.models.questions import questions as question
from stack.app.v1.models.data1 import answer_list,question_list
from flask import Flask,Blueprint,request,abort,make_response,jsonify 

BP = Blueprint('views', __name__,url_prefix='/app/v1/views')
JSON_ERR_MSG = 'Malformed Request data. Please use JSON data'
app = Flask(__name__)

@BP.errorhandler(404)
def item_not_found(e):
    """
    Custom response to 404 errors.
    """
    return make_response(jsonify({'Failed' : 'Item not found'}), 404)


@BP.errorhandler(400)
def bad_request(e):
    """
    Custom response to 400 errors.
    """
    return make_response(jsonify({'Failed': 'bad request'}), 400)

@BP.route("/questions/", methods=["GET","POST"])
def get_all_questions():
    """
    View all questions.
    """
    if question:
        for quiz in question.get_questions():
            #get number of answers
            quiz["answers"]=len(question.get_answers(quiz["question_id"]))
    return jsonify({"questions": question.get_questions()}),200
    abort(404)



@BP.route('/home/<int:question_id>', methods=['GET','POST'])
def get_a_specific_question(question_id):
    """
    Get a specific question.
    """
    if request.method == 'GET':
        question_list = question.get_questions()
        my_question=[my_question for my_question in question_list if my_question['question_id'] == question_id]
        if my_question:
            question_answers=question.get_answers(my_question[0]['question_id'])
            my_question[0]["answers"]=question_answers
        return jsonify({"question": my_question}),200
        abort(404)



if __name__ == "__main__":
    app.run(debug=True)
    
    

