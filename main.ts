controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, -100, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.warmRadial, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite, effects.fire, 500)
    scene.cameraShake(4, 500)
})
let EnemyShip: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(5)
game.onUpdateInterval(2000, function () {
    EnemyShip = sprites.create(img`
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
        `, SpriteKind.Enemy)
    EnemyShip.x = scene.screenWidth()
    EnemyShip.vx = -20
    EnemyShip.y = randint(10, scene.screenHeight() - 0)
})
