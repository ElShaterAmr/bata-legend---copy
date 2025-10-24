@namespace
class SpriteKind:
    mity = SpriteKind.create()
    duck = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . b . . . . . . . 
                        . . . . . . . b d b . . . . . . 
                        . . . . . . . c d c . . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . . . c d 5 d c . . . . . 
                        . . . b c c d 5 5 5 d c c b . . 
                        . . b d d 5 5 5 5 5 5 5 d d b . 
                        . . . b c c d 5 5 5 d c c b . . 
                        . . . . . . c d 5 d c . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . . . . c d c . . . . . . 
                        . . . . . . . b d b . . . . . . 
                        . . . . . . . . b . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . b d b . . . . . . 
                        . . . . . . . b d b c . . . . . 
                        . . . . b b c 5 5 5 c b b . . . 
                        . . . . b 5 5 5 1 5 5 5 b . . . 
                        . . . c c 5 5 5 1 5 5 5 c c . . 
                        . . b b 5 5 5 1 1 1 5 5 5 b b . 
                        . . d d 5 1 1 1 1 1 1 1 5 d d . 
                        . . b b 5 5 5 1 1 1 5 5 5 b b . 
                        . . . c c 5 5 5 1 5 5 5 c c . . 
                        . . . . b 5 5 5 1 5 5 5 b . . . 
                        . . . . b b c 5 5 5 c b b . . . 
                        . . . . . . c b d b c . . . . . 
                        . . . . . . . b d b . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . 1 . . . . . . . . . . 
                        . . 1 1 . . . 1 1 1 . . . . . . 
                        . . 1 1 . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                        . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . 1 . . 1 1 1 1 1 1 1 . . . . 
                        . . . . . . . 1 1 1 . . . . 1 . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite4, location3):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.coral5, on_overlap_tile)

def on_on_overlap(sprite5, otherSprite):
    sprites.destroy(otherSprite, effects.spray, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

def on_overlap_tile2(sprite3, location4):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile2)

def on_overlap_tile3(sprite2, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile3)

def on_overlap_tile4(sprite52, location42):
    tiles.set_tile_at(location42, sprites.dungeon.collectible_red_crystal)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile4)

def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy += -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . b 5 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . b 5 5 5 5 5 5 5 b b b b b . 
                        . . b 5 5 5 5 5 5 5 5 b 5 d b . 
                        . . f 4 d 5 f 1 d 5 b 5 5 b . . 
                        . . c 4 4 5 f f 1 b 5 5 d b . . 
                        . b 4 4 4 4 b f d 5 5 5 b d b b 
                        b 4 4 4 4 4 4 5 b 5 5 d c d d b 
                        . b 5 5 5 5 5 5 5 b c c d d d c 
                        . b 5 5 5 5 5 5 5 d d d d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . b 5 5 5 5 5 5 5 b b b b b . 
                        . . b 5 5 5 5 5 5 5 5 b 5 d b . 
                        . . f 4 d 5 f 1 d 5 b 5 5 b . . 
                        . . c 4 4 5 f f 1 b 5 5 d b . . 
                        b 4 4 4 4 4 b f d 5 5 5 b d b b 
                        . b 4 4 4 4 4 5 b 5 5 d c d d b 
                        . b 5 5 5 5 5 5 5 b c c d d d c 
                        . b 5 5 5 5 5 5 5 d d d d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . . c b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . f d 5 5 f 1 d 5 b b . . . . 
                        . . c 4 d 5 f f 1 5 5 b . . . . 
                        . . 4 4 d d b f d 5 5 b . . . . 
                        b 4 4 4 4 4 5 5 5 d b b d d d b 
                        . b 4 4 4 4 4 5 5 b 5 5 5 d b b 
                        . . b 5 5 5 5 5 d 5 5 5 5 c d b 
                        . b 5 5 5 5 5 5 b 5 5 d c d d c 
                        . b 5 5 5 5 5 5 5 b c c d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . c 4 d 5 f 1 d 5 b b . . . . 
                        b 4 4 4 d d f f 1 5 5 b . . . . 
                        . b 4 4 4 4 b f d 5 5 b . . . . 
                        . . b 4 4 4 4 5 5 5 5 d b . . . 
                        . . b 5 5 5 5 5 5 5 5 d d b . . 
                        . b 5 5 5 5 5 5 5 5 d d d d b . 
                        . b 5 5 5 5 5 5 5 b b b d d d b 
                        . b 5 5 5 5 5 5 c d 5 5 b d d c 
                        . b 5 5 5 5 5 5 d c d 5 d b b c 
                        . b d 5 5 5 5 5 d d c b 5 5 b . 
                        . . b b 5 5 5 d d d d c c c b b 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . c 4 d 5 f 1 d 5 b b . . . . 
                        b 4 4 4 d d f f 1 5 5 b . . . . 
                        . b 4 4 4 4 b f d 5 5 b . . . . 
                        . . b 4 4 4 4 5 5 5 5 d b . . . 
                        . . b 5 5 5 5 5 5 5 d d d b b . 
                        . b 5 5 5 5 5 5 5 b b b d d d b 
                        . b 5 5 5 5 5 5 c d 5 5 b d d c 
                        . b 5 5 5 5 5 5 d c d 5 d b b c 
                        . b 5 5 5 5 5 5 d d c b 5 5 b c 
                        . b d 5 5 5 5 5 d d d c c c b b 
                        . . b b 5 5 5 d d d c c . . . . 
                        . . . b b c c c c c . . . . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . f d 5 5 f 1 d 5 b b . . . . 
                        . . c 4 d 5 f f 1 5 5 b . . . . 
                        . . 4 4 d d b f d 5 5 b . . . . 
                        b 4 4 4 4 4 5 5 5 5 5 d b b b . 
                        . b 4 4 4 4 4 5 5 d b b d d d b 
                        . . b 5 5 5 5 5 5 b 5 5 5 d b b 
                        . b 5 5 5 5 5 5 d 5 5 5 5 c d c 
                        . b 5 5 5 5 5 5 b 5 5 d c d b c 
                        . b d 5 5 5 5 5 d b c c d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile5(sprite22, location22):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.swamp.swamp_tile2,
    on_overlap_tile5)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile6(sprite32, location23):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile6)

