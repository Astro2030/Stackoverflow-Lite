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

    elif request.method == 'POST':
        """handle POST /app/v1/views/ endpoint"""
        answer_list = question.get_answers(question_id)
        data = request.get_json(force=True, silent=True)
        if not data:
            raise MalformedRequest(JSON_ERR_MSG)
        try:
            answer_id=len(answer_list)+1
            author = data['author']
            timeposted = datetime.datetime.now()
            description = data['description']

        except KeyError as e:
            raise MalformedRequest(f'Missing {e.args} field(s)', 400)
        new_answer = {
            'question_id': question_id,
            'author' : author,
            'timeposted' : datetime.datetime.now(),
            'description' : description,
            'answer_id': answer_id
        }
        answer_list.append(new_answer)
        return make_response(jsonify({
            'status': "Ok",
            'message': "posted successfully",
            'answer':new_answer}),201)
    

@BP.route('/post_question/', methods=['POST'])
def add_question():
    data = request.get_json(force=True, silent=True)
    if not data:
        raise MalformedRequest(JSON_ERR_MSG)
    try:
        question_id=len(answer_list)+1
        author = data['author']
        timeposted = datetime.datetime.now()
        description = data['description']

    except KeyError as e:
        raise MalformedRequest(f'Missing {e.args} field(s)', 400)
    quiz = {
        'question_id': question_id,
        'author' : author,
        'timeposted' : datetime.datetime.now(),
        'description' : description,
    }
    question_list.append(quiz)
    return make_response(jsonify({
        'status': "Ok",
        'message': "posted successfully",
        'question_list':question_list}),201)


if __name__ == "__main__":
    app.run(debug=True)
    
    

