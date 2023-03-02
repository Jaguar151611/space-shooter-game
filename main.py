def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 5 5 5 5 5 . . 
                    . . . . . 5 5 5 5 5 f f f 5 . . 
                    f f f f f f f f f f f f f 5 . . 
                    5 5 5 5 5 5 5 5 f f f f f 5 . . 
                    . . . . . . . . . . f f 5 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        -100,
        0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 5 5 5 5 5 . . 
                    . . . . . 5 5 5 5 5 f f f 5 . . 
                    f f f f f f f f f f f f f 5 . . 
                    5 5 5 5 5 5 5 5 f f f f f 5 . . 
                    . . . . . . . . . . f f 5 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.warm_radial, 200)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.camera_shake(4, 500)
    info.change_score_by(-5)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

EnemyShip: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 1 1 1 . . . . . . . . . . . . 
            . 1 1 1 . . . . . . . . . . . . 
            . 1 1 8 8 8 8 8 8 . . . . . . . 
            . 1 1 . . . . . 8 8 . . . . . . 
            . 1 1 9 9 9 9 9 . 9 9 8 8 . . . 
            . 1 1 . . . 9 9 9 9 . . 8 8 . . 
            . 1 1 . . . 9 9 . . . . . 8 8 8 
            . 1 1 . 9 9 . 9 9 9 9 9 9 9 . 8 
            . 1 1 . . . . . . . . . . . 8 8 
            . 1 1 9 9 9 . . . 9 9 8 8 8 8 . 
            . 1 1 1 . 9 9 9 9 9 8 8 . . . . 
            . 1 1 . . 8 8 8 8 8 . . . . . . 
            . 1 1 8 8 8 . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(5)

def on_update_interval():
    global EnemyShip
    EnemyShip = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . e 1 1 . . . . . 
                    . . . . . . . e e 2 1 1 . . . . 
                    . . . . . . e e 9 9 2 1 . . . . 
                    . . . . . e e 9 9 9 1 1 . . . . 
                    . . . . e e 1 1 9 9 1 . . . . . 
                    . . . e 1 1 1 1 9 9 1 1 . . . 3 
                    . e e 9 9 9 9 1 9 9 2 1 . . . . 
                    . e 1 1 1 9 9 9 9 9 2 1 . . . . 
                    . e 9 9 1 1 1 1 1 1 1 1 . . . . 
                    . 1 1 9 1 1 1 1 1 1 1 1 . . . . 
                    . . 1 1 1 1 9 9 1 1 1 1 . . . . 
                    . . . . . 1 1 9 9 1 1 1 . . . . 
                    . . . . . . 1 1 1 9 2 1 . . . . 
                    . . . . . . . . 1 1 1 1 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    EnemyShip.x = scene.screen_width()
    EnemyShip.vx = -20
    EnemyShip.ax = -100
    EnemyShip.y = randint(scene.screen_height(), 0 - 0)
game.on_update_interval(2000, on_update_interval)
