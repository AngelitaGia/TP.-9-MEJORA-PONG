import py5

paddle1_y = paddle2_y = 0
paddle_width = paddle_height = 0
paddle_speed = ball_size = 0
ball_x = ball_y = ball_dx = ball_dy = 0
player1_score = player2_score = 0
game_started = False  


keys = set()

def setup():
    py5.size(800, 400)
    global paddle_width, paddle_height, paddle_speed, ball_size
    global ball_x, ball_y, ball_dx, ball_dy
    global paddle1_y, paddle2_y, player1_score, player2_score
    paddle_width = 20
    paddle_height = 100
    paddle_speed = 7
    ball_size = 20
    reset_game()

def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, game_started
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = 5
    ball_dy = 3
    paddle1_y = py5.height / 2 - paddle_height / 2
    paddle2_y = py5.height / 2 - paddle_height / 2
    game_started = False 
    player1_score = 0
    player2_score = 0

def draw():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, game_started

    py5.background(0)
    

    py5.stroke(255)
    py5.stroke_weight(2)
    py5.line(py5.width / 2, 0, py5.width / 2, py5.height)
    

    py5.rect(30, paddle1_y, paddle_width, paddle_height) 
    py5.rect(py5.width - 30 - paddle_width, paddle2_y, paddle_width, paddle_height)  
    

    if game_started:
        py5.ellipse(ball_x, ball_y, ball_size, ball_size)
    

    py5.text_size(32)
    py5.text_align(py5.CENTER)
    py5.fill(255)
    py5.text(f"{player1_score} - {player2_score}", py5.width / 2, 40)
    

    if not game_started:
        py5.text_size(24)
        py5.text("Presiona SPACE para comenzar", py5.width / 2, py5.height / 2)
    

    py5.text_size(16)
    py5.text_align(py5.LEFT)
    py5.fill(255)
    py5.text("Jugador 1: W (Arriba), S (Abajo)", 10, 30)
    py5.text_align(py5.RIGHT)
    py5.text("Jugador 2: O (Arriba), L (Abajo)", py5.width - 10, 30)
    

    if game_started:
        ball_x += ball_dx
        ball_y += ball_dy
    

    if ball_y <= ball_size / 2 or ball_y >= py5.height - ball_size / 2:
        ball_dy *= -1
        print("Rebote en el borde")
    

    if ball_x - ball_size / 2 <= 30 + paddle_width:
        if paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_dx *= -1
            ball_x = 30 + paddle_width + ball_size / 2
            print("Rebote en la pala 1")
            increase_ball_speed()
    
    if ball_x + ball_size / 2 >= py5.width - 30 - paddle_width:
        if paddle2_y < ball_y < paddle2_y + paddle_height:
            ball_dx *= -1
            ball_x = py5.width - 30 - paddle_width - ball_size / 2
            print("Rebote en la pala 2")
            increase_ball_speed()

    if ball_x < 0:
        player2_score += 1
        reset_ball()

    if ball_x > py5.width:
        player1_score += 1
        reset_ball()


    if 'w' in keys and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if 's' in keys and paddle1_y < py5.height - paddle_height:
        paddle1_y += paddle_speed
    if 'o' in keys and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if 'l' in keys and paddle2_y < py5.height - paddle_height:
        paddle2_y += paddle_speed


    if player1_score >= 10:
        py5.text_size(48)
        py5.text_align(py5.CENTER)
        py5.fill(255)
        py5.text("Jugador 1 Gana!", py5.width / 2, py5.height / 2)
        py5.no_loop()
    elif player2_score >= 10:
        py5.text_size(48)
        py5.text_align(py5.CENTER)
        py5.fill(255)
        py5.text("Jugador 2 Gana!", py5.width / 2, py5.height / 2)
        py5.no_loop()

def key_pressed():
    global keys, game_started
    keys.add(py5.key)
    if py5.key == ' ':
        game_started = True

def key_released():
    global keys
    keys.discard(py5.key)

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = 5 * (-1 if ball_dx > 0 else 1) 
    ball_dy = py5.random(-3, 3)

def increase_ball_speed():
    global ball_dx, ball_dy

    ball_dx *= 1.05
    ball_dy *= 1.05

if __name__ == "__main__":
    py5.run_sketch()