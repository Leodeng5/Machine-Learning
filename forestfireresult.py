import orange, orngTree, random, orngSVM, orngCN2, orngStat, orngTest, Orange
import orange, orngTree, random, orngSVM, orngCN2, orngStat, orngTest, Orange
from Orange.classification import bayes, svm
from Orange.evaluation import testing, scoring

random.seed()

def accuracy(test_data, classifiers):
    correct = [0.0]*len(classifiers)
    for ex in test_data:
        for i in range(len(classifiers)):
            if classifiers[i](ex) == ex.getclass():
                correct[i] += 1
    for i in range(len(correct)):
        correct[i] = correct[i] / len(test_data)
    return correct

def test_rnd_sampling(data, learners, p=1, n=30):
    acc = [0.0]*len(learners)
    for i in range(n):
        newselection = orange.MakeRandomIndices2(data, 0.1, randseed=i+10)
        selection = orange.MakeRandomIndices2(data, p, randseed=i)
        train_data = data.select(selection, 0)#this selects selection
        test_data = data.select(newselection, 0)
        classifiers = []
        for l in learners:
            classifiers.append(l(train_data))
        acc1 = accuracy(test_data, classifiers)
        print "%d: %s" % (i+1, acc1)
        for j in range(len(learners)):
            acc[j] += acc1[j]
    for j in range(len(learners)):
        acc[j] = acc[j]/n
    return acc
    
# set up the learners
bayes = Orange.classification.bayes.NaiveLearner(name="bayes")
adjustedbayes = Orange.classification.bayes.NaiveLearner(m=1, adjust_threshold=True, name="adjusted bayes")

tree = orngTree.TreeLearner(name="tree")
adjustedtree = orngTree.TreeLearner(m_pruning=2, max_depth=100, name="adjusted tree")

svmlinear = orngSVM.SVMLearner(svm_type = orngSVM.SVMLearner.Nu_SVC, kernel_type = orange.SVMLearner.Linear, name="svm linear")
svmrbf = orngSVM.SVMLearner(name="svm rbf")
svmpolynomial = orngSVM.SVMLearner(svm_type = orngSVM.SVMLearner.Nu_SVR, kernel_type = orange.SVMLearner.Polynomial, name="svm polynomial")

sop = Orange.classification.rules.CN2Learner(name="sop")
adjustedsop = Orange.classification.rules.CN2Learner(beam_width=50, alpha=1, name="adjusted sop")

learners = [sop,tree,bayes,svmrbf,svmpolynomial,svmlinear]#svmrbf, sop, svmpolynomial, adjustedbayes, bayes, svmlinear, adjustedsop, tree, adjustedtree 

# compute accuracies on data
data = orange.ExampleTable("forest-fire-oregon.tab")
results = orngTest.crossValidation(learners, data, folds=5)

#print "Learner  CA"
#for i in range(len(learners)):
   #print "%-8s %5.3f" % (learners[i].name, orngStat.CA(results)[i])

#output the results
print "Classification accuracies:"
for i in range(len(learners)):
    print learners[i].name, acc[i]