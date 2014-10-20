score1 = input ("請輸入您的第一個成績")
score2 = input ("請輸入您的第二個成績")
score3 = input ("請輸入您的第三個成績")
score1 = int(score1)
score2 = int(score2)
score3 = int(score3)
x = [score1 , score2, score3]
x.sort()
Score = x[0] * 0.2 + x[1] * 0.3 + x[2] * 0.5
print (Score)
