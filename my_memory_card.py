#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,QButtonGroup, QPushButton, QLabel)
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3 ):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = list()
questions_list.append(Question('Что будет если ты убьёшь человека?', 'тюрьма','скорее всего ничего','ничего','я стану авторитетом'))
questions_list.append(Question('Что будет смыться в унитаз?','в него невозможно смыться','ничего','будет','невкусно'))
questions_list.append(Question('Почему люди не умеют летать?', 'они не птицы','незнаю','у них нет крыльев','потому что'))
questions_list.append(Question('Какой гриб самый дорогой в мире?','трюфель','мухомор','опята','лисички'))
questions_list.append(Question('Как дела?','отлично','норм','плохо','более менее'))






app = QApplication([])



window = QWidget()
window.setWindowTitle('Memo Card')

btn_ok = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана москва?')


radio = QGroupBox('Варианты ответов')
r_1 = QRadioButton('1147')
r_2 = QRadioButton('1242')
r_3 = QRadioButton('1861')
r_4 = QRadioButton('1943')

Radiogroup = QButtonGroup()
Radiogroup.addButton(r_1)
Radiogroup.addButton(r_2)
Radiogroup.addButton(r_3)
Radiogroup.addButton(r_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()

Layout_ans2.addWidget(r_1)
Layout_ans2.addWidget(r_2)
Layout_ans3.addWidget(r_3)
Layout_ans3.addWidget(r_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

radio.setLayout(Layout_ans1)


ansgrbox = QGroupBox()
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
ansgrbox.setLayout(Layout_res)

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
Layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Layout_line2.addWidget(radio)
Layout_line2.addWidget(ansgrbox)

ansgrbox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)


Lay_card = QVBoxLayout()

Lay_card.addLayout(Layout_line1, stretch=1)
Lay_card.addLayout(Layout_line2, stretch=8)
Lay_card.addStretch(1)
Lay_card.addLayout(layout_line3, stretch=1)
Lay_card.addStretch(1)
Lay_card.setSpacing(5)

def show_result():
    radio.hide()
    ansgrbox.show()
    btn_ok.setText('Следующий вопрос')



def show_question():
    radio.show()
    ansgrbox.hide()
    btn_ok.setText('Ответить')
    Radiogroup.setExclusive(False)
    r_1.setChecked(False)
    r_2.setChecked(False)
    r_3.setChecked(False)
    r_4.setChecked(False)
    Radiogroup.setExclusive(True)
answers = [r_1, r_2, r_3, r_4]



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:',window.score)
        print('Рейтинг: ',(window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ',(window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:',window.score)
    window.cur_question = window.cur_question + 1
  
    
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()






window.setLayout(Lay_card)
window.cur_question = -1
window.total = 0
window.score = 0
btn_ok.clicked.connect(click_OK)
next_question()
window.resize(400,300)
window.show()
app.exec()





