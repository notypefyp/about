<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сосал?</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #111;
            color: white;
            text-align: left;
        }

        h1 {
            font-size: 6rem;
            margin-bottom: 40px;
        }

        .button-container {
            display: flex;
            gap: 50px;
        }

        .btn {
            font-family: 'Montserrat', sans-serif;
            color: white;
            font-size: 2.5rem;
            padding: 20px 60px;
            border-radius: 15px;
            cursor: pointer;
            transition: 0.3s;
            border: 4px solid rgba(255, 255, 255, 0.10);
        }

        .btn-glow {
            background: linear-gradient(45deg, #FFD700, #FF8C00, #FF4500);
            border: none;
            color: black;
            font-weight: bold;
            animation: glow 1.5s infinite alternate;
        }

        @keyframes glow {
            from {
                box-shadow: 0 0 15px rgba(255, 200, 0, 0.8);
            }
            to {
                box-shadow: 0 0 30px rgba(255, 140, 0, 1);
            }
        }

        .btn-outline {
            background: transparent;
            color: white;
            border: 4px solid rgba(255, 255, 255, 0.10);
        }

        .btn:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>

    <h1>Сосал?</h1>
    
    <div class="button-container">
        <button class="btn btn-glow">Да</button>
        <button class="btn btn-outline">Да</button>
    </div>

</body>
</html>
