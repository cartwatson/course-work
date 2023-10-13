package com.usu.rougelikev2.game.gameobjects

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.usu.rougelikev2.game.gameengine.Game
import com.usu.rougelikev2.game.gameengine.GameObject
import com.usu.rougelikev2.game.gameengine.Location


class BossBarrier(game: Game?) : GameObject(game!!) {
    override fun render(canvas: Canvas, paint: Paint) {
//        things you can do in this render method for reference.
//        val coords: Location = state["coords"] // gets the location of the object in the grid
//        val cellSize: Int = game.gameState["cellSize"] // gets the size of each cell in the game
//        val myX = coords.x * cellSize // gets the current x position (in pixels) in screen space
//        val myY = coords.y * cellSize // gets the current y position (in pixels) in screen space
        val coords: Location = state["coords"]
        val cellSize: Int = game.gameState["cellSize"]
        val myX = coords.x * cellSize
        val myY = coords.y * cellSize
        canvas.translate(myX, myY)
        val size = cellSize.toFloat()

        // bricks
        paint.color = Color.rgb( 222, 222, 222)
        canvas.drawRect(0f, 0f, size/2, size/2, paint)
        canvas.drawRect(size/2, size/2, size, size, paint)

        paint.color = Color.rgb(111, 111, 111)
        canvas.drawRect(0f, size/2, size/2, size, paint)
        canvas.drawRect(size/2, 0f, size, size/2, paint)
        // grout
        paint.style = Paint.Style.STROKE
        paint.color = Color.rgb(50, 50, 50)
        paint.strokeWidth = 3f
        canvas.drawRect(0f, 0f, size, size, paint)
        canvas.drawRect(0f, 0f, size/2, size/2, paint)
        canvas.drawRect(size/2, size/2, size, size, paint)
    }
}