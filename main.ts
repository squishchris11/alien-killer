controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`shoot`, mySprite, -50, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`shoot`, mySprite, 50, 0)
    projectile.startEffect(effects.spray)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprites.destroy(bad_guy)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(bad_guy)
    info.changeLifeBy(-1)
})
info.onLifeZero(function () {
    sprites.destroy(mySprite)
    game.gameOver(false)
    game.setGameOverMessage(false, "GAME OVER!")
})
info.onScore(500, function () {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
    game.setGameOverMessage(true, "you win")
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(bad_guy)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(bad_guy)
    info.changeLifeBy(-1)
})
let bad_guy: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(assets.image`little guy`, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`level`)
scene.cameraFollowSprite(mySprite)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
game.splash("hello commander aliens have entered our system use the weapon systems and you have to take them out ")
game.splash("if you kill 500 and that will get them out of our system and make sure to watch out for the Juggernaut it can instantly kill you.Use the A and B buttons to shoot them good luck commander")
game.splash("Use the A/Z and B/X buttons to shoot them good luck commander")
info.setScore(0)
info.setLife(3)
game.onUpdateInterval(2000, function () {
    bad_guy = sprites.create(assets.image`not little guy`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(bad_guy, sprites.dungeon.collectibleRedCrystal)
    bad_guy.follow(mySprite, 50)
})