def on_overlap_tile7(sprite, location2):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.sapling_pine,
    on_overlap_tile7)

def on_on_overlap2(sprite6, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite7, otherSprite3):
    sprites.destroy(otherSprite3, effects.confetti, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
mySprite: Sprite = None
scene.set_background_image(img("""
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddd
        ddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3dddddddddddddddd
        ddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333ddddddddddddddd
        dddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddd
        ddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333dddddddddddddd
        ddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3dddddddddddddd
        ddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333dddddddddddddddd
        ddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333dddddddddddddd
        ddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333dddddddddddddd
        ddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333dddddddddddd
        dd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddd
        d33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbddddd
        33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd
        333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd
        d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3
        d333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3d
        33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd
        333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3
        3333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd33
        3333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd33
        3333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd33
        3333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd33
        3333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd33
        3333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd3
        3333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd33
        333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333
        33bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b333
        33b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b333
        33b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b333
        3bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b333
        3bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b33
        3bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b33
        3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb
        bb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333b
        3b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb33333333333
        3b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb33344433333
        3b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb333444333333
        44444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb334443344444
        44443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb333334444444
        44444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb333344444444
        44444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb34444344444
        44444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b4334434
        3444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b3344333
        33b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb333333
        33b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb333333
        33b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb333333
        33b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb333333
        333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333
        333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333
        333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333
        3333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb333
        33333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b3333
        33333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b33333
        33333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb333333
        33333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb33333333
        33333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb33333333
        33333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb33333333
        33333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb333333333
        33333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb3333333333
        33333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb3333333333
        33333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb3333333333
        3333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d33333333
        3333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d3
        3333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd3
        dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33
        3dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd33333333
        3dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d3333
        3dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d3
        ddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33ddd
        ddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbddddddddd
        ddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbddddddddd
        ddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbddddddddd
        ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
        ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbddddddddd
        ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
        ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
        ddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3dddddddd
        ddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3dddddddd
        ddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbdddddddd
        ddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbdddddddd
        443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444
        44444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
"""))
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.ay = 500
scene.camera_follow_sprite(mySprite)
sprites.destroy(myEnemy)
info.set_life(20)
tiles.set_current_tilemap(tilemap("""
    level1
"""))

def on_update_interval():
    global myEnemy
    myEnemy = sprites.create(img("""
            . . . . . . 3 9 . . . . . . . . 
                    . . . . . . 3 5 3 . . . . . . . 
                    . . 9 3 . . 3 1 3 . . 3 9 . . . 
                    . . 3 1 9 . 3 1 3 2 9 1 3 . . . 
                    . . . 3 1 3 9 1 9 2 1 3 . . . . 
                    3 3 3 3 2 9 9 1 9 9 3 . . . . . 
                    9 5 1 1 9 9 5 9 5 2 3 3 3 3 3 3 
                    . 3 3 9 2 9 9 1 9 9 1 1 1 1 5 9 
                    . . . . . 2 1 4 1 3 3 2 9 3 3 . 
                    . . . . 9 1 3 1 3 1 9 . . . . . 
                    . . . 3 1 3 2 1 3 3 1 3 . . . . 
                    . . 3 1 3 . 2 1 3 . 3 1 3 . . . 
                    . . 9 3 . . 3 1 3 . . 3 9 . . . 
                    . . . . . . 3 1 3 . . . . . . . 
                    . . . . . . 3 5 3 . . . . . . . 
                    . . . . . . 3 9 . . . . . . . .
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(myEnemy, sprites.dungeon.collectible_blue_crystal)
    myEnemy.follow(mySprite, 50)
game.on_update_interval(2000, on_update_interval)

def on_forever():
    music.play(music.string_playable("B A G A G F A C5 ", 200),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
