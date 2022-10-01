from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt

def plot_roc_curve(X_train,y_train,X_test,y_test,model):
    fpr, tpr, _ = roc_curve(y_test, model.predict(X_test))
    fpr_train, tpr_train, _ = roc_curve(y_train, model.predict(X_train))

    plt.figure()
    lw = 2
    roc = 2*roc_auc_score(y_test,model.predict(X_test))-1
    roc_train = 2*roc_auc_score(y_train,model.predict(X_train))-1

    plt.plot(
        fpr,
        tpr,
        color="darkorange",
        lw=lw,
        label="ROC curve (area = %0.3f)" % roc,
    )

    plt.plot(
        fpr_train,
        tpr_train,
        #color="darkorange",
        lw=lw,
        label="ROC curve Train (area = %0.3f)" % roc_train,
    )


    plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver operating characteristic example")
    plt.legend(loc="lower right")
    plt.show()

def gini(y_true,y_pred):
    return 2*roc_auc_score(y_true,y_pred)-1