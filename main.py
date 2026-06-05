import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Negro. 💕</title>
    <style>
        body {
            background-color: #fce4ec;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .card {
            background-color: #fff5f7;
            border: 2px solid #ffb3c6;
            border-radius: 20px;
            padding: 40px 20px;
            width: 85%;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
            position: relative;
        }
        .ribbon {
            font-size: 35px;
            margin-bottom: 10px;
            color: #ff4d6d;
        }
        .title {
            color: #ff4d6d;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 25px;
        }
        .verse-container {
            border: 1px dashed #ffb3c6;
            border-radius: 12px;
            padding: 30px 15px;
            margin-bottom: 25px;
            background-color: #fffdfd;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .verse {
            color: #c9184a;
            font-size: 18px;
            font-weight: bold;
            line-height: 1.5;
            margin: 0;
        }
        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            min-height: 100px;
        }
        .btn {
            color: white;
            border: none;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, background-color 0.2s;
            display: block;
        }
        .btn-yes {
            background-color: #2a9d8f;
            padding: 12px 35px;
            font-size: 16px;
        }
        .btn-yes:hover {
            background-color: #3aa89b;
        }
        .btn-no {
            background-color: #9b2226;
            padding: 12px 25px;
            font-size: 14px;
        }
        .btn-no:hover {
            background-color: #ae2012;
        }
        
        #finalSection {
            text-align: center;
            padding: 20px;
            position: absolute;
            top: 40px; 
            width: 100%;
            box-sizing: border-box;
        }
        .final-text {
            color: #ff4d6d;
            font-size: 14px; 
            font-weight: bold;
            margin-bottom: 30px;
            padding: 0 10px;
        }
        .gif-container img {
            max-width: 150px; 
            height: auto;
            border-radius: 10px;
        }
    </style>
</head>
<body>

    <div class="card" id="mainCard">
        <div class="ribbon" id="cardIcon">🎀</div>
        <div class="title" id="cardTitle">💕 Para mi flaco 💕</div>
        
        <div id="gameSection">
            <div class="verse-container">
                <p class="verse" id="questionText">¿Has estado bien?</p>
            </div>
            
            <div class="btn-container">
                <button class="btn btn-yes" id="btnYes" onclick="nextQuestion()">Sí 💕</button>
                <button class="btn btn-no" id="btnNo" onclick="handleNoClick()">No 🥺</button>
            </div>
        </div>
    </div>

    <div id="finalSection" style="display: none;">
        <p class="final-text">¡Gracias por leer! Ya puedes cerrar esta pestañita, Te Amo Mi Negro. 💕</p>
        <div class="gif-container">
            <img src="https://i.postimg.cc/0jXvC61g/hello-kitty-love.gif" alt="Hello Kitty Love">
        </div>
    </div>

    <script>
        // CORREGIDO AQUÍ: El primer elemento de la lista para que coincida perfectamente al avanzar/retroceder
        const preguntas = [
            "¿Has estado bien?",
            "¿Comes bien?",
            "¿Me extrañas..?",
            "¿Piensas en mí..?",
            "¿Pronto volveremos a hablar?",
            "¿Lo volvemos a intentar una vez más..?"
        ];

        let currentStep = 0;
        let yesScale = 1.0;
        let noScale = 1.0;

        function handleNoClick() {
            if (currentStep === preguntas.length - 1) {
                yesScale += 0.25;
                noScale -= 0.15;

                const btnYes = document.getElementById('btnYes');
                const btnNo = document.getElementById('btnNo');

                btnYes.style.transform = "scale(" + yesScale + ")";
                btnNo.style.transform = "scale(" + noScale + ")";

                if (noScale <= 0.25) {
                    btnNo.style.display = 'none';
                }
            } else {
                nextQuestion();
            }
        }

        function nextQuestion() {
            currentStep++;

            yesScale = 1.0;
            noScale = 1.0;
            const btnYes = document.getElementById('btnYes');
            const btnNo = document.getElementById('btnNo');
            
            if (btnYes && btnNo) {
                btnYes.style.transform = 'scale(1)';
                btnNo.style.transform = 'scale(1)';
                btnNo.style.display = 'block';
            }

            if (currentStep < preguntas.length) {
                document.getElementById('questionText').innerText = preguntas[currentStep];
            } else {
                document.getElementById('mainCard').style.display = 'none';
                document.body.style.backgroundColor = '#ffffff'; 
                document.getElementById('finalSection').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
