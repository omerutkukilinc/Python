from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from config import API_KEY

app = Flask(__name__)
client = OpenAI(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/masal-yaz', methods=['POST'])
def masal_yaz():
    data = request.json
    baslik = data.get('baslik')
    karakter = data.get('karakter')
    tur = data.get('tur')

    if not baslik or not karakter or not tur:
        return jsonify({'error': 'Lütfen tüm alanları doldurun.'}), 400

    prompt = f"Bir {tur} masalı yaz. Başlığı: '{baslik}', Ana karakter: '{karakter}'. 10-15 cümle uzunluğunda olsun, çocuklara uygun ve eğlenceli olsun."

    try:
        response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Sen yaratıcı bir masal anlatıcısın."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.9
            )
        masal = response.choices[0].message.content
        return jsonify({'masal': masal})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
