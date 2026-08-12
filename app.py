from flask import Flask, request

app = Flask(__name__)

@app.route('/yמות', methods=['GET', 'POST'])
def yמות_bridge():
    # ימות המשיח שולחים את מה שהקישו בפרמטר שנקרא בדרך כלל 'digits' או מה שנגדיר להם
    # אנחנו נשתמש בפרמטר msg כדי שיהיה ברור
    user_input = request.values.get('msg', '')

    # בדיקה שהמשתמש הקיש אכן 4 ספרות
    if len(user_input) == 4 and user_input.isdigit():
        # מחזיר לימות המשיח פקודה להשמעת הודעת המערכת שנבחרה
        # הפורמט הזה גורם לימות להבין שהם צריכים להשמיע את הקובץ m-XXXX
        return f"id_list_message=m-{user_input}"
    
    # אם הקלט לא תקין, אפשר להחזיר הודעת שגיאה או פשוט לבקש להקיש שוב
    return "read=t-הקשתם מספר שגוי. נא הקישו ארבע ספרות של הודעת המערכת.=&digits=4,4,7"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
