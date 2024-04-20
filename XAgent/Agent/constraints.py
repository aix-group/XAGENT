welcome_msg = "Welcome. I am a conversational agent and can explain decisions made by machine learning models. Currently, the default dataset is german-credit. Would you like to go on with this dataset? Please type 'yes' to continue, otherwise, type one of the supported dataset in this list [Adult, Iris, Titanic]?"
welcome_msg_test = "Hello, I am XAgent, an AI model designed to provide explanations for predictions made by an AI model trained on the **German Credit dataset**. \
My role is to help you understand how the model arrived at a specific prediction and provide insights into the factors that influenced that prediction. **Assume you are a customer who wants a loan from a bank and provide your information**. An AI model will then predict whether you are able to **get a loan or not**. After that, you can ask questions about the predictions. Type anything when we shall start."


dataset_error_msg = "I only support adult, iris, titanic and german-credit dataset, please type a correct name"
wait_msg = "Wait a min, I need to learn it."
list_feature_request_msgs = ["How about your ", "What is your ", "Give me your "]
record_info_msg = "I recorded the information {}, "
predict_msg = "you have {}."
question_msg = "You can ask questions about a machine learning model, such as: \n Why was the prediction made? \n Why was Y not predicted? \n What should change in order to make prediction Y? \nPlease type your question."
select_msg = "Sorry, I am not exactly sure whether I understood your question correctly. \n Did you mean any of the below? Please select a number or type a new question: \n "
rephrase_question_msg = "Sorry, I don't understand your question. Please rephrase your question."
no_cf_msg = "Sorry, I couldn't find the way to modify {} to change the label."
cant_answer_msg = "I am not capable of answering your question. Questions of this type can currently not be answered by an explainable AI method."
repeat_cat_features = "The input value is not valid, please choose in one of the following values:{}"
repeat_num_features = "Please input numbers only."
request_number_msg = "It is not a number or not an appropriate number. Please choose another number."
request_more_msg = "Here are some example questions. Please select a number or type a new question: \n "
ans_shap_question_single_feature = "Here is the impact of this feature. "
l_shap_question_ids = [3, 5, 6, 8, 67, 69]
l_shap_question_feature = [3, 5, 69]
l_shap_question_single_feature = [6]
l_dice_question_ids = [11, 12, 14, 71]
l_dice_question_relation_ids = [71]
l_anchor_question_ids = [20, 15, 13]
l_feature_questions_ids = [6, 12]
l_new_predict_question_ids = [64]
l_terminology_question_ids=[43]
l_others = [1, 2, 4, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 68, 70]
l_questions = ["How about your ", "What is your ", "Give me your "]
l_support_questions_ids = l_shap_question_ids+l_dice_question_ids+l_anchor_question_ids
map_job = ["unskilled and non - resident", "unskilled and resident", "skilled", "highly skilled"]