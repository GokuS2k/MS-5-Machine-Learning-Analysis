import numpy as np
import matplotlib.pyplot as plt
import wf_ml_prediction


def survey():
    save_plots = r"D:/ASU_Codes/python/ChatBot/Visuals"
    list_sur = []
    list_rub = ["Satisfaction", "Efficiency", "Accuracy", "Response Time", "Answered all?"]
    print("Please do rate SPARKY's customer service (from 1-5)")
    list_sur.append(int(float(input("How satisfied are you with our response today?"))))
    list_sur.append(int(float(input("How efficient was this chatbot service?"))))
    list_sur.append(int(float(input("Was the response accurate enough?"))))
    list_sur.append(int(float(input("How good was the response time?"))))
    list_sur.append(int(float(input("How strongly do you agree with the response answers?"))))
    t = wf_ml_prediction.predict_rec(list_sur[0:2], list_sur[2:4])
    print("-------------------------------------------------------------------------------------")
    print("Below part ment for Developers only")
    print("Prediction score (out of 5). Chances of recommending this chatbot to other companies: "+str(t))

    sug = input("Additional feedback (optional)*")
    print(list_sur)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(list_rub, list_sur, color='maroon', width=0.4)
    plt.xlabel("Customer Review")
    plt.ylabel("Ratings")
    plt.title("Rating of the present customer")
    plt.show()
    fig.savefig(save_plots + '/Customer_Response')
    plt.close()

# survey()
