from .models import StudentAnswer, Question


def get_answers(student_answers):
    answers = []
    for student_answer in student_answers:
        question_id = student_answer['question_id']
        question = Question.objects.get(pk=question_id)
        answers.append(dict([('question', question), ('answer', student_answer['answer'])]))
    return answers


def write_student_answer(student_answers, test, profile):
    answer_list = get_answers(student_answers)
    for answer in answer_list:
        correct_answer = ''
        for question_answer in answer['question'].answers.all():
            if question_answer.is_correct:
                correct_answer = question_answer
            StudentAnswer.objects.create(question=answer['question'],
                                         answer=answer['answer'],
                                         correct_answer=correct_answer,
                                         test=test,
                                         profile=profile)


def calculate_result(student_answers):
    result = 0
    answer_list = get_answers(student_answers)
    for answer in answer_list:
        for question_answer in answer['question'].answers.all():
            if question_answer.is_correct and question_answer.text == answer['answer']:
                result += 1
    return result
