from .models import StudentAnswer, Question, Answer, TestResult


def get_answers(student_answers):
    answers = []
    for student_answer in student_answers:
        question_id = student_answer['question_id']
        question = Question.objects.get(pk=question_id)
        answers.append(dict([('question', question), ('answer', student_answer['answer'])]))
    return answers


def write_student_answer(student_answers, test_result):
    answer_list = get_answers(student_answers)
    for answer in answer_list:
        correct_answer = Answer.objects.get(is_correct=True, question=answer['question'])
        is_correct = False
        if answer['answer'] == correct_answer.text:
            is_correct = True
        StudentAnswer.objects.create(question=answer['question'],
                                     answer=answer['answer'],
                                     correct_answer=correct_answer,
                                     test_result=test_result,
                                     is_correct=is_correct
                                     )


def calculate_result(student_answers):
    result = 0
    answer_list = get_answers(student_answers)
    for answer in answer_list:
        for question_answer in answer['question'].answers.all():
            if question_answer.is_correct and question_answer.text == answer['answer']:
                result += 1
    return result


def check_attempts(profile, test):
    test_results = TestResult.objects.filter(profile=profile, test=test)
    if test.attempts_number is not None:
        if len(test_results) < test.attempts_number:
            return True
        elif len(test_results) >= test.attempts_number:
            return False
    else:
        return True
