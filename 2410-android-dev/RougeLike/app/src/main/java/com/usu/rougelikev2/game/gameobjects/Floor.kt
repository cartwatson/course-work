package com.usu.rougelikev2.game.gameobjects

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.usu.rougelikev2.game.gameengine.Game
import com.usu.rougelikev2.game.gameengine.GameObject
import com.usu.rougelikev2.game.gameengine.Location


class Floor(game: Game?) : GameObject(game!!) {
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

        // base color
        paint.color = Color.rgb(143, 143,143)
        canvas.drawRect(0f,0f, size, size, paint)

        // rotated squares
        canvas.save()
        canvas.rotate(45f, size/2, size/2)
        paint.color = Color.rgb(200,200,200)
        canvas.drawRect(23f, 23f, size-23f, size-23f, paint)
            // internal square
            canvas.save()
            canvas.rotate(45f, size/2, size/2)
            paint.color = Color.rgb(227,227,227)
            canvas.drawRect(40f, 40f, size-40f, size-40f, paint)
            canvas.restore()
        canvas.restore()

        // outline
        paint.style = Paint.Style.STROKE
        paint.color = Color.rgb(80,80,80)
        paint.strokeWidth = 2f
        canvas.drawRect(0f, 0f, size, size, paint)
    }
}
