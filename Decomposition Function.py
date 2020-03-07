import orange, orngTree, random, orngSVM, orngCN2, orngStat, orngTest, Orange, orngCI
import orange, orngTree, random, orngSVM, orngCN2, orngStat, orngTest, Orange, orngCI
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

def test_rnd_sampling(data, learners, p=0.9, n=30):
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
learners = [sop,tree,bayes,svmrbf,svmpolynomial,svmlinear]#svmrbf, sop, svmpolynomial, adjustedbayes, bayes, svmlinear, adjustedsop, tree, adjustedtree, HINT

# compute accuracies on data

data = orange.ExampleTable("pima-indian-diabetes.tab")
#"lenses.tab" "lenses00.tab" "lenses01.tab" "lenses10.tab" "lenses11.tab"
#"forestfires3.tab" "forestfires3_11.tab"
#"forestfiresnot1101.tab" "forestfires1101.tab"
#"discretefires3.tab" "discretefires3_00.tab" "discretefires3_01.tab" "discretefires3_10.tab" "discretefires3_11.tab"
#"breast-cancer-wisconsin-cont.tab" "breast-cancer-wisconsin-cont00.tab" "breast-cancer-wisconsin-cont01.tab" "breast-cancer-wisconsin-cont.tab10" "breast-cancer-wisconsin-cont11.tab"
#"heart_disease.tab" "heart_disease01.tab" "heart_disease10.tab" "heart_disease11.tab"
#"glass.tab" "glass00.tab" "glass01.tab" "glass10.tab" "glass11.tab"
#"iris.tab" "iris0-.tab" "iris10.tab" "iris11.tab"
#"pima-indian-diabetes.tab" "pima-indian-diabetes00.tab" "pima-indian-diabetes01.tab" "pima-indian-diabetes10.tab" "pima-indian-diabetes0000.tab" "pima-indian-diabetes1010.tab" "pima-indian-diabetes1011.tab"
#"promoters.tab" "promoters1.tab" "promoters2.tab" "promoters3.tab" "promoters4.tab"
#"ionosphere.tab" "ionosphere11.tab"
#"vehicle.tab" "vehicle10.tab" "vehicle11.tab"
#"hepatitis.tab" "hepatitis10.tab"
#"shuttle-landing-control.tab" "shuttle-landing-control00.tab"
#"tic_tac_toe.tab" "tic_xx.tab" "tic_xo.tab" "tic_xb.tab" "tic_ox.tab" "tic_oo.tab" "tic_ob.tab" "tic_bx.tab" "tic_bo.tab" "tic_bb.tab" 
#"soybean-small.tab" "soybean-small01.tab"

acc = test_rnd_sampling(data, learners)
results = orngTest.crossValidation(learners, data, folds=5)

#print "Learner  CA"
#for i in range(len(learners)):
   #print "%-8s %5.3f" % (learners[i].name, orngStat.CA(results)[i])

#output the results
print "Classification accuracies:"
for i in range(len(learners)):
    print learners[i].name, acc[i]