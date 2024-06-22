from flask import Flask, request, jsonify

app = Flask(__name__)

faqs = {
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase with a receipt.",
    "How do I track my order?": "You can track your order using the tracking link sent to your email after the purchase.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, and Apple Pay.",
    # Add more FAQs as needed
}

def find_faq(query):
    for question, answer in faqs.items():
        if query.lower() in question.lower():
            return answer
    return "I'm sorry, I don't have an answer for that question."

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    response = find_faq(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)


