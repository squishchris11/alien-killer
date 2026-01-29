def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        shoot
        """), mySprite, -50, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        shoot
        """), mySprite, 50, 0)
    projectile.start_effect(effects.spray)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(bad_guy, effects.spray, 500)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(bad_guy, effects.spray, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap2)

def on_life_zero():
    sprites.destroy(mySprite)
    game.game_over(False)
    game.set_game_over_message(False, "GAME OVER!")
info.on_life_zero(on_life_zero)

def on_b_released():
    global bad_guy
    bad_guy = sprites.create(assets.image("""
            not little guy
            """),
        SpriteKind.enemy)
    bad_guy.follow(mySprite, 50)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_on_score():
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
    game.set_game_over_message(True, "GAME OVER!")
info.on_score(500, on_on_score)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(bad_guy, effects.spray, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

projectile: Sprite = None
bad_guy: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    little guy
    """), SpriteKind.player)
scene.set_background_image(assets.image("""
    space
    """))
bad_guy.follow(mySprite, 50)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
game.splash("hello commander the aliens have hacked in to our systems and we need you to take them out ")
game.splash("they have it where if you go down more spawn kill 500 and that should get them out of our system. use the a and b buttons to shoot them good luck commander")
info.set_score(0)
info.set_life(3)