if __name__ == '__main__':
    records = []
    scoreList = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scoreList.add(score)
        
    newScoreList = sorted(list(scoreList))
    Scores2nd = newScoreList[1]
    
    newRecordsList = [name for name, s in records if s == Scores2nd]
    newRecordsList.sort()
    
    for name in newRecordsList:
        print(name)
