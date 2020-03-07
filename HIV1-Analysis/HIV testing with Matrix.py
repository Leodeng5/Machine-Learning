import orange, orngTree, random, orngSVM, orngCI, orngCN2, orngStat, orngTest, Orange, datetime
from Orange.classification import bayes, svm
from Orange.evaluation import testing, scoring

random.seed()

def accuracy(test_data, classifiers):
    correct = [0.0]*len(classifiers)
    tpositive = [0.0]*len(classifiers)
    tnegative = [0.0]*len(classifiers)
    fpositive = [0.0]*len(classifiers)
    fnegative = [0.0]*len(classifiers)
    for ex in test_data:
        for i in range(len(classifiers)):
            if classifiers[i](ex) == ex.getclass():
                correct[i] += 1
                if ex.getclass()=="-1":
                    tnegative[i] += 1
                elif ex.getclass()=="1":
                    tpositive[i] += 1
            else:
                if ex.getclass()=="1":
                    fpositive[i] += 1
                elif ex.getclass()=="-1":
                    fnegative[i] += 1
    #accuracy
    for i in range(len(correct)):
        correct[i] = correct[i] / len(test_data)
    #sensitivity
    #for i in range(len(tpositive)):
    #    tpositive[i] = tpositive[i] / (tpositive[i] + fnegative[i])
    #specificity
    #for i in range(len(tnegative)):
    #    tnegative[i] = tnegative[i] / (tnegative[i] + fpositive[i])
    for i in range(len(fpositive)):
        tpositive[i] = tpositive[i] / len(test_data)
    for i in range(len(fpositive)):
        tnegative[i] = tnegative[i] / len(test_data)
    #false positives
    for i in range(len(fpositive)):
        fpositive[i] = fpositive[i] / len(test_data)
    #false negatives
    for i in range(len(fnegative)):
        fnegative[i] = fnegative[i] / len(test_data)

    return (correct, tpositive, tnegative, fpositive, fnegative)

def test_rnd_sampling(data, learners, p=0.9, n=30, x=1):
    acc = [0.0]*len(learners)
    #sens = [0.0]*len(learners)
    #spec = [0.0]*len(learners)
    tpos = [0.0]*len(learners)
    tneg = [0.0]*len(learners)
    fpos = [0.0]*len(learners)
    fneg = [0.0]*len(learners)
    for i in range(n):
        newselection = orange.MakeRandomIndices2(data, 0.1, randseed=(datetime.datetime.now().time().microsecond + i))
        selection = orange.MakeRandomIndices2(data, p, randseed=(datetime.datetime.now().time().microsecond-i))
        train_data = data.select(selection, 0)#this selects selection
        test_data = data.select(newselection, 0)
        classifiers = []
        for l in learners:
            classifiers.append(l(train_data))
        acc1 = accuracy(test_data, classifiers)[0]
        #sens1 = accuracy(test_data, classifiers)[1]
        #spec1 = accuracy(test_data, classifiers)[2]
        tpos1 = accuracy(test_data, classifiers)[1]
        tneg1 = accuracy(test_data, classifiers)[2]
        fpos1 = accuracy(test_data, classifiers)[3]
        fneg1 = accuracy(test_data, classifiers)[4]
        #print "%d: %s" % (i+1, acc1)
        for j in range(len(learners)):
            acc[j] += acc1[j]
        #for j in range(len(learners)):
         #   sens[j] += sens1[j]
        #for j in range(len(learners)):
         #   spec[j] += spec1[j]
        for j in range(len(learners)):
            tpos[j] += tpos1[j]
        for j in range(len(learners)):
            tneg[j] += tneg1[j]
        for j in range(len(learners)):
            fpos[j] += fpos1[j]
        for j in range(len(learners)):
            fneg[j] += fneg1[j]
    for j in range(len(learners)):
        acc[j] = acc[j]/n
    #for j in range(len(learners)):
     #   sens[j] = sens[j]/n
    #for j in range(len(learners)):
     #   spec[j] = spec[j]/n
    for j in range(len(learners)):
        tpos[j] = tpos[j]/n
    for j in range(len(learners)):
        tneg[j] = tneg[j]/n
    for j in range(len(learners)):
        fpos[j] = fpos[j]/n
    for j in range(len(learners)):
        fneg[j] = fneg[j]/n
    return (acc, tpos, tneg, fpos, fneg)
    
# set up the learners
bayes = Orange.classification.bayes.NaiveLearner(name="bayes")
adjustedbayes = Orange.classification.bayes.NaiveLearner(m=1, adjust_threshold=True, name="adjusted bayes")

tree = orngTree.TreeLearner(name="tree")
adjustedtree = orngTree.TreeLearner(m_pruning=2, max_depth=100, name="adjusted tree")

svmlinear = orngSVM.SVMLearner(svm_type = orngSVM.SVMLearner.Nu_SVC, kernel_type = orange.SVMLearner.Linear, name="svm linear")
svmrbf = orngSVM.SVMLearner(name="svm rbf")
svmpolynomial = orngSVM.SVMLearner(svm_type = orngSVM.SVMLearner.Nu_SVR, kernel_type = orange.SVMLearner.Polynomial, name="svm polynomial")

sop = Orange.classification.rules.CN2Learner(beam_width=100, name="sop")
adjustedsop = Orange.classification.rules.CN2Learner(beam_width=50, alpha=1, name="adjusted sop")

learners = [sop, tree, bayes, svmlinear, svmrbf, svmpolynomial]

# compute accuracies on data
data = orange.ExampleTable("1625-hiv-continuous-input.tab") #forest-fire-oregon.tab #breast-cancer-wisconsin.tab #forestfires0.tab
b = test_rnd_sampling(data, learners)
acc = b[0]
#sens = b[1]
#spec = b[2]
tpos = b[1]
tneg = b[2]
fpos = b[3]
fneg = b[4]

#print "Learner  CA"
#for i in range(len(learners)):
   #print "%-8s %5.3f" % (learners[i].name, orngStat.CA(results)[i])

#output the results
print "Classification results:  (Accuracy, True Positives, True Negatives, False Positives, False Negatives)"
for i in range(len(learners)):
    print learners[i].name, acc[i], tpos[i], tneg[i], fpos[i], fneg[i]
