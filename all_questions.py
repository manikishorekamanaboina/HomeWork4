# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "No"
    answers["(b)"] = "No"
    answers["(c)"] = "Yes"        
    answers["(d)"] = "Yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "If no single example fulfills more than one rule simultaneously, it's seen as contradictory. Unfortunately, overlaps are likely within this group. For instance, a homeowner who fits rule (1) might also be categorized as a defaulted borrower (DB = Yes) and see their annual income reduced under rule (3). However, the rules aren't completely separate since an individual's traits could activate multiple rules."
    answers["(b) explain"] = "In a scenario where rules are mutually exclusive, it's impossible for a case to fulfill more than one rule simultaneously. However, in this particular instance, there's overlap between rules. For example, a person with a low annual income may also be a homeowner, which are both criteria typically associated with a defaulted borrower. In situations where multiple rules influence actions, they may not be mutually exclusive."
    answers["(c) explain"] = "The final classification result could be influenced by the arrangement of the rules since they aren't separate. In scenarios with multiple rules, the sequence decides which rule takes precedence, impacting the borrower's eventual response. Ensuring fair results is achieved by prioritizing the rules based on their ranking."
    answers["(d) explain"] = "If we overlook situations where the specified rules are disregarded, the rule system remains deficient. Any unaddressed scenarios should be categorized using defined classes. Having a catch-all default class ensures that all cases, even those not fitting into any specific rule set, are accounted for. Without a default class, some individuals will remain uncategorized, which is undesirable in a rule-based system aimed at delivering definitive forecasts."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = ""
    answers["(b)"] = ""
    answers["(c)"] = ""
    answers["(d)"] = ""

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "No"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "When a case cannot satisfy more than one rule simultaneously, rules operate within pairs of cases. Among these, R1 defines a category comprising creatures that breathe air but reproduce differently from birds. Under this framework, any aquatic animal not laying eggs is considered a fish. R3 defines mammals as warm-blooded vertebrates. R4 categorizes live-bearing animals as reptiles, distinct from fish or birds. Each rule necessitates a specific combination of attributes exclusive to itself, ensuring mutual exclusivity among the rules."
    answers["(b) example"] = "The comprehensive ruleset will encompass all conceivable scenarios, ensuring that every data entry is categorized by at least one rule. However, these rules are applicable only to specific cases. Consequently, amphibians and birds are not explicitly addressed, as none of the rules encompass vertebrates that are cold-blooded and give birth (like salamanders), or warm-blooded creatures that give birth but are not aerial (such as penguins)."
    answers["(c) example"] = "Due to their distinctiveness, only one instance is relevant to a specific scenario, rendering the order of application inconsequential. This ensures a deterministic classification process, as each example will be sorted according to one of the rules consistently, regardless of sequence. However, it's crucial to note that reasons not listed may remain uncategorized, posing a separate challenge from fitting reasons into predefined rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The gradient computed at the (k+1)th layer serves as a crucial component in determining the gradient at the kth layer. This process involves applying the chain rule to ensure accuracy in obtaining the necessary value. Ultimately, this calculated gradient forms the foundation for adjusting the weights within each layer of the neural network."
    answers["(b) explain"] = "When transitioning from the kth layer to the k+1th layer in an artificial neural network (ANN), the activation of the k+1th layer is determined by combining the weighted inputs from the nodes in the kth layer, then subjecting the result to a function for activation."
    answers["(c) explain"] = "During the training of artificial neural networks (ANNs), the challenge of vanishing gradients occurs when it becomes difficult for the algorithm to effectively transmit gradient information backward through the layers. This leads to limited or negligible learning in the initial layers. It's important to note that this issue is distinct from the disappearance of training errors being propagated through backpropagation."
    answers["(d) explain"] = "Even if an Artificial Neural Network (ANN) achieves flawless performance, it doesn't guarantee that the gradients of the loss function with respect to the weights at each layer will be precisely zero. Attaining a global optimal minimum for the model necessitates zero gradients. Conversely, achieving perfect classification on the training set might result from a model specifically designed for that data, yet still possess non-zero gradients. This occurs because the loss function typically permits certain margins of error."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.28
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "No"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.4
    answers["(c) P(X_2=1 | +)"] = 0.4
    answers["(c) P(X_2=1 | -)"] = 0.5
    answers["(c) P(X_3=1 | +)"] = 0.16
    answers["(c) P(X_3=1 | -)"] = 0

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The chart depicted in figure KNN (a) clearly illustrates distinct clusters identifiable by their different colors, indicating no overlap between classes. In such instances, opting for a small value of K is deemed preferable, as it ensures instances of each class are tightly grouped in the space. Specifically, when K = 1, there's minimal risk of misjudgment due to the involvement of very few neighbors. In contrast, in scenario A, where class separation is less distinct, choosing K=50 might excessively smooth the decision boundary, making it a secondary choice compared to a smaller K value."
    answers["(b) explain"] = "Figure KNN (b) illustrates a scenario where there is significant overlap between the classes, suggesting that individual instances may not accurately represent the overall distribution due to noise or overlapping classes. In such cases, using a larger value of k in the k-nearest neighbors (KNN) algorithm is preferable. A larger k ensures that the classifier's decision is based on a broader range of neighboring points, thereby reducing the influence of noise. A suitable compromise could be to set k = 5, which balances the need for a smoother decision boundary to avoid sensitivity to outliers (as seen with k = 1) while still being detailed enough to capture the complexities of the true class boundaries better than k = 50, which might oversimplify and lead to underfitting. When the decision boundary becomes ambiguous, k = 50 may fail to capture finer details of the data, unlike k = 5."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.4
    answers["(a) P(A=1|-)"] = 0.8
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.4

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "1. Begin by tallying the occurrences where the class is positive (+) and the attribute is 1. Subtract the count of positive occurrences from the total number of positive instances. Then, divide the counts from the first step by those from the second step to determine \( P(Attribute = 1 | Class = +) \). 2. Repeat the process for the negative class (-). Identify instances where attribute A equals 1 and the class is positive. These instances are visible in the table, where rows 5 and 10 indicate A=1 and are classified as positive. Calculate the total count of positive instances: Rows 2, 5, 6, 9, and 10 are positive, resulting in 5 positive cases. Compute \( P(A=1 | +) \) by considering that among these 5 positive instances, there are 2 occurrences where \( A=1 \), yielding \( P(A=1 | +) = \frac{2}{5} \)."

    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "1. Begin by tallying the occurrences where the class is positive (+) and the attribute is 1. Subtract the count of positive occurrences from the total number of positive instances. Then, divide the counts from the first step by those from the second step to determine \( P(Attribute = 1 | Class = +) \). 2. Repeat the process for the negative class (-). Identify instances where attribute A equals 1 and the class is positive. These instances are visible in the table, where rows 5 and 10 indicate A=1 and are classified as positive. Calculate the total count of positive instances: Rows 2, 5, 6, 9, and 10 are positive, resulting in 5 positive cases. Compute \( P(A=1 | +) \) by considering that among these 5 positive instances, there are 2 occurrences where \( A=1 \), yielding \( P(A=1 | +) = \frac{2}{5} \)."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.3
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "No"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.7
    answers["(d) P(A=1,B=0)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "No"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.8
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "Yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "In reality, A and B are considered independent under certain conditions, specifically when considering the class+. This principle is grounded in the requirement for conditional independence when certain constraints disappear within the framework of the Naive Bayes classifier, based on its conditions. A and B are seen as conditionally independent under the class if the probability of both A and B occurring given the class is equal to the probability of A given the class multiplied by the probability of B given the class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
