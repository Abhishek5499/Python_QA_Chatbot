from knowledge_base import knowledge_base

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# 1. GET QUESTIONS FROM KNOWLEDGE BASE
# ==========================================

questions = []

for item in knowledge_base:
    questions.append(item["question"])


# ==========================================
# 2. CREATE TF-IDF VECTORIZER
# ==========================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)


# Convert questions into numerical vectors
question_vectors = vectorizer.fit_transform(questions)


# ==========================================
# 3. CHATBOT FUNCTION
# ==========================================

def get_answer(user_question):

    # Convert user's question into TF-IDF vector
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity
    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    # Find the question with highest similarity
    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]


    # ======================================
    # 4. CONFIDENCE THRESHOLD
    # ======================================

    if best_score < 0.20:

        return (
            "Sorry, I don't understand that question. "
            "Please ask a Python-related question."
        )


    # Get corresponding answer
    answer = knowledge_base[best_match_index]["answer"]

    return answer


# ==========================================
# 5. TEST CHATBOT
# ==========================================

if __name__ == "__main__":

    print("======================================")
    print("      PERSONAL PYTHON CHATBOT")
    print("======================================")

    print("Type 'exit' to stop the chatbot.\n")


    while True:

        user_question = input("You: ")

        if user_question.lower() == "exit":

            print("Chatbot: Goodbye!")

            break


        answer = get_answer(user_question)

        print("Chatbot:", answer)