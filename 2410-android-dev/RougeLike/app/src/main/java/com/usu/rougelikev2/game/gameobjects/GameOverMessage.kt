package com.usu.rougelikev2.game.gameobjects

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.usu.rougelikev2.game.gameengine.Game
import com.usu.rougelikev2.game.gameengine.GameObject


class GameOverMessage(game: Game?) : GameObject(game!!) {
    override fun render(canvas: Canvas, paint: Paint) {
        // this object is a little different than the others as is doesn't have a position inherently.
        // its position is determined at render time.
        // here are some of the things that will be useful for you.
        // game.height // get the height of the game
        // game.width; // get the width of the game
        val isPlaying: Boolean = game.gameState["playing"]
        if (isPlaying) return
        paint.color = Color.rgb(255,0,0)
        canvas.drawRect(0f,0f, game.width, game.height, paint)
        paint.color = Color.rgb(80,80,80)
        canvas.drawOval(100f,500f, game.width-100f, game.height-500f, paint)
        paint.color = Color.RED
        paint.textSize = 100f
        canvas.drawText("GAME OVER", game.width / 2 - 280f, game.height / 2 - 50, paint)
        paint.textSize = 75f
        canvas.drawText("YOU DIED", game.width / 2 - 140f, game.height / 2 + 100f, paint)
    }
}