package com.usu.rougelikev2.game.gameobjects


import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.usu.rougelikev2.game.gameengine.Game
import com.usu.rougelikev2.game.gameengine.GameObject
import com.usu.rougelikev2.game.gameengine.Location


class Door(game: Game?) : GameObject(game!!) {
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

        // IT IS A LADDER NOT A DOOR
        // felt like it fit better thematically

        // Left Side
        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(30f, 10f, size/2-30f, size-10f, paint)
        paint.color = Color.rgb(250, 204, 157)
        canvas.drawRect(30f+2f, 10f+2f, size/2-30f-2f, size-10f-2f, paint)

        // rungs
        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(40f, 25f, size-30f, 45f, paint)
        paint.color = Color.rgb(250, 204, 157)
        canvas.drawRect(40f+2f, 25f+2f, size-30f-2f, 45f-2f, paint)

        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(40f, 65f, size-30f, 85f, paint)
        paint.color = Color.rgb(250, 204, 157)
        canvas.drawRect(40f+2f, 65f+2f, size-30f-2f, 85f-2f, paint)

        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(40f, 105f, size-30f, 125f, paint)
        paint.color = Color.rgb(250, 204, 157)
        canvas.drawRect(40f+2f, 105f+2f, size-30f-2f, 125f-2f, paint)

        // right side
        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(size/2+30f, 10f, size-30f, size-10f, paint)
        paint.color = Color.rgb(250, 204, 157)
        canvas.drawRect(size/2+30f+2f, 10f+2f, size-30f-2f, size-10f-2f, paint)
    }
}