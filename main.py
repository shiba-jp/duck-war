def initBogey():
    global bogey, anim2
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . c c c c . . . . 
                    . . . . . . c c d d d d c . . . 
                    . . . . . c c c c c c d c . . . 
                    . . . . c c 4 4 4 4 d c c . . . 
                    . . . c 4 d 4 4 4 4 4 1 c . c c 
                    . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                    . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                    f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                    f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                    f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                    . f 4 4 4 4 1 c 4 f 4 d f f f f 
                    . . f f 4 d 4 4 f f 4 c f c . . 
                    . . . . f f 4 4 4 4 c d b c . . 
                    . . . . . . f f f f d d d c . . 
                    . . . . . . . . . . c c c . . .
        """),
        SpriteKind.enemy)
    anim2 = animation.create_animation(ActionKind.Idle, 100)
def initSpacePlane():
    global spacePlane, anim2
    spacePlane = sprites.create(img("""
            . . . . . . . . . . b 5 b . . . 
                    . . . . . . . . . b 5 b . . . . 
                    . . . . . . . . . b c . . . . . 
                    . . . . . . b b b b b b . . . . 
                    . . . . . b b 5 5 5 5 5 b . . . 
                    . . . . b b 5 d 1 f 5 5 d f . . 
                    . . . . b 5 5 1 f f 5 d 4 c . . 
                    . . . . b 5 5 d f b d d 4 4 . . 
                    b d d d b b d 5 5 5 4 4 4 4 4 b 
                    b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                    b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                    c d d c d 5 5 b 5 5 5 5 5 5 b . 
                    c b d d c c b 5 5 5 5 5 5 5 b . 
                    . c d d d d d d 5 5 5 5 5 d b . 
                    . . c b d d d d d 5 5 5 b b . . 
                    . . . c c c c c c c c b b . . .
        """),
        SpriteKind.player)
    spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    anim2 = animation.create_animation(ActionKind.Idle, 100)
    animation.attach_animation(spacePlane, anim2)
    anim2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . b 5 5 b . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . b b b b b 5 5 5 5 5 5 5 b . . 
                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                . . b d 5 5 b 1 f f 5 4 4 c . . 
                b b d b 5 5 5 d f b 4 4 4 4 b . 
                b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . b b b b b 5 5 5 5 5 5 5 b . . 
                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                . . b d 5 5 b 1 f f 5 4 4 c . . 
                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . . . . b c . . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 5 d f . . 
                . . . . b 5 5 1 f f 5 d 4 c . . 
                . . . . b 5 5 d f b d d 4 4 . . 
                b d d d b b d 5 5 5 4 4 4 4 4 b 
                b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                c d d c d 5 5 b 5 5 5 5 5 5 b . 
                c b d d c c b 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 d 4 c . . 
                . . . . b 5 5 1 f f d d 4 4 4 b 
                . . . . b 5 5 d f b 4 4 4 4 b . 
                . . . b d 5 5 5 5 4 4 4 4 b . . 
                . . b d d 5 5 5 5 5 5 5 5 b . . 
                . b d d d d 5 5 5 5 5 5 5 5 b . 
                b d d d b b b 5 5 5 5 5 5 5 b . 
                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                c b b d 5 d c d 5 5 5 5 5 5 b . 
                . b 5 5 b c d d 5 5 5 5 5 d b . 
                b b c c c d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 d 4 c . . 
                . . . . b 5 5 1 f f d d 4 4 4 b 
                . . . . b 5 5 d f b 4 4 4 4 b . 
                . . . b d 5 5 5 5 4 4 4 4 b . . 
                . b b d d d 5 5 5 5 5 5 5 b . . 
                b d d d b b b 5 5 5 5 5 5 5 b . 
                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                c b b d 5 d c d 5 5 5 5 5 5 b . 
                c b 5 5 b c d d 5 5 5 5 5 5 b . 
                b b c c c d d d 5 5 5 5 5 d b . 
                . . . . c c d d d 5 5 5 b b . . 
                . . . . . . c c c c c b b . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 5 d f . . 
                . . . . b 5 5 1 f f 5 d 4 c . . 
                . . . . b 5 5 d f b d d 4 4 . . 
                . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                b d d d b b d 5 5 4 4 4 4 4 b . 
                b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                c b d c d 5 5 b 5 5 5 5 5 5 b . 
                . c d d c c b d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . . 
                . . . . . . . . . . . . . . . .
    """))
    anim2.add_animation_frame(img("""
        . . . . . . . . . b 5 b . . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 b c 5 5 d 4 c . . 
                . b b b b 5 5 5 b f d d 4 4 4 b 
                . b d 5 b 5 5 b c b 4 4 4 4 b . 
                . . b 5 5 b 5 5 5 4 4 4 4 b . . 
                . . b d 5 5 b 5 5 5 5 5 5 b . . 
                . b d b 5 5 5 d 5 5 5 5 5 5 b . 
                b d d c d 5 5 b 5 5 5 5 5 5 b . 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    animation.set_action(spacePlane, ActionKind.Idle)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """),
        spacePlane,
        200,
        50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

dart: Sprite = None
anim2: animation.Animation = None
bogey: Sprite = None
spacePlane: Sprite = None
class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
initSpacePlane()
info.set_life(3)
controller.move_sprite(spacePlane, 200, 200)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . c c c c . . . . 
                    . . . . . . c c d d d d c . . . 
                    . . . . . c c c c c c d c . . . 
                    . . . . c c 4 4 4 4 d c c . . . 
                    . . . c 4 d 4 4 4 4 4 1 c . c c 
                    . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                    . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                    f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                    f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                    f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                    . f 4 4 4 4 1 c 4 f 4 d f f f f 
                    . . f f 4 d 4 4 f f 4 c f c . . 
                    . . . . f f 4 4 4 4 c d b c . . 
                    . . . . . . f f f f d d d c . . 
                    . . . . . . . . . . c c c . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.left = scene.screen_width()
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
