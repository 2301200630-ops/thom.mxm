import os
from Flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Negro. 💕</title>
    <style>
        Body {
            Background-color: #fce4ec;
            Font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            Display: flex;
            Justify-content: center;
            Align-items: center;
            Height: 100vh;
            Margin: 0;
            Overflow: hidden;
        }
        .card {
            Background-color: #fff5f7;
            Border: 2px solid #ffb3c6;
            Border-radius: 20px;
            Padding: 40px 20px;
            Width: 85%;
            Max-width: 500px;
            Text-align: center;
            Box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
            Position: relative;
        }
        .ribbon {
            Font-size: 35px;
            Margin-bottom: 10px;
            Color: #ff4d6d;
        }
        .title {
            Color: #ff4d6d;
            Font-size: 20px;
            Font-weight: bold;
            Margin-bottom: 25px;
        }
        .verse-container {
            Border: 1px dashed #ffb3c6;
            Border-radius: 12px;
            Padding: 30px 15px;
            Margin-bottom: 25px;
            Background-color: #fffdfd;
            Min-height: 80px;
            Display: flex;
            Align-items: center;
            Justify-content: center;
        }
        .verse {
            Color: #c9184a;
            Font-size: 18px;
            Font-weight: bold;
            Line-height: 1.5;
            Margin: 0;
        }
        .btn-container {
            Display: flex;
            Justify-content: center;
            Align-items: center;
            Gap: 15px;
            Min-height: 100px;
        }
        .btn {
            Color: white;
            Border: none;
            Border-radius: 25px;
            Font-weight: bold;
            Cursor: pointer;
            Box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            Transition: transform 0.2s ease, background-color 0.2s;
            Display: inline-block !important;
        }
        .btn-yes {
            Background-color: #2a9d8f;
            Padding: 12px 35px;
            Font-size: 16px;
        }
        .btn-yes:hover {
            Background-color: #3aa89b;
        }
        .btn-no {
            Background-color: #9b2226;
            Padding: 12px 25px;
            Font-size: 14px;
        }
        .btn-no:hover {
            Background-color: #ae2012;
        }
        
        #finalSection {
            Text-align: center;
            Padding: 20px;
            Position: absolute;
            Top: 40px; 
            Width: 100%;
            Box-sizing: border-box;
        }
        .final-text {
            Color: #ff4d6d;
            Font-size: 14px; 
            Font-weight: bold;
            Margin-bottom: 30px;
            Padding: 0 10px;
        }
        .gif-container img {
            Max-width: 150px; 
            Height: auto;
            Border-radius: 10px;
        }
    </style>
</head>
<body>

    <div class="card" id="mainCard">
        <div class="ribbon" id="cardIcon">💘</div>
        <div class="title" id="cardTitle">✨ Para mi flaco ✨</div>
        
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
            <img src="https://pub-c0490b4d4b3149528d9d4949bd51a140.r2.dev/kitty-love.gif" alt="Hello Kitty Love">
        </div>
    </div>

    <script>
        Const preguntas = [
            "¿Has estado bien?",
            "¿comes bien?,",
            "¿Me extrañas..?,",
            "¿Piensas en mí..?,",
            "¿Pronto volveremos a hablar..?,",
            "¿Lo volveremos a intentar una última vez..? Mi Flaco... <'3"
        ];

        Let currentStep = 0;
        Let yesScale = 1.0;
        Let noScale = 1.0;

        Function handleNoClick() {
            Const btnYes = document.getElementById('btnYes');
            Const btnNo = document.getElementById('btnNo');

            If (currentStep === preguntas.length - 1) {
                YesScale += 0.25;
                NoScale -= 0.15;

                If (btnYes && btnNo) {
                    BtnYes.style.transform = "scale(" + yesScale + ")";
                    BtnNo.style.transform = "scale(" + noScale + ")";

                    If (noScale <= 0.25) {
                        BtnNo.style.display = 'none';
                    }
                }
            } else {
                NextQuestion();
            }
        }

        Function nextQuestion() {
            CurrentStep++;

            YesScale = 1.0;
            NoScale = 1.0;
            Const btnYes = document.getElementById('btnYes');
            Const btnNo = document.getElementById('btnNo');
            
            If (btnYes && btnNo) {
                BtnYes.style.transform = 'scale(1)';
                BtnNo.style.transform = 'scale(1)';
                BtnNo.style.display = 'inline-block';
            }

            If (currentStep < preguntas.length) {
                Document.getElementById('questionText').innerText = preguntas[currentStep];
            } else {
                Document.getElementById('mainCard').style.display = 'none';
                Document.body.style.backgroundColor = '#ffffff'; 
                Document.getElementById('finalSection').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    Return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    App.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
